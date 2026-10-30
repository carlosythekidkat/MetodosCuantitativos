# Práctica 3: Modelo de Punto de Equilibrio en Excel y Python

## Descripción
Modelado financiero del análisis de **Costo-Volumen-Utilidad (CVU)** para una comercializadora de camisas.

El repositorio incluye dos implementaciones integrales:
1. **Modelo en Python:** Implementación orientada a objetos (`punto_equilibrio.py`) para terminal CLI con simulación de escenarios sin dependencias gráficas.
2. **Modelo en Excel:** Archivo dinámico (`punto_de_equilibrio.xlsx`) con fórmulas matriciales, celdas vinculadas y tabla de estados de resultados.

---

## Formulación Matemática

1. **Costo Variable Unitario Total ($CV_u$):**
   $$CV_u = \text{Costo Adquisición} + \text{Comisión} = \$24 + \$2 = \$26\text{ USD}$$

2. **Margen de Contribución Unitario ($MCU$):**
   $$MCU = PV - CV_u = \$40 - \$26 = \$14\text{ USD}$$

3. **Razón de Margen de Contribución ($RMC$):**
   $$RMC = \frac{MCU}{PV} = \frac{14}{40} = 35\%$$

4. **Punto de Equilibrio en Unidades Físicas ($Q_e$):**
   $$Q_e = \frac{CF}{MCU} = \frac{\$3,500}{\$14} = 250\text{ camisas}$$

5. **Punto de Equilibrio en Ingresos Monetarios ($V_e$):**
   $$V_e = Q_e \times PV = 250 \times \$40 = \$10,000\text{ USD}$$

---

## Estado de Resultados en el Punto de Equilibrio ($Q = 250$)

```text
(+) Ingresos Totales (250 x $40.00):          $ 10,000.00 USD
(-) Costos Variables Totales (250 x $26.00):   $  6,500.00 USD
(=) Margen de Contribución Total:              $  3,500.00 USD
(-) Costos Fijos Totales:                      $  3,500.00 USD
(=) UTILIDAD OPERATIVA (EBIT):                 $      0.00 USD (Equilibrio Exacto)
```

---

## Archivos del Ejercicio
- `punto_equilibrio.py`: Script de ejecución en terminal.
- `punto_de_equilibrio.xlsx`: Hoja de cálculo con fórmulas financieras activas.

---

## Ejecución en Terminal

```bash
# Ejecutar modelo base
python3 03_punto_equilibrio_excel_python/punto_equilibrio.py

# Parámetros personalizados vía CLI:
python3 03_punto_equilibrio_excel_python/punto_equilibrio.py --precio 45 --costo 25 --comision 3 --costos-fijos 4000
```
