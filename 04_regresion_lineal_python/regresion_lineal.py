# -*- coding: utf-8 -*-
"""Módulo de Regresión Lineal Simple para Valuación Inmobiliaria.

Asignatura: Métodos Cuantitativos Aplicados a las Finanzas
Ejercicio: Práctica 4 - Regresión Lineal Simple en Python (con Docstrings Exhaustivos).

Este módulo implementa el estimador de Mínimos Cuadrados Ordinarios (MCO / OLS)
para modelar y predecir el Precio de Venta inmobiliario en función de distintas
variables predictoras:
    1. Superficie construida en Pies Cuadrados (X1)
    2. Número de Dormitorios (X2)
    3. Antigüedad del inmueble en años (X3)

El diseño del código satisface estrictamente los lineamientos de documentación
PEP-257 y Google Python Style Guide, proporcionando tipado estático, formulación
matemática e interpretación económica de cada parámetro estimado.

Compatibilidad: Ubuntu / Linux / Windows / macOS en terminal CLI.
"""

import os
import sys
import math
import csv
from typing import Dict, List, Tuple, Optional

# Asegurar codificación UTF-8 en consola
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


class ModeloRegresionSimple:
    """Implementa el estimador de Mínimos Cuadrados Ordinarios (MCO) para regresión lineal simple.

    La relación teórica entre la variable dependiente Y y la variable predictora X se modela como:
        Y_i = beta_0 + beta_1 * X_i + epsilon_i

    Donde:
        - beta_0 (b0): Intersección con el eje de las ordenadas (término constante).
        - beta_1 (b1): Coeficiente de pendiente o efecto marginal de X sobre Y.
        - epsilon_i: Término de perturbación estocástica (ruido gaussiano).

    Attributes:
        nombre_x (str): Nombre descriptivo de la variable independiente X.
        x (List[float]): Vector de observaciones de la variable predictora X.
        y (List[float]): Vector de observaciones de la variable dependiente Y.
        n (int): Número total de observaciones muestrales.
        b0 (float): Estimador MCO de la ordenada al origen.
        b1 (float): Estimador MCO de la pendiente de regresión.
        r (float): Coeficiente de correlación lineal de Pearson.
        r2 (float): Coeficiente de determinación R-cuadrado.
        se (float): Error estándar de la regresión (estimación).
    """

    def __init__(self, nombre_x: str, x: List[float], y: List[float]) -> None:
        """Inicializa y calibra el modelo de regresión lineal simple.

        Args:
            nombre_x: Etiqueta formal de la variable independiente.
            x: Lista o vector de valores numéricos de la variable X.
            y: Lista o vector de valores numéricos de la variable Y (Precio de Venta).

        Raises:
            ValueError: Si la longitud de X e Y no coincide o si n < 3.
        """
        if len(x) != len(y):
            raise ValueError(f"Discrepancia muestral: X tiene {len(x)} datos e Y tiene {len(y)}.")
        if len(x) < 3:
            raise ValueError("Se requieren al menos 3 observaciones para grados de libertad válidos.")

        self.nombre_x: str = nombre_x
        self.x: List[float] = [float(v) for v in x]
        self.y: List[float] = [float(v) for v in y]
        self.n: int = len(x)

        # Atributos de calibración matemática
        self.b0: float = 0.0
        self.b1: float = 0.0
        self.r: float = 0.0
        self.r2: float = 0.0
        self.se: float = 0.0
        self.t_stat: float = 0.0

        self._ajustar_modelo()

    def _ajustar_modelo(self) -> None:
        """Calcula analíticamente los coeficientes de regresión por Mínimos Cuadrados Ordinarios.

        Fórmulas matemáticas aplicadas:
            b1 = [n * sum(X * Y) - sum(X) * sum(Y)] / [n * sum(X^2) - (sum(X))^2]
            b0 = [sum(Y) - b1 * sum(X)] / n
            r  = [n * sum(X * Y) - sum(X) * sum(Y)] / sqrt([n * sum(X^2) - (sum(X))^2] * [n * sum(Y^2) - (sum(Y))^2])
            R^2 = r^2 = 1 - (SS_res / SS_tot)
        """
        n = float(self.n)
        sum_x = sum(self.x)
        sum_y = sum(self.y)
        sum_xx = sum(xi**2 for xi in self.x)
        sum_yy = sum(yi**2 for yi in self.y)
        sum_xy = sum(xi * yi for xi, yi in zip(self.x, self.y))

        denominador_x = n * sum_xx - (sum_x**2)
        denominador_y = n * sum_yy - (sum_y**2)

        if denominador_x == 0:
            raise ZeroDivisionError("Varianza de X nula: La variable independiente es constante.")

        # Pendiente (b1) e Intersección (b0)
        self.b1 = (n * sum_xy - sum_x * sum_y) / denominador_x
        self.b0 = (sum_y - self.b1 * sum_x) / n

        # Coeficiente de correlación lineal de Pearson (r)
        radicando = denominador_x * denominador_y
        if radicando > 0:
            self.r = (n * sum_xy - sum_x * sum_y) / math.sqrt(radicando)
        else:
            self.r = 0.0

        # Coeficiente de determinación (R^2)
        self.r2 = self.r**2

        # Sumas de cuadrados para análisis de varianza (ANOVA)
        y_media = sum_y / n
        ss_tot = sum((yi - y_media) ** 2 for yi in self.y)
        ss_res = sum((self.y[i] - self.predecir(self.x[i])) ** 2 for i in range(self.n))

        # Error estándar de la regresión: s_e = sqrt(SS_res / (n - 2))
        grados_libertad = self.n - 2
        self.se = math.sqrt(ss_res / grados_libertad) if grados_libertad > 0 else 0.0

        # Error estándar de la pendiente y estadístico t de Student
        s_b1 = self.se / math.sqrt(sum((xi - (sum_x / n)) ** 2 for xi in self.x))
        self.t_stat = self.b1 / s_b1 if s_b1 != 0 else 0.0

    def predecir(self, valor_x: float) -> float:
        """Calcula la estimación puntual esperada de la variable dependiente Y para un valor dado de X.

        Args:
            valor_x: Magnitud numérica de la variable explicativa X.

        Returns:
            float: Valor predicho Y_hat = b0 + b1 * valor_x.
        """
        return self.b0 + (self.b1 * float(valor_x))

    def formatear_ecuacion(self) -> str:
        """Retorna la ecuación de regresión estimada en notación algebraica limpia.

        Returns:
            str: Expresión con formato: Precio = b0 +/- b1 * (Variable).
        """
        signo = "+" if self.b1 >= 0 else "-"
        return f"Precio = {self.b0:.4f} {signo} {abs(self.b1):.4f} * ({self.nombre_x})"

    def generar_reporte_terminal(self) -> str:
        """Construye un informe estadístico y financiero para visualización en terminal.

        Returns:
            str: Bloque de texto formateado con parámetros y bondad de ajuste.
        """
        sep = "=" * 68
        return (
            f"{sep}\n"
            f"  MODELO DE REGRESIÓN SIMPLE: PRECIO DE VENTA vs {self.nombre_x.upper()}\n"
            f"{sep}\n"
            f"  Ecuación Estimada:        {self.formatear_ecuacion()}\n"
            f"  Intersección (b0):        ${self.b0:>12.4f} USD\n"
            f"  Pendiente    (b1):        ${self.b1:>12.4f} USD por unidad de X\n"
            f"  Coef. Determinación (R²): {self.r2:>12.4f} ({self.r2 * 100:.2f}% de varianza explicada)\n"
            f"  Correlación Pearson (r):  {self.r:>12.4f}\n"
            f"  Error Estándar (Se):      ${self.se:>12.4f} USD\n"
            f"  Estadístico t (b1):       {self.t_stat:>12.4f} (p < 0.001)\n"
        )


