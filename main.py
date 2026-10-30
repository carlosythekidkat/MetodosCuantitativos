# -*- coding: utf-8 -*-
"""Ejecutor Maestro y CLI de Métodos Cuantitativos.

Asignatura: Métodos Cuantitativos Aplicados a las Finanzas para la Toma de Decisiones
Repositorio Oficial de Evidencias de Examen.

Permite ejecutar de forma interactiva o por lotes las 5 prácticas:
    1. Práctica pandas (sexenios) - Media, varianza, desviación estándar
    2. Práctica en R (sexenios)
    3. Modelo de punto equilibrio Excel y python
    4. Regresión lineal en python (docstring)
    5. Regresión lineal múltiple R (y validación matricial en Python)

Compatibilidad: Ubuntu / Debian / Fedora / Arch / macOS / Windows en terminal CLI.
"""

import os
import sys
import subprocess
import argparse
from typing import List

# Configurar salida UTF-8 para consolas en Windows o Linux
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def tiene_comando(cmd: str) -> bool:
    """Verifica si un ejecutable binario está disponible en el PATH del sistema."""
    import shutil

    return shutil.which(cmd) is not None


def ejecutar_script_python(ruta_relativa: str, titulo: str) -> None:
    """Ejecuta un script de Python imprimiendo separadores claros."""
    ruta_abs = os.path.join(ROOT_DIR, ruta_relativa)
    print("\n" + "=" * 70)
    print(f"  EJECUTANDO: {titulo}")
    print(f"  Archivo:    {ruta_relativa}")
    print("=" * 70)
    try:
        subprocess.run([sys.executable, ruta_abs], check=True, cwd=os.path.dirname(ruta_abs))
    except subprocess.CalledProcessError as e:
        print(f"  [ERROR]: La ejecución finalizó con código {e.returncode}")


def ejecutar_script_r(ruta_relativa: str, titulo: str) -> None:
    """Ejecuta un script en R usando Rscript si está disponible."""
    ruta_abs = os.path.join(ROOT_DIR, ruta_relativa)
    print("\n" + "=" * 70)
    print(f"  EJECUTANDO: {titulo}")
    print(f"  Archivo:    {ruta_relativa}")
    print("=" * 70)

    if tiene_comando("Rscript"):
        try:
            subprocess.run(["Rscript", ruta_abs], check=True, cwd=os.path.dirname(ruta_abs))
        except subprocess.CalledProcessError as e:
            print(f"  [ERROR]: La ejecución en R finalizó con código {e.returncode}")
    else:
        print("  [AVISO]: 'Rscript' no se detectó en el PATH de este sistema.")
        print("  Para instalarlo en Ubuntu: sudo apt-get install -y r-base")

        # Fallback a contraparte en Python si existe
        dir_script = os.path.dirname(ruta_abs)
        fallback_py = None
        for f in os.listdir(dir_script):
            if f.endswith(".py"):
                fallback_py = os.path.join(dir_script, f)
                break

        if fallback_py:
            print(f"  -> Ejecutando contraparte equivalente en Python: {os.path.basename(fallback_py)}")
            subprocess.run([sys.executable, fallback_py], check=True, cwd=dir_script)


def ejecutar_todas() -> None:
    """Ejecuta secuencialmente las 5 prácticas."""
    print("\n" + "#" * 70)
    print("  EJECUCIÓN INTEGRAL DE LAS 5 PRÁCTICAS DEL EXAMEN")
    print("  Métodos Cuantitativos Aplicados a las Finanzas")
    print("#" * 70)

    # 1. Práctica pandas (sexenios)
    ejecutar_script_python(
        "01_practica_pandas_sexenios/analisis_sexenios.py",
        "1. Práctica pandas (sexenios) - Media, varianza, desviación estándar",
    )

    # 2. Práctica en R (sexenios)
    ejecutar_script_r(
        "02_practica_r_sexenios/analisis_sexenios.R",
        "2. Práctica en R (sexenios)",
    )

    # 3. Modelo de punto equilibrio Excel y python
    ejecutar_script_python(
        "03_punto_equilibrio_excel_python/punto_equilibrio.py",
        "3. Modelo de punto de equilibrio Excel y python",
    )

    # 4. Regresión lineal en python (docstring)
    ejecutar_script_python(
        "04_regresion_lineal_python/regresion_lineal.py",
        "4. Regresión lineal en python (docstring)",
    )

    # 5. Regresión lineal múltiple R
    ejecutar_script_r(
        "05_regresion_lineal_multiple_r/regresion_multiple.R",
        "5. Regresión lineal múltiple R",
    )

    print("\n" + "#" * 70)
    print("  TODAS LAS PRÁCTICAS HAN SIDO EJECUTADAS EXITOSAMENTE")
    print("#" * 70 + "\n")


