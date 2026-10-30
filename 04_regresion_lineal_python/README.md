# Práctica 4: Regresión Lineal Simple en Python (con Docstrings)

## Descripción
Implementación en Python puro de un modelo econométrico de **Regresión Lineal Simple** por Mínimos Cuadrados Ordinarios (MCO / OLS) enfocado en la valuación de activos inmobiliarios.

El código fuente (`regresion_lineal.py`) cumple rigurosamente con los estándares de documentación **PEP-257** y **Google Python Style Guide**, integrando docstrings completos en módulos, clases y métodos, con tipado estático `typing`.

---

## Formulación Matemática de MCO

Para el modelo $Y_i = \beta_0 + \beta_1 X_i + \varepsilon_i$:

1. **Pendiente ($\beta_1$):**
   $$b_1 = \frac{n \sum XY - \sum X \sum Y}{n \sum X^2 - (\sum X)^2}$$

2. **Intersección ($\beta_0$):**
   $$b_0 = \bar{Y} - b_1 \bar{X} = \frac{\sum Y - b_1 \sum X}{n}$$

3. **Coeficiente de Correlación de Pearson ($r$):**
   $$r = \frac{n \sum XY - \sum X \sum Y}{\sqrt{[n \sum X^2 - (\sum X)^2][n \sum Y^2 - (\sum Y)^2]}}$$

4. **Coeficiente de Determinación ($R^2$):**
   $$R^2 = r^2 = 1 - \frac{SS_{res}}{SS_{tot}}$$

---

## Modelos Estimados

| Variable Predictora ($X$) | Ecuación de Regresión Estimada | $R^2$ | Correlación ($r$) | Error Estándar ($S_e$) |
| :--- | :--- | :---: | :---: | :---: |
| **Pies Cuadrados** | $\text{Precio} = 2,415.7416 + 46.5932 \times (\text{Pies})$ | `0.6461` | `+0.8038` | $\$22,046.73$ |
| **Dormitorios** | $\text{Precio} = 1,984.6939 + 36,127.5510 \times (\text{Dorm})$ | `0.3652` | `+0.6043` | $\$29,528.71$ |
| **Antigüedad** | $\text{Precio} = 147,686.8796 - 2,423.1765 \times (\text{Antig})$ | `0.7769` | `-0.8814` | $\$17,507.09$ |

### Predicción para Casa de 2,000 Pies Cuadrados
$$\hat{Y} = 2,415.7416 + 46.5932 \times (2,000) = \mathbf{\$95,602.14\text{ USD}}$$

---

## Ejecución en Terminal

```bash
python3 04_regresion_lineal_python/regresion_lineal.py
```
