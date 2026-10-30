# Práctica 2: Análisis Estadístico de Sexenios en R

## Descripción
Script en lenguaje estadístico **R** diseñado específicamente para ejecutarse en terminal (Ubuntu / Linux / macOS / Windows) sin interfaz gráfica obligatoria.

Calcula los momentos estadísticos de primer y segundo orden para la serie FIX del Tipo de Cambio USD/MXN en ambos periodos presidenciales utilizando funciones nativas optimizadas de base R (`mean`, `var`, `sd`, `max`, `min`).

---

## Métricas del Modelo en R

- **Media Muestral:** $\bar{x} = \frac{1}{n} \sum_{i=1}^n x_i$
- **Varianza Muestral:** $s^2 = \frac{1}{n-1} \sum_{i=1}^n (x_i - \bar{x})^2$
- **Desviación Estándar:** $s = \sqrt{s^2}$
- **Rango:** $R = x_{max} - x_{min}$

---

## Resultados Obtenidos

```text
============================================================
        RESULTADOS: SEXENIO 1 (N = 1759 observaciones)
============================================================
  MEDIA:                    15.9935 MXN/USD
  VARIANZA:                  7.9288
  DESVIACION ESTANDAR:       2.8158 MXN
  MAXIMO:                   21.9076 MXN/USD
  MINIMO:                   11.9807 MXN/USD
  RANGO:                     9.9269 MXN
============================================================

============================================================
        RESULTADOS: SEXENIO 2 (N = 1510 observaciones)
============================================================
  MEDIA:                    19.5390 MXN/USD
  VARIANZA:                  2.5604
  DESVIACION ESTANDAR:       1.6001 MXN
  MAXIMO:                   25.1185 MXN/USD
  MINIMO:                   16.3357 MXN/USD
  RANGO:                     8.7828 MXN
============================================================
```

---

## Ejecución en Terminal Ubuntu / Linux

```bash
# 1. Si no tienes R instalado en Ubuntu:
sudo apt-get update && sudo apt-get install -y r-base

# 2. Ejecutar directamente con Rscript:
Rscript 02_practica_r_sexenios/analisis_sexenios.R

# O entrando al directorio:
cd 02_practica_r_sexenios
Rscript analisis_sexenios.R
```
