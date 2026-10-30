# -*- coding: utf-8 -*-
"""Práctica 3: Modelo Financiero de Punto de Equilibrio (Break-Even Analysis).

Asignatura: Métodos Cuantitativos Aplicados a las Finanzas
Objetivo:
    Modelar cuantitativamente el Punto de Equilibrio Operativo (EBIT = 0)
    para una Comercializadora de Camisas, determinando:
    1. Costo Variable Unitario Total (CVu)
    2. Margen de Contribución Unitario (MCU)
    3. Razón de Margen de Contribución (RMC)
    4. Punto de Equilibrio en Unidades Físicas (Qe)
    5. Punto de Equilibrio en Unidades Monetarias (Ve)
    6. Estado de Resultados en el punto de equilibrio
    7. Tabla de Sensibilidad Operativa bajo diferentes escenarios de ventas

Compatibilidad: Ejecución nativa por terminal CLI (Ubuntu / Linux / Windows / macOS).
No requiere librerías gráficas para operar.
"""

import sys
import argparse
from typing import Dict, List

# Asegurar codificación UTF-8 en consola
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


class PuntoEquilibrio:
    """Modelo matemático financiero de análisis de Costo-Volumen-Utilidad (CVU).

    Attributes:
        precio_venta (float): Precio de venta unitario ($ PV).
        costo_unitario (float): Costo de adquisición o compra por unidad ($ CU).
        comision_venta (float): Comisión o gasto variable por venta unitaria ($ Com).
        costos_fijos (float): Total de costos y gastos fijos del periodo ($ CF).
    """

    def __init__(
        self,
        precio_venta: float = 40.0,
        costo_unitario: float = 24.0,
        comision_venta: float = 2.0,
        costos_fijos: float = 3500.0,
    ) -> None:
        """Inicializa los parámetros del modelo de punto de equilibrio.

        Args:
            precio_venta: Precio de venta por unidad en USD.
            costo_unitario: Costo directo de compra por unidad en USD.
            comision_venta: Comisión variable pagada al vendedor por unidad en USD.
            costos_fijos: Costos fijos operativos del mes en USD.

        Raises:
            ValueError: Si el precio de venta es menor o igual al costo variable unitario.
        """
        self.precio_venta = float(precio_venta)
        self.costo_unitario = float(costo_unitario)
        self.comision_venta = float(comision_venta)
        self.costos_fijos = float(costos_fijos)

        if self.precio_venta <= self.costo_variable_unitario:
            raise ValueError(
                f"Error Financiero: El precio de venta (${self.precio_venta:.2f}) "
                f"debe superar al costo variable total (${self.costo_variable_unitario:.2f}) "
                "para tener un margen de contribución positivo."
            )

    @property
    def costo_variable_unitario(self) -> float:
        """Costo variable unitario total: CVu = Costo Adquisición + Comisión."""
        return self.costo_unitario + self.comision_venta

    @property
    def margen_contribucion_unitario(self) -> float:
        """Margen de contribución unitario: MCU = PV - CVu."""
        return self.precio_venta - self.costo_variable_unitario

    @property
    def razon_margen_contribucion(self) -> float:
        """Razón o porcentaje de margen de contribución: RMC = MCU / PV."""
        return self.margen_contribucion_unitario / self.precio_venta

    @property
    def punto_equilibrio_unidades(self) -> float:
        """Volumen de equilibrio en unidades: Qe = CF / MCU."""
        return self.costos_fijos / self.margen_contribucion_unitario

    @property
    def punto_equilibrio_ingresos(self) -> float:
        """Ventas de equilibrio en ingresos monetarios: Ve = Qe * PV = CF / RMC."""
        return self.punto_equilibrio_unidades * self.precio_venta

    def calcular_estado_resultados(self, unidades: float) -> Dict[str, float]:
        """Calcula el estado de resultados financiero para un nivel de unidades dado.

        Args:
            unidades: Número de camisas vendidas en el periodo.

        Returns:
            Dict[str, float]: Desglose de ingresos, costos variables, margen de
            contribución, costos fijos y utilidad/pérdida neta de operación.
        """
        ingresos = unidades * self.precio_venta
        costos_variables = unidades * self.costo_variable_unitario
        margen_total = ingresos - costos_variables
        utilidad_operativa = margen_total - self.costos_fijos

        return {
            "unidades": unidades,
            "ingresos": ingresos,
            "costos_variables": costos_variables,
            "margen_total": margen_total,
            "costos_fijos": self.costos_fijos,
            "costos_totales": costos_variables + self.costos_fijos,
            "utilidad_operativa": utilidad_operativa,
        }

    def generar_reporte_detallado(self) -> str:
        """Genera un reporte ejecutivo en formato texto estructurado para consola."""
        qe = self.punto_equilibrio_unidades
        ve = self.punto_equilibrio_ingresos
        mcu = self.margen_contribucion_unitario
        cvu = self.costo_variable_unitario
        rmc_pct = self.razon_margen_contribucion * 100
        estado_eq = self.calcular_estado_resultados(qe)

        sep = "=" * 72
        sub_sep = "-" * 72

        lineas = [
            sep,
            "        ANÁLISIS DE PUNTO DE EQUILIBRIO FINANCIERO (BREAK-EVEN)",
            "               COMERCIALIZADORA DE CAMISAS S.A.",
            sep,
            "1. PARÁMETROS BASE DEL MODELO:",
            f"   • Precio de Venta Unitario (PV):           ${self.precio_venta:>10.2f} USD",
            f"   • Costo de Adquisición Unitario:           ${self.costo_unitario:>10.2f} USD",
            f"   • Comisión de Ventas por Camisa:           ${self.comision_venta:>10.2f} USD",
            f"   • Costos Fijos Totales del Periodo (CF):   ${self.costos_fijos:>10.2f} USD",
            sub_sep,
            "2. ESTRUCTURA DE MÁRGENES OPERATIVOS:",
            f"   • Costo Variable Unitario Total (CVu):     ${cvu:>10.2f} USD  ($24 + $2)",
            f"   • Margen de Contribución Unitario (MCU):   ${mcu:>10.2f} USD  ($40 - $26)",
            f"   • Razón de Margen de Contribución (RMC):    {rmc_pct:>10.2f} %   ($14 / $40)",
            sub_sep,
            "3. RESULTADOS CLAVE DEL PUNTO DE EQUILIBRIO:",
            f"   >>> PUNTO DE EQUILIBRIO EN UNIDADES (Qe):   {qe:>10.0f} camisas <<<",
            f"   >>> PUNTO DE EQUILIBRIO EN INGRESOS (Ve):  ${ve:>10.2f} USD <<<",
            "",
            "   Interpretación Financiera:",
            f"   La empresa necesita comercializar exactamente {qe:.0f} camisas al mes,",
            f"   generando una facturación mínima de ${ve:,.2f} USD, para cubrir la totalidad",
            "   de sus obligaciones fijas y costos variables sin incurrir en pérdidas.",
            sub_sep,
            f"4. ESTADO DE RESULTADOS AL PUNTO DE EQUILIBRIO (Q = {qe:.0f} unidades):",
            f"   (+) Ingresos Totales por Ventas:          ${estado_eq['ingresos']:>10.2f} USD",
            f"   (-) Costos Variables Totales:             ${estado_eq['costos_variables']:>10.2f} USD",
            f"   (=) Margen de Contribución Total:         ${estado_eq['margen_total']:>10.2f} USD",
            f"   (-) Costos Fijos Totales:                 ${estado_eq['costos_fijos']:>10.2f} USD",
            f"   (=) UTILIDAD OPERATIVA (EBIT):            ${estado_eq['utilidad_operativa']:>10.2f} USD (Equilibrio Exacto)",
            sep,
        ]
        return "\n".join(lineas)

    def generar_tabla_simulacion(self, escenarios: List[int] = None) -> str:
        """Genera una tabla de sensibilidad de utilidad/pérdida ante distintos volúmenes."""
        if escenarios is None:
            escenarios = [0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500]

        encabezado = (
            "-------------------------------------------------------------------------------------------------\n"
            " Unidades |   Ingresos   | Costos Var.  | Costos Fijos | Costos Tot.  | Utilidad/Pérdida | Estado\n"
            "-------------------------------------------------------------------------------------------------"
        )
        filas = [encabezado]
        for q in escenarios:
            res = self.calcular_estado_resultados(q)
            u = res["utilidad_operativa"]
            if u < 0:
                estado = "Zona de Pérdida"
            elif u == 0:
                estado = "<-- EQUILIBRIO EXACTO"
            else:
                estado = "Zona de Ganancia"

            fila = (
                f"  {q:>6d}  | "
                f"${res['ingresos']:>10.2f} | "
                f"${res['costos_variables']:>10.2f} | "
                f"${res['costos_fijos']:>10.2f} | "
                f"${res['costos_totales']:>10.2f} | "
                f"${u:>14.2f} | {estado}"
            )
            filas.append(fila)

        filas.append(
            "-------------------------------------------------------------------------------------------------"
        )
        return "\n".join(filas)


