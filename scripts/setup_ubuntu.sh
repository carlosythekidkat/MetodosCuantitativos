#!/bin/bash
# ==============================================================================
# Script de Configuración de Entorno en Ubuntu / Debian
# Asignatura: Métodos Cuantitativos Aplicados a las Finanzas
# Repositorio: MetodosCuantitativos
# ==============================================================================

set -e

echo ">>> Actualizando lista de paquetes e instalando dependencias base..."
sudo apt-get update
sudo apt-get install -y python3 python3-pip python3-venv r-base

echo ">>> Creando entorno virtual de Python (.venv)..."
python3 -m venv .venv
source .venv/bin/activate

echo ">>> Instalando dependencias desde requirements.txt..."
pip install --upgrade pip
pip install -r requirements.txt

echo ">>> Verificando instalación..."
python3 --version
Rscript --version

echo "======================================================================"
echo " Entorno configurado exitosamente."
echo " Para activar el entorno virtual ejecuta: source .venv/bin/activate"
echo " Para correr todas las prácticas ejecuta: ./scripts/run_all.sh"
echo "======================================================================"
