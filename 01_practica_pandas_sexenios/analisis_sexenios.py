# -*- coding: utf-8 -*-
"""Práctica 1: Análisis Estadístico de Sexenios con Pandas.

Asignatura: Métodos Cuantitativos Aplicados a las Finanzas
Objetivo:
    Calcular las métricas estadísticas descriptivas del Tipo de Cambio USD/MXN
    (FIX - Determinación Banco de México) para dos periodos sexenales:
    - Media aritmética
    - Varianza muestral
    - Desviación estándar muestral
    - Valor Máximo
    - Valor Mínimo
    - Rango muestral (Máximo - Mínimo)

Compatibilidad: Ubuntu / Linux / macOS / Windows en terminal CLI.
"""

import os
import sys
import argparse
from typing import Dict, Tuple
import pandas as pd

# Asegurar codificación UTF-8 en consola
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


def cargar_serie_tipo_cambio(ruta_base: str, nombre_archivo_base: str) -> pd.Series:
    """Carga y limpia la serie temporal de tipo de cambio oficial FIX.

    Intenta primero leer el archivo .csv para máxima velocidad y evitar
    dependencias de motores binarios de Excel en entornos Linux mínimos.
    Si no existe el .csv, recurre a .xls omitiendo encabezados de Banxico.

    Args:
        ruta_base: Directorio donde reside el archivo.
        nombre_archivo_base: Nombre base (ej. 'sexenio-1').

    Returns:
        pd.Series: Serie numérica limpia sin valores nulos ni encabezados.

    Raises:
        FileNotFoundError: Si no se encuentra ni la versión .csv ni .xls.
    """
    ruta_csv = os.path.join(ruta_base, f"{nombre_archivo_base}.csv")
    ruta_xls = os.path.join(ruta_base, f"{nombre_archivo_base}.xls")

    if os.path.exists(ruta_csv):
        df = pd.read_csv(ruta_csv)
        # La columna 'Determinacion' contiene el tipo de cambio FIX oficial
        if "Determinacion" in df.columns:
            serie = pd.to_numeric(df["Determinacion"], errors="coerce").dropna()
        else:
            serie = pd.to_numeric(df.iloc[:, 1], errors="coerce").dropna()
        return serie

    if os.path.exists(ruta_xls):
        # Banxico incluye 6 filas de metadatos institucionales
        df = pd.read_excel(ruta_xls, skiprows=6).iloc[1:]
        serie = pd.to_numeric(df.iloc[:, 1], errors="coerce").dropna()
        return serie

    raise FileNotFoundError(
        f"No se encontró el conjunto de datos para '{nombre_archivo_base}' en: {ruta_base}"
    )


def calcular_metricas(serie: pd.Series) -> Dict[str, float]:
    """Calcula las 6 métricas financieras y estadísticas fundamentales.

    Args:
        serie: Serie de Pandas con valores numéricos continuos.

    Returns:
        Dict[str, float]: Diccionario con media, varianza, desviación estándar,
        máximo, mínimo y rango muestral.
    """
    media = float(serie.mean())
    varianza = float(serie.var(ddof=1))  # Varianza muestral insesgada (n-1)
    desv_std = float(serie.std(ddof=1)) # Desviación estándar muestral
    maximo = float(serie.max())
    minimo = float(serie.min())
    rango = maximo - minimo

    return {
        "media": media,
        "varianza": varianza,
        "desv_std": desv_std,
        "maximo": maximo,
        "minimo": minimo,
        "rango": rango,
        "observaciones": len(serie),
    }


def imprimir_reporte_sexenio(titulo: str, metricas: Dict[str, float]) -> None:
    """Imprime el reporte en formato legible y elegante para terminal CLI."""
    linea = "=" * 62
    print(f"\n{linea}")
    print(f"       {titulo.upper()} ({metricas['observaciones']} observaciones)")
    print(linea)
    print(f"  MEDIA:               {metricas['media']:>12.4f} MXN/USD")
    print(f"  VARIANZA:            {metricas['varianza']:>12.4f}")
    print(f"  DESVIACION ESTANDAR: {metricas['desv_std']:>12.4f} MXN")
    print(f"  MAXIMO:              {metricas['maximo']:>12.4f} MXN/USD")
    print(f"  MINIMO:              {metricas['minimo']:>12.4f} MXN/USD")
    print(f"  RANGO:               {metricas['rango']:>12.4f} MXN")
    print(linea)


def main() -> None:
    """Punto de entrada principal para la ejecución en consola."""
    parser = argparse.ArgumentParser(
        description="Práctica Pandas: Análisis Estadístico del Tipo de Cambio por Sexenios"
    )
    parser.add_argument(
        "--data-dir",
        type=str,
        default=os.path.dirname(os.path.abspath(__file__)),
        help="Directorio donde se ubican los archivos de datos",
    )
    args = parser.parse_args()

    data_dir = args.data_dir
    # Buscar datos localmente o en carpeta global data/sexenios
    if not os.path.exists(os.path.join(data_dir, "sexenio-1.csv")) and not os.path.exists(
        os.path.join(data_dir, "sexenio-1.xls")
    ):
        alt_dir = os.path.abspath(os.path.join(data_dir, "..", "data", "sexenios"))
        if os.path.exists(alt_dir):
            data_dir = alt_dir

    print("\n" + "#" * 62)
    print("  EJERCICIO 1: ANALISIS ESTADISTICO EN PANDAS (SEXENIOS)")
    print("  Metodos Cuantitativos Aplicados a las Finanzas")
    print("#" * 62)

    serie1 = cargar_serie_tipo_cambio(data_dir, "sexenio-1")
    metricas1 = calcular_metricas(serie1)
    imprimir_reporte_sexenio("RESULTADOS: SEXENIO 1", metricas1)

    serie2 = cargar_serie_tipo_cambio(data_dir, "sexenio-2")
    metricas2 = calcular_metricas(serie2)
    imprimir_reporte_sexenio("RESULTADOS: SEXENIO 2", metricas2)

    # Comparativa financiera
    dif_media = metricas2["media"] - metricas1["media"]
    pct_cambio = (dif_media / metricas1["media"]) * 100
    print("\n>>> SINTESIS COMPARATIVA FINANCIERA:")
    print(f"    Incremento medio del tipo de cambio: +${dif_media:.4f} MXN (+{pct_cambio:.2f}%)")
    print(
        f"    Volatilidad (Desv. Std.): Sexenio 1 = {metricas1['desv_std']:.4f} vs Sexenio 2 = {metricas2['desv_std']:.4f}"
    )
    if metricas1["desv_std"] > metricas2["desv_std"]:
        print("    Interpretación: El Sexenio 1 presentó mayor dispersión y volatilidad cambiaria.")
    else:
        print("    Interpretación: El Sexenio 2 presentó mayor dispersión y volatilidad cambiaria.")
    print("-" * 62 + "\n")


if __name__ == "__main__":
    main()