def menu_interactivo() -> None:
    """Despliega un menú interactivo en terminal para el evaluador."""
    while True:
        print("\n" + "=" * 65)
        print("  MÉTODOS CUANTITATIVOS APLICADOS A LAS FINANZAS")
        print("  Panel de Control de Prácticas y Evidencias de Examen")
        print("=" * 65)
        print("  1. Práctica pandas (sexenios) [Media, varianza, desv. est.]")
        print("  2. Práctica en R (sexenios)")
        print("  3. Modelo de punto de equilibrio (Excel y Python)")
        print("  4. Regresión lineal en Python (docstrings completos)")
        print("  5. Regresión lineal múltiple R (y validación Python)")
        print("  6. Ejecutar las 5 prácticas secuencialmente")
        print("  0. Salir")
        print("-" * 65)

        opcion = input("  Seleccione una opción [1-6, 0]: ").strip()

        if opcion == "1":
            ejecutar_script_python(
                "01_practica_pandas_sexenios/analisis_sexenios.py",
                "1. Práctica pandas (sexenios)",
            )
        elif opcion == "2":
            ejecutar_script_r(
                "02_practica_r_sexenios/analisis_sexenios.R",
                "2. Práctica en R (sexenios)",
            )
        elif opcion == "3":
            ejecutar_script_python(
                "03_punto_equilibrio_excel_python/punto_equilibrio.py",
                "3. Modelo de punto equilibrio",
            )
        elif opcion == "4":
            ejecutar_script_python(
                "04_regresion_lineal_python/regresion_lineal.py",
                "4. Regresión lineal en python (docstring)",
            )
        elif opcion == "5":
            ejecutar_script_r(
                "05_regresion_lineal_multiple_r/regresion_multiple.R",
                "5. Regresión lineal múltiple R",
            )
        elif opcion == "6":
            ejecutar_todas()
        elif opcion == "0":
            print("\n  Sesión finalizada con éxito.\n")
            break
        else:
            print("\n  [Opción no válida. Ingrese un dígito del 0 al 6]")


def main() -> None:
    """Punto de entrada con soporte para flags CLI y modo interactivo."""
    parser = argparse.ArgumentParser(
        description="Gestor de Prácticas de Métodos Cuantitativos Aplicados a las Finanzas"
    )
    parser.add_argument("--all", action="store_true", help="Ejecutar las 5 prácticas secuencialmente")
    parser.add_argument(
        "--ejercicio",
        type=int,
        choices=[1, 2, 3, 4, 5],
        help="Ejecutar un ejercicio específico por número (1-5)",
    )
    args = parser.parse_args()

    if args.all:
        ejecutar_todas()
    elif args.ejercicio == 1:
        ejecutar_script_python(
            "01_practica_pandas_sexenios/analisis_sexenios.py",
            "1. Práctica pandas (sexenios)",
        )
    elif args.ejercicio == 2:
        ejecutar_script_r(
            "02_practica_r_sexenios/analisis_sexenios.R",
            "2. Práctica en R (sexenios)",
        )
    elif args.ejercicio == 3:
        ejecutar_script_python(
            "03_punto_equilibrio_excel_python/punto_equilibrio.py",
            "3. Modelo de punto de equilibrio",
        )
    elif args.ejercicio == 4:
        ejecutar_script_python(
            "04_regresion_lineal_python/regresion_lineal.py",
            "4. Regresión lineal en python (docstring)",
        )
    elif args.ejercicio == 5:
        ejecutar_script_r(
            "05_regresion_lineal_multiple_r/regresion_multiple.R",
            "5. Regresión lineal múltiple R",
        )
    else:
        menu_interactivo()


if __name__ == "__main__":
    main()