def main() -> None:
    """Ejecución del script desde consola con soporte para argumentos."""
    parser = argparse.ArgumentParser(
        description="Modelo Financiero de Punto de Equilibrio (Terminal CLI)"
    )
    parser.add_argument("--precio", type=float, default=40.0, help="Precio de venta unitario")
    parser.add_argument("--costo", type=float, default=24.0, help="Costo unitario de adquisición")
    parser.add_argument("--comision", type=float, default=2.0, help="Comisión por venta unitaria")
    parser.add_argument("--costos-fijos", type=float, default=3500.0, help="Costos fijos mensuales")
    parser.add_argument(
        "-i", "--interactivo", action="store_true", help="Ingreso manual interactivo"
    )

    args = parser.parse_args()

    if args.interactivo:
        print("\n--- INGRESO MANUAL DE PARÁMETROS FINANCIEROS ---")
        try:
            pv = float(input("Precio de venta ($ USD) [40.0]: ") or 40.0)
            cu = float(input("Costo adquisición ($ USD) [24.0]: ") or 24.0)
            com = float(input("Comisión unitaria ($ USD) [2.0]: ") or 2.0)
            cf = float(input("Costos fijos totales ($ USD) [3500.0]: ") or 3500.0)
        except ValueError:
            print("Error: Todos los datos deben ser numéricos.")
            sys.exit(1)
    else:
        pv = args.precio
        cu = args.costo
        com = args.comision
        cf = args.costos_fijos

    modelo = PuntoEquilibrio(
        precio_venta=pv,
        costo_unitario=cu,
        comision_venta=com,
        costos_fijos=cf,
    )

    print("\n" + "#" * 72)
    print("  EJERCICIO 3: MODELO DE PUNTO DE EQUILIBRIO EN PYTHON Y EXCEL")
    print("  Metodos Cuantitativos Aplicados a las Finanzas")
    print("#" * 72)

    print(modelo.generar_reporte_detallado())
    print("\n5. ANÁLISIS DE SENSIBILIDAD OPERATIVA (TABLA DE VOLÚMENES):")
    print(modelo.generar_tabla_simulacion())
    print()


if __name__ == "__main__":
    main()
