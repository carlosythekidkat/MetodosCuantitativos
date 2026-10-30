# -*- coding: utf-8 -*-
"""Práctica 5 (Contraparte Python): Regresión Lineal Múltiple Matricial.

Asignatura: Métodos Cuantitativos Aplicados a las Finanzas
Objetivo:
    Validar y replicar analíticamente mediante álgebra lineal y Mínimos Cuadrados
    Ordinarios (MCO) los dos modelos multivariados de R:
    1. Modelo de 2 Variables (Pies Cuadrados + Dormitorios)
    2. Modelo de 3 Variables (Pies Cuadrados + Dormitorios + Antigüedad)

Compatibilidad: CLI terminal pura (Ubuntu / Linux / Windows / macOS).
"""

import os
import sys
import csv
import math
from typing import Dict, List, Tuple

# Asegurar codificación UTF-8 en consola
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


def cargar_datos() -> Dict[str, List[float]]:
    """Carga los datos inmobiliarios desde CSV o XLSX."""
    dir_actual = os.path.dirname(os.path.abspath(__file__))
    candidatos = [
        os.path.join(dir_actual, "Precio_de_Venta.csv"),
        os.path.join(dir_actual, "Precio_de_Venta.xlsx"),
        os.path.join(dir_actual, "..", "data", "inmobiliario", "Precio_de_Venta.csv"),
    ]

    for ruta in candidatos:
        if os.path.exists(ruta) and ruta.endswith(".csv"):
            datos: Dict[str, List[float]] = {
                "precio": [],
                "pies": [],
                "dorm": [],
                "antig": [],
            }
            with open(ruta, mode="r", encoding="utf-8") as f:
                lector = csv.DictReader(f)
                for fila in lector:
                    precio = fila.get("precio") or fila.get("Precio") or fila.get("Precio de Venta")
                    pies = fila.get("pies_cuadrados") or fila.get("Pies Cuadrados") or fila.get("pies")
                    dorm = fila.get("dormitorios") or fila.get("Dormitorios") or fila.get("dorm")
                    antig = fila.get("antiguedad") or fila.get("Antigüedad") or fila.get("antig")

                    if precio is not None:
                        datos["precio"].append(float(precio))
                        datos["pies"].append(float(pies))
                        datos["dorm"].append(float(dorm))
                        datos["antig"].append(float(antig))
            return datos

    for ruta in candidatos:
        if os.path.exists(ruta) and ruta.endswith(".xlsx"):
            try:
                import pandas as pd

                df = pd.read_excel(ruta, skiprows=3).dropna(how="all", axis=1)
                df.columns = ["precio", "pies", "dorm", "antig"]
                return {
                    "precio": df["precio"].astype(float).tolist(),
                    "pies": df["pies"].astype(float).tolist(),
                    "dorm": df["dorm"].astype(float).tolist(),
                    "antig": df["antig"].astype(float).tolist(),
                }
            except Exception:
                pass

    raise FileNotFoundError("No se encontró el archivo de datos Precio_de_Venta.")


def resolver_sistema_lineal(A: List[List[float]], b: List[float]) -> List[float]:
    """Resuelve un sistema matricial Ax = b mediante Eliminación Gaussiana con pivoteo parcial."""
    n = len(b)
    # Crear matriz aumentada
    M = [A[i][:] + [b[i]] for i in range(n)]

    for i in range(n):
        # Pivoteo parcial
        max_fila = i
        for k in range(i + 1, n):
            if abs(M[k][i]) > abs(M[max_fila][i]):
                max_fila = k
        M[i], M[max_fila] = M[max_fila], M[i]

        pivote = M[i][i]
        if abs(pivote) < 1e-12:
            raise ZeroDivisionError("Matriz singular: colinealidad perfecta entre predictores.")

        for j in range(i, n + 1):
            M[i][j] /= pivote

        for k in range(n):
            if k != i:
                factor = M[k][i]
                for j in range(i, n + 1):
                    M[k][j] -= factor * M[i][j]

    return [M[i][n] for i in range(n)]


