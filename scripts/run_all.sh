#!/bin/bash
# ==============================================================================
# Script de Ejecución Automatizada para Terminal Ubuntu / Debian / Linux
# Asignatura: Métodos Cuantitativos Aplicados a las Finanzas
# Repositorio: MetodosCuantitativos
# ==============================================================================

set -e

# Colores para salida en terminal
VERDE='\033[0;32m'
AZUL='\033[0;34m'
AMARILLO='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

echo -e "${CYAN}======================================================================${NC}"
echo -e "${CYAN}   MÉTODOS CUANTITATIVOS APLICADOS A LAS FINANZAS (EVALUACIÓN)       ${NC}"
echo -e "${CYAN}   Ejecución Automatizada de las 5 Evidencias de Examen              ${NC}"
echo -e "${CYAN}======================================================================${NC}\n"

# 1. Verificar intérprete de Python
if command -v python3 &>/dev/null; then
    PY_CMD="python3"
elif command -v python &>/dev/null; then
    PY_CMD="python"
else
    echo -e "${AMARILLO}[ERROR]: Python no está instalado en este sistema.${NC}"
    exit 1
fi

echo -e "${VERDE}[1/5] Ejecutando: Práctica pandas (sexenios)...${NC}"
$PY_CMD 01_practica_pandas_sexenios/analisis_sexenios.py

echo -e "\n${VERDE}[2/5] Ejecutando: Práctica en R (sexenios)...${NC}"
if command -v Rscript &>/dev/null; then
    Rscript 02_practica_r_sexenios/analisis_sexenios.R
else
    echo -e "${AMARILLO}[AVISO]: Rscript no está disponible. Para instalar en Ubuntu: sudo apt install -y r-base${NC}"
    echo -e "${AMARILLO}Ejecutando versión equivalente en Python:${NC}"
    $PY_CMD 01_practica_pandas_sexenios/analisis_sexenios.py
fi

echo -e "\n${VERDE}[3/5] Ejecutando: Modelo de punto equilibrio (Excel y Python)...${NC}"
$PY_CMD 03_punto_equilibrio_excel_python/punto_equilibrio.py

echo -e "\n${VERDE}[4/5] Ejecutando: Regresión lineal en Python (docstrings completos)...${NC}"
$PY_CMD 04_regresion_lineal_python/regresion_lineal.py

echo -e "\n${VERDE}[5/5] Ejecutando: Regresión lineal múltiple R...${NC}"
if command -v Rscript &>/dev/null; then
    Rscript 05_regresion_lineal_multiple_r/regresion_multiple.R
else
    echo -e "${AMARILLO}[AVISO]: Rscript no está disponible. Ejecutando contraparte validada en Python:${NC}"
    $PY_CMD 05_regresion_lineal_multiple_r/regresion_multiple.py
fi

echo -e "\n${CYAN}======================================================================${NC}"
echo -e "${VERDE}   ¡TODAS LAS PRÁCTICAS FUERON EJECUTADAS SATISFACTORIAMENTE!        ${NC}"
echo -e "${CYAN}======================================================================${NC}\n"
