# Práctica 5: Regresión Lineal Múltiple en R

## Descripción
Modelado econométrico multivariado aplicado a la valuación y predicción del **Precio de Venta Inmobiliario** mediante el software estadístico **R** (`lm()`).

Se estiman dos especificaciones econométricas para contrastar el poder explicativo y la significancia estadística:
1. **Modelo A (2 variables):** $\text{Precio} = f(\text{Pies Cuadrados}, \text{Dormitorios})$
2. **Modelo B (3 variables):** $\text{Precio} = f(\text{Pies Cuadrados}, \text{Dormitorios}, \text{Antigüedad})$

---

## Comparativa de Modelos Econométricos

| Métrica / Parámetro | Modelo A (2 Variables) | Modelo B (3 Variables) |
| :--- | :---: | :---: |
| **Intercepto ($\beta_0$)** | `$5,762.6218$` | `$82,192.5367$` |
| **Coef. Pies Cuadrados ($\beta_1$)** | `+$48.5048` | `+$25.9561` |
| **Coef. Dormitorios ($\beta_2$)** | `-$2,550.0562` | `-$2,161.6873` |
| **Coef. Antigüedad ($\beta_3$)** | *No incluido* | `-$1,710.3227` |
| **$R^2$ (Varianza explicada)** | `64.69%` | `88.64%` |
| **$R^2$ Ajustado** | `59.64%` | `86.02%` |
| **Error Estándar ($S_e$)** | `$22,796.93 USD` | `$13,417.06 USD` |

---

## Predicciones Clave del Examen

### 1. Propiedad de 2,000 pies² y 3 dormitorios (Modelo A)
$$\hat{Y} = 5,762.6218 + 48.5048 \times (2,000) - 2,550.0562 \times (3) = \mathbf{\$95,122.00\text{ USD}}$$

### 2. Propiedad de 2,000 pies², 3 dormitorios y 10 años (Modelo B)
$$\hat{Y} = 82,192.5367 + 25.9561(2,000) - 2,161.6873(3) - 1,710.3227(10) = \mathbf{\$110,516.46\text{ USD}}$$

---

## Ejecución en Terminal Ubuntu / Linux

```bash
# Ejecutar script en R
Rscript 05_regresion_lineal_multiple_r/regresion_multiple.R

# Ejecutar contraparte de validación en Python
python3 05_regresion_lineal_multiple_r/regresion_multiple.py
```