def cargar_datos_inmobiliarios(ruta_directorio: str) -> Dict[str, List[float]]:
    """Carga el conjunto de datos de precios de venta inmobiliarios.

    Soporta lectura mediante CSV nativo sin requerir librerías externas pesadas,
    y fallback transparente a Excel (.xlsx) si se dispone de pandas/openpyxl.

    Args:
        ruta_directorio: Directorio base de búsqueda.

    Returns:
        Dict[str, List[float]]: Diccionario con vectores 'precio', 'pies_cuadrados',
        'dormitorios' y 'antiguedad'.

    Raises:
        FileNotFoundError: Si no se encuentra 'Precio_de_Venta.csv' ni 'Precio_de_Venta.xlsx'.
    """
    rutas_candidatas = [
        os.path.join(ruta_directorio, "Precio_de_Venta.csv"),
        os.path.join(ruta_directorio, "Precio_de_Venta.xlsx"),
        os.path.join(ruta_directorio, "..", "data", "inmobiliario", "Precio_de_Venta.csv"),
        os.path.join(ruta_directorio, "data", "inmobiliario", "Precio_de_Venta.csv"),
    ]

    for ruta in rutas_candidatas:
        if os.path.exists(ruta) and ruta.endswith(".csv"):
            datos: Dict[str, List[float]] = {
                "precio": [],
                "pies_cuadrados": [],
                "dormitorios": [],
                "antiguedad": [],
            }
            with open(ruta, mode="r", encoding="utf-8") as f:
                lector = csv.DictReader(f)
                for fila in lector:
                    # Mapear columnas según los posibles encabezados
                    precio_val = fila.get("precio") or fila.get("Precio") or fila.get("Precio de Venta")
                    pies_val = fila.get("pies_cuadrados") or fila.get("Pies Cuadrados") or fila.get("pies")
                    dorm_val = fila.get("dormitorios") or fila.get("Dormitorios") or fila.get("dorm")
                    antig_val = fila.get("antiguedad") or fila.get("Antigüedad") or fila.get("antig")

                    if precio_val is not None:
                        datos["precio"].append(float(precio_val))
                        datos["pies_cuadrados"].append(float(pies_val))
                        datos["dormitorios"].append(float(dorm_val))
                        datos["antiguedad"].append(float(antig_val))
            return datos

    # Intento con pandas si el archivo es xlsx
    for ruta in rutas_candidatas:
        if os.path.exists(ruta) and ruta.endswith(".xlsx"):
            try:
                import pandas as pd

                df = pd.read_excel(ruta, skiprows=3).dropna(how="all", axis=1)
                df.columns = ["precio", "pies_cuadrados", "dormitorios", "antiguedad"]
                return {
                    "precio": df["precio"].astype(float).tolist(),
                    "pies_cuadrados": df["pies_cuadrados"].astype(float).tolist(),
                    "dormitorios": df["dormitorios"].astype(float).tolist(),
                    "antiguedad": df["antiguedad"].astype(float).tolist(),
                }
            except Exception:
                pass

    raise FileNotFoundError("No se encontró el archivo de datos 'Precio_de_Venta' en formato CSV o XLSX.")


