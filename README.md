# Métodos Cuantitativos Aplicados a las Finanzas para la Toma de Decisiones

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python)](https://www.python.org/)
[![R Language](https://img.shields.io/badge/R-%3E%3D4.0-blue.svg?logo=r)](https://www.r-project.org/)
[![Ubuntu Compatible](https://img.shields.io/badge/OS-Ubuntu%20%7C%20Linux%20%7C%20Windows-green.svg?logo=ubuntu)](https://ubuntu.com/)
[![CLI Terminal Ready](https://img.shields.io/badge/Mode-Pure%20CLI%20Terminal-orange.svg)](https://github.com/carlosythekidkat/MetodosCuantitativos)
[![Zero Images Policy](https://img.shields.io/badge/Visuals-Pure%20Code%20Output-purple.svg)](https://github.com/carlosythekidkat/MetodosCuantitativos)

> **Repositorio Oficial de Evaluación:** Evidencias cuantitativas, modelos econométricos y análisis de sensibilidad para la toma de decisiones financieras corporativas y de inversión.

---

## 📋 Contenido del Repositorio (Pizarrón del Examen)

El repositorio está estructurado en concordancia estricta con los 5 requerimientos de evaluación:

1. **[01. Práctica pandas (sexenios)](#1-práctica-pandas-sexenios):** Media, varianza muestral, desviación estándar, máximos, mínimos y rangos del Tipo de Cambio USD/MXN oficial FIX (Banco de México) para dos periodos presidenciales.
2. **[02. Práctica en R (sexenios)](#2-práctica-en-r-sexenios):** Mismo análisis estadístico del tipo de cambio implementado en lenguaje R nativo para ejecución directa en terminal Ubuntu.
3. **[03. Modelo de punto de equilibrio (Excel y Python)](#3-modelo-de-punto-de-equilibrio-excel-y-python):** Análisis de Costo-Volumen-Utilidad (CVU) para una Comercializadora de Camisas ($PV = \$40, CU = \$24, Com = \$2, CF = \$3,500$), determinando unidades ($Q_e = 250$), ingresos ($V_e = \$10,000$), estado de resultados y tabla de escenarios sin generación de imágenes.
4. **[04. Regresión lineal en Python (docstring)](#4-regresión-lineal-en-python-docstrings-completos):** Modelo de regresión lineal simple MCO para valuación inmobiliaria, documentado exhaustivamente bajo estándar PEP-257 y Google Docstrings, con cálculo de coeficientes, $R^2$, estadísticos t y predicción para 2,000 pies².
5. **[05. Regresión lineal múltiple R](#5-regresión-lineal-múltiple-r-y-validación-python):** Modelos econométricos multivariados de 2 variables ($Precio \sim Pies + Dormitorios$) y 3 variables ($Precio \sim Pies + Dormitorios + Antigüedad$) en script R y su contraparte de validación matricial analítica en Python.

---

## 🚀 Guía de Inicio Rápido en Terminal (Ubuntu / Linux)

### 1. Clonar el Repositorio
```bash
git clone https://github.com/carlosythekidkat/MetodosCuantitativos.git
cd MetodosCuantitativos
```

### 2. Configuración en Ubuntu / Debian (1 Clic)
Puedes configurar todas las dependencias del sistema y de Python automáticamente corriendo:
```bash
bash scripts/setup_ubuntu.sh
```

O hacerlo manualmente:
```bash
# Instalar paquetes base de Linux
sudo apt-get update
sudo apt-get install -y python3 python3-pip python3-venv r-base

# Crear y activar entorno virtual
python3 -m venv .venv
source .venv/bin/activate

# Instalar librerías de Python
pip install -r requirements.txt
```

---

## ⚡ Formas de Ejecución en Terminal

### Opción A: Ejecutar TODO de forma automatizada (Script Bash)
```bash
bash scripts/run_all.sh
```

### Opción B: Ejecutor Maestro en Python
```bash
# Correr todas las prácticas secuencialmente
python3 main.py --all

# O abrir el menú interactivo en terminal
python3 main.py
```

### Opción C: Ejecución individual por ejercicio
```bash
# Ejercicio 1 (Pandas)
python3 01_practica_pandas_sexenios/analisis_sexenios.py

# Ejercicio 2 (R)
Rscript 02_practica_r_sexenios/analisis_sexenios.R

# Ejercicio 3 (Punto de Equilibrio)
python3 03_punto_equilibrio_excel_python/punto_equilibrio.py

# Ejercicio 4 (Regresión Lineal Simple con docstrings)
python3 04_regresion_lineal_python/regresion_lineal.py

# Ejercicio 5 (Regresión Lineal Múltiple en R)
Rscript 05_regresion_lineal_multiple_r/regresion_multiple.R
# O contraparte en Python:
python3 05_regresion_lineal_multiple_r/regresion_multiple.py
```

---

## 📊 Resumen Ejecutivo de Resultados y Respuestas Oficiales

### 1. Práctica pandas (sexenios)
- **Serie Analizada:** Tipo de Cambio FIX Oficial USD/MXN (Banxico).
- **Sexenio 1:**
  - Media: **15.9935** MXN/USD
  - Varianza Muestral: **7.9288**
  - Desviación Estándar: **2.8158** MXN
  - Máximo: **21.9076** | Mínimo: **11.9807** | Rango: **9.9269**
- **Sexenio 2:**
  - Media: **19.5390** MXN/USD
  - Varianza Muestral: **2.5604**
  - Desviación Estándar: **1.6001** MXN
  - Máximo: **25.1185** | Mínimo: **16.3357** | Rango: **8.7828**
- **Conclusión Financiera:** El Sexenio 2 registró un nivel medio más elevado (+22.17%), pero el Sexenio 1 experimentó mayor volatilidad y dispersión cambiaria (+75.97% en varianza).

---

### 2. Práctica en R (sexenios)
- Implementación en **Base R** nativa para máxima portabilidad en servidores sin entorno de escritorio.
- Produce exactamente los mismos estadísticos descriptivos con consistencia a 4 decimales.

---

### 3. Modelo de punto de equilibrio (Excel y Python)
- **Parámetros:**
  - Precio de Venta ($PV$): **$40.00 USD**
  - Costo Unitario de Adquisición ($CU$): **$24.00 USD**
  - Comisión de Venta ($Com$): **$2.00 USD**
  - Costos Fijos Totales ($CF$): **$3,500.00 USD**
- **Fórmulas y Resultados:**
  - Costo Variable Unitario Total: $CV_u = 24 + 2 = \mathbf{\$26.00\text{ USD}}$
  - Margen de Contribución Unitario: $MCU = 40 - 26 = \mathbf{\$14.00\text{ USD}}$
  - Razón de Margen de Contribución: $RMC = \frac{14}{40} = \mathbf{35.00\%}$
  - **Punto de Equilibrio en Unidades ($Q_e$):** $\frac{3,500}{14} = \mathbf{250\text{ camisas}}$
  - **Punto de Equilibrio en Ingresos ($V_e$):** $250 \times 40 = \mathbf{\$10,000.00\text{ USD}}$
- **Estado de Resultados al Equilibrio:**
  - Ingresos ($250 \times \$40$): $\$10,000.00$
  - Costos Variables ($250 \times \$26$): $\$6,500.00$
  - Margen de Contribución: $\$3,500.00$
  - Costos Fijos: $\$3,500.00$
  - **Utilidad Operativa (EBIT): $0.00 USD**

---

### 4. Regresión lineal en Python (docstrings completos)
- **Ecuación Estimada (Pies Cuadrados):**
  $$\text{Precio} = 2,415.7416 + 46.5932 \times (\text{Pies Cuadrados})$$
  - Intersección ($b_0$): **$2,415.7416 USD**
  - Pendiente ($b_1$): **$46.5932 USD por pie²**
  - Coeficiente de Determinación ($R^2$): **0.6461 (64.61%)**
  - Correlación de Pearson ($r$): **0.8038**
  - Error Estándar Residual ($S_e$): **$22,046.73 USD**
- **Predicción para una propiedad de 2,000 pies²:**
  $$\hat{Y} = 2,415.7416 + 46.5932(2,000) = \mathbf{\$95,602.14\text{ USD}}$$

---

### 5. Regresión lineal múltiple R (y validación Python)

#### A. Modelo de 2 Variables Independientes:
$$\text{Precio} = 5,762.6218 + 48.5048 \times (\text{Pies}) - 2,550.0562 \times (\text{Dormitorios})$$
- $R^2$: **0.6469 (64.69%)** | $R^2$ Ajustado: **0.5964**
- **Predicción (2,000 pies², 3 dormitorios):** **$95,122.00 USD**

#### B. Modelo de 3 Variables Independientes (+ Antigüedad):
$$\text{Precio} = 82,192.5367 + 25.9561 \times (\text{Pies}) - 2,161.6873 \times (\text{Dorm}) - 1,710.3227 \times (\text{Antigüedad})$$
- $R^2$: **0.8864 (88.64%)** | $R^2$ Ajustado: **0.8602**
- **Predicción (2,000 pies², 3 dormitorios, 10 años):** **$110,516.46 USD**

---

## 📁 Estructura del Proyecto

```text
MetodosCuantitativos/
├── 01_practica_pandas_sexenios/
│   ├── analisis_sexenios.py          # Script con Pandas
│   ├── sexenio-1.csv
│   ├── sexenio-1.xls
│   ├── sexenio-2.csv
│   ├── sexenio-2.xls
│   └── README.md
├── 02_practica_r_sexenios/
│   ├── analisis_sexenios.R           # Script nativo en R
│   ├── sexenio-1.csv
│   ├── sexenio-1.xls
│   ├── sexenio-2.csv
│   ├── sexenio-2.xls
│   └── README.md
├── 03_punto_equilibrio_excel_python/
│   ├── punto_equilibrio.py           # Modelo OOP en Python (sin imágenes)
│   ├── punto_de_equilibrio.xlsx      # Hoja de cálculo con fórmulas financieras
│   └── README.md
├── 04_regresion_lineal_python/
│   ├── regresion_lineal.py           # Script con docstrings PEP-257
│   ├── Precio_de_Venta.csv
│   ├── Precio_de_Venta.xlsx
│   └── README.md
├── 05_regresion_lineal_multiple_r/
│   ├── regresion_multiple.R          # Script en R (2 y 3 variables)
│   ├── regresion_multiple.py         # Contraparte matricial en Python
│   ├── Precio_de_Venta.csv
│   ├── Precio_de_Venta.xlsx
│   └── README.md
├── data/                             # Conjuntos de datos compartidos
│   ├── sexenios/
│   ├── inmobiliario/
│   └── punto_equilibrio/
├── docs/                             # Documentación y desglose de ejercicios
│   └── GUIA_DESGLOSE_PASO_A_PASO_5_EJERCICIOS.docx
├── scripts/
│   ├── run_all.sh                    # Ejecutor integral para Ubuntu / Linux
│   └── setup_ubuntu.sh               # Instalador de dependencias en Ubuntu
├── .gitignore                        # Reglas de exclusión (incluye bloqueo de imágenes)
├── requirements.txt                  # Dependencias de Python
├── main.py                           # CLI interactivo y batch runner
├── MEMORY.md                         # Memoria persistente del repositorio
└── README.md                         # Manual y guía de despliegue oficial
```

---

## 🛠️ Comandos de Despliegue en GitHub

Para subir cambios o inicializar en un nuevo entorno:

```bash
git add .
git commit -m "feat: Evidencias de evaluacion de metodos cuantitativos para terminal ubuntu"
git branch -M main
git remote add origin https://github.com/carlosythekidkat/MetodosCuantitativos.git
git push -u origin main
```