def ajustar_mco_multivariado(X_mat: List[List[float]], y: List[float]) -> Tuple[List[float], float, float, float]:
    """Calcula coeficientes MCO: beta = (X^T * X)^(-1) * X^T * y.

    Args:
        X_mat: Matriz de diseño con columna de 1s para intercepto y predictores.
        y: Vector de la variable dependiente.

    Returns:
        Tuple: (betas, R2, R2_ajustado, Se)
    """
    n = len(y)
    k = len(X_mat[0]) - 1  # Número de variables explicativas excluyendo intercepto

    # Calcular X^T * X
    num_cols = k + 1
    XtX = [[0.0] * num_cols for _ in range(num_cols)]
    for i in range(num_cols):
        for j in range(num_cols):
            XtX[i][j] = sum(X_mat[row][i] * X_mat[row][j] for row in range(n))

    # Calcular X^T * y
    Xty = [sum(X_mat[row][i] * y[row] for row in range(n)) for i in range(num_cols)]

    # Resolver beta
    betas = resolver_sistema_lineal(XtX, Xty)

    # Predicciones y sumas de cuadrados
    y_pred = [sum(betas[j] * X_mat[row][j] for j in range(num_cols)) for row in range(n)]
    y_bar = sum(y) / n
    ss_tot = sum((y[i] - y_bar) ** 2 for i in range(n))
    ss_res = sum((y[i] - y_pred[i]) ** 2 for i in range(n))

    r2 = 1.0 - (ss_res / ss_tot)
    r2_adj = 1.0 - ((ss_res / (n - k - 1)) / (ss_tot / (n - 1)))
    se = math.sqrt(ss_res / (n - k - 1))

    return betas, r2, r2_adj, se


def main() -> None:
    """Punto de entrada de validación en Python para Práctica 5."""
    datos = cargar_datos()
    n = len(datos["precio"])
    y = datos["precio"]
    x1 = datos["pies"]
    x2 = datos["dorm"]
    x3 = datos["antig"]

    print("\n" + "#" * 68)
    print("  EJERCICIO 5 (VALIDACIÓN PYTHON): REGRESIÓN MÚLTIPLE MATRICIAL")
    print("  Metodos Cuantitativos Aplicados a las Finanzas")
    print("#" * 68 + "\n")

    # 1. Modelo 2 variables
    X2 = [[1.0, x1[i], x2[i]] for i in range(n)]
    b2, r2_2, r2_adj2, se2 = ajustar_mco_multivariado(X2, y)
    pred_2 = b2[0] + b2[1] * 2000.0 + b2[2] * 3.0

    print("=" * 68)
    print("  1. MODELO MÚLTIPLE DE 2 VARIABLES (Pies + Dormitorios)")
    print("=" * 68)
    print(f"  Ecuación: Precio = {b2[0]:.4f} + {b2[1]:.4f}*(Pies) - {abs(b2[2]):.4f}*(Dorm)")
    print(f"  R² = {r2_2:.4f} ({r2_2 * 100:.2f}%) | R² Ajustado = {r2_adj2:.4f} | Se = ${se2:,.2f}")
    print(f"  >>> PREDICCIÓN (2,000 pies², 3 dorm): ${pred_2:>10.2f} USD <<<")
    print("--------------------------------------------------------------------\n")

    # 2. Modelo 3 variables
    X3 = [[1.0, x1[i], x2[i], x3[i]] for i in range(n)]
    b3, r2_3, r2_adj3, se3 = ajustar_mco_multivariado(X3, y)
    pred_3 = b3[0] + b3[1] * 2000.0 + b3[2] * 3.0 + b3[3] * 10.0

    print("=" * 68)
    print("  2. MODELO MÚLTIPLE DE 3 VARIABLES (+ Antigüedad)")
    print("=" * 68)
    print(f"  Ecuación: Precio = {b3[0]:.4f} + {b3[1]:.4f}*(Pies) - {abs(b3[2]):.4f}*(Dorm) - {abs(b3[3]):.4f}*(Antig)")
    print(f"  R² = {r2_3:.4f} ({r2_3 * 100:.2f}%) | R² Ajustado = {r2_adj3:.4f} | Se = ${se3:,.2f}")
    print(f"  >>> PREDICCIÓN (2,000 pies², 3 dorm, 10 años): ${pred_3:>10.2f} USD <<<")
    print("=" * 68 + "\n")


if __name__ == "__main__":
    main()