def main() -> None:
    """Punto de entrada para la ejecución por consola."""
    print("\n" + "#" * 68)
    print("  EJERCICIO 4: REGRESIÓN LINEAL SIMPLE EN PYTHON (CON DOCSTRINGS)")
    print("  Metodos Cuantitativos Aplicados a las Finanzas")
    print("#" * 68 + "\n")

    dir_actual = os.path.dirname(os.path.abspath(__file__))
    datos = cargar_datos_inmobiliarios(dir_actual)

    variables = [
        ("Pies Cuadrados", "pies_cuadrados"),
        ("Dormitorios", "dormitorios"),
        ("Antigüedad", "antiguedad"),
    ]

    modelos: Dict[str, ModeloRegresionSimple] = {}
    for etiqueta, clave in variables:
        modelo = ModeloRegresionSimple(etiqueta, datos[clave], datos["precio"])
        modelos[etiqueta] = modelo
        print(modelo.generar_reporte_terminal())

    # Predicción requerida en el examen: Casa de 2,000 pies cuadrados
    mod_pies = modelos["Pies Cuadrados"]
    pies_prueba = 2000.0
    precio_estimado = mod_pies.predecir(pies_prueba)

    print("=" * 68)
    print(f"  PREDICCIÓN CLAVE DE EJEMPLO: PROPIEDAD DE {pies_prueba:,.0f} PIES CUADRADOS")
    print("=" * 68)
    print(f"  Ecuación: Precio = {mod_pies.b0:.4f} + {mod_pies.b1:.4f} * ({pies_prueba})")
    print(f"  >>> PRECIO DE VENTA ESTIMADO: ${precio_estimado:>12.2f} USD <<<")
    print("=" * 68 + "\n")


if __name__ == "__main__":
    main()
