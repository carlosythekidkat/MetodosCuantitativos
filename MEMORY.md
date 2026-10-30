# MEMORIA DEL PROYECTO: METODOS CUANTITATIVOS APLICADOS A LAS FINANZAS

## 1. Identificación del Repositorio
- **Nombre:** MetodosCuantitativos
- **URL Remota Oficial:** `https://github.com/carlosythekidkat/MetodosCuantitativos.git`
- **Ámbito:** Examen y Evidencias de Evaluación en Métodos Cuantitativos Aplicados a las Finanzas para la Toma de Decisiones.
- **Entorno Objetivo:** Ubuntu / Linux Terminal (con soporte multiplataforma Windows/macOS).

---

## 2. Mapa de Prácticas y Evidencias Requeridas (Pizarrón del Examen)

| # | Título en Pizarrón | Directorio en Repo | Lenguaje Principal | Archivos Principales | Salidas Clave |
| :---: | :--- | :--- | :---: | :--- | :--- |
| **1** | Práctica pandas (sexenios) | `01_practica_pandas_sexenios/` | Python / Pandas | `analisis_sexenios.py`<br>`sexenio-1.csv`, `sexenio-2.csv` | Sexenio 1: $\mu = 15.9935$, $\sigma^2 = 7.9288$, $\sigma = 2.8158$<br>Sexenio 2: $\mu = 19.5390$, $\sigma^2 = 2.5604$, $\sigma = 1.6001$ |
| **2** | Práctica en R (sexenios) | `02_practica_r_sexenios/` | R (Base R) | `analisis_sexenios.R`<br>`sexenio-1.csv`, `sexenio-2.csv` | Idénticas a Práctica 1 calculadas en R nativo sin dependencias externas. |
| **3** | Modelo de punto equilibrio Excel y python | `03_punto_equilibrio_excel_python/` | Python / Excel | `punto_equilibrio.py`<br>`punto_de_equilibrio.xlsx` | $PV=\$40, CV_u=\$26, MCU=\$14, CF=\$3,500$<br>$Q_e = 250$ unidades, $V_e = \$10,000$ USD.<br>Utilidad operativa EBIT = $\$0.00$. |
| **4** | Regresión lineal en python (docstring) | `04_regresion_lineal_python/` | Python (PEP-257) | `regresion_lineal.py`<br>`Precio_de_Venta.csv` | Docstrings completos y tipado estático.<br>Precio vs Pies: $Y = 2415.7416 + 46.5932(Pies)$ ($R^2=0.6461$)<br>Predicción 2,000 pies: $\$95,602.14$ USD. |
| **5** | Regresión lineal múltiple R | `05_regresion_lineal_multiple_r/` | R (y Python) | `regresion_multiple.R`<br>`regresion_multiple.py` | 2 Variables: $Precio = 5762.6218 + 48.5048(Pies) - 2550.0562(Dorm)$ ($R^2=0.6469$)<br>Pred. (2000 pies, 3 dorm) = $\$95,122.00$ USD.<br>3 Variables: $Precio = 82192.5367 + 25.9561(Pies) - 2161.6873(Dorm) - 1710.3227(Antig)$ ($R^2=0.8864$)<br>Pred. (2000 pies, 3 dorm, 10 años) = $\$110,516.46$ USD. |

---

## 3. Decisiones de Ingeniería Implementadas
1. **Restricción Estricta de No Imágenes:** Se desactivó cualquier generación o guardado automático de archivos de imagen (`.png`, `.jpg`), configurando `.gitignore` para bloquearlas y ejecutando todas las salidas directamente en texto por terminal CLI.
2. **Independencia en Ubuntu Mínimo:** Los scripts en R utilizan `read.csv()` nativo y los de Python utilizan módulos estándar con fallback transparente a Pandas/NumPy, garantizando que un evaluador en Ubuntu pueda correr las 5 prácticas inmediatamente.
3. **Ejecutor Centralizado:** Se desarrollaron `main.py` y `scripts/run_all.sh` para correr todo el proyecto en 1 solo comando.
4. **Documentación Completa:** Se preservó el documento maestro `GUIA_DESGLOSE_PASO_A_PASO_5_EJERCICIOS.docx` en `docs/` y se generaron READMEs específicos en cada subcarpeta más un `README.md` principal.
