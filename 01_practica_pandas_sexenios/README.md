# Práctica 1: Análisis Estadístico de Sexenios con Pandas

## Descripción
En esta práctica se analizan las series históricas del **Tipo de Cambio FIX (USD/MXN)** publicadas por el Banco de México correspondientes a dos periodos sexenales presidenciales.

El objetivo cuantitativo es comparar la tendencia central y la dispersión (volatilidad) de la paridad cambiaria en cada sexenio mediante la biblioteca `pandas`.

---

## Métricas Calculadas
Para cada sexenio se calculan de forma exacta:
1. **Media Aritmética ($\bar{x}$):** Nivel promedio del tipo de cambio.
2. **Varianza Muestral ($s^2$):** Medida de variabilidad con $n-1$ grados de libertad (`ddof=1`).
3. **Desviación Estándar ($s$):** Dispersión respecto a la media (indicador clave de riesgo cambiario).
4. **Máximo:** Nivel pico alcanzado por el tipo de cambio.
5. **Mínimo:** Nivel más bajo cotizado en el periodo.
6. **Rango:** Amplitud total del movimiento cambiario ($Max - Min$).

---

## Resultados Obtenidos

| Métrica | Sexenio 1 | Sexenio 2 | Variación Absoluta | Variación % |
| :--- | :---: | :---: | :---: | :---: |
| **Media** | `15.9935` | `19.5390` | `+3.5455` | `+22.17%` |
| **Varianza** | `7.9288` | `2.5604` | `-5.3684` | `-67.71%` |
| **Desviación Estándar** | `2.8158` | `1.6001` | `-1.2157` | `-43.17%` |
| **Máximo** | `21.9076` | `25.1185` | `+3.2109` | `+14.66%` |
| **Mínimo** | `11.9807` | `16.3357` | `+4.3550` | `+36.35%` |
| **Rango** | `9.9269` | `8.7828` | `-1.1441` | `-11.53%` |

---

## Ejecución en Terminal (Ubuntu / Linux / Windows)

```bash
# Desde la raíz del repositorio
python3 01_practica_pandas_sexenios/analisis_sexenios.py

# O ingresando a la carpeta
cd 01_practica_pandas_sexenios
python3 analisis_sexenios.py
```
