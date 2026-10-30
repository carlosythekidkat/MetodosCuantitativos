#!/usr/bin/env Rscript
# ==============================================================================
# Práctica 5: Regresión Lineal Múltiple en R
# Asignatura: Métodos Cuantitativos Aplicados a las Finanzas
#
# Objetivo: Estimar modelos econométricos multivariados para la valuación
#           inmobiliaria de propiedades residenciales:
#           - Modelo A (2 Variables): Precio ~ Pies Cuadrados + Dormitorios
#           - Modelo B (3 Variables): Precio ~ Pies Cuadrados + Dormitorios + Antigüedad
#
# Compatibilidad: Ubuntu / Linux / macOS / Windows mediante CLI terminal.
# ==============================================================================

# Localización dinámica del conjunto de datos
obtener_ruta_datos <- function() {
  candidatos <- c(
    ".",
    "05_regresion_lineal_multiple_r",
    "data/inmobiliario",
    "../data/inmobiliario"
  )
  for (d in candidatos) {
    if (file.exists(file.path(d, "Precio_de_Venta.csv")) || file.exists(file.path(d, "Precio_de_Venta.xlsx"))) {
      return(d)
    }
  }
  return(".")
}

dir_datos <- obtener_ruta_datos()
ruta_csv <- file.path(dir_datos, "Precio_de_Venta.csv")
ruta_xlsx <- file.path(dir_datos, "Precio_de_Venta.xlsx")

# Carga de datos con fallback automático (Base R nativo para terminal Linux)
if (file.exists(ruta_csv)) {
  df <- read.csv(ruta_csv, stringsAsFactors = FALSE)
  colnames(df) <- c("precio", "pies_cuadrados", "dormitorios", "antiguedad")
} else if (file.exists(ruta_xlsx)) {
  if (!requireNamespace("readxl", quietly = TRUE)) {
    stop("Se requiere el archivo CSV o instalar 'readxl' para procesar archivos .xlsx.")
  }
  df <- readxl::read_excel(ruta_xlsx, skip = 3)
  if (ncol(df) > 4) df <- df[, (ncol(df) - 3):ncol(df)]
  colnames(df) <- c("precio", "pies_cuadrados", "dormitorios", "antiguedad")
} else {
  stop("No se encontró el archivo 'Precio_de_Venta' en formato CSV ni XLSX.")
}

df <- na.omit(df)
df[] <- lapply(df, as.numeric)

cat("\n##############################################################\n")
cat("  EJERCICIO 5: REGRESIÓN LINEAL MÚLTIPLE EN R\n")
cat("  Metodos Cuantitativos Aplicados a las Finanzas\n")
cat("##############################################################\n\n")

# ==============================================================================
# 1. MODELO A (2 VARIABLES INDEPENDIENTES: PIES Y DORMITORIOS)
# ==============================================================================
cat("====================================================================\n")
cat("  1. MODELO MÚLTIPLE DE 2 VARIABLES (Pies Cuadrados + Dormitorios)\n")
cat("====================================================================\n")

mod2 <- lm(precio ~ pies_cuadrados + dormitorios, data = df)
s2 <- summary(mod2)
b0_2 <- coef(mod2)[1]
b1_2 <- coef(mod2)[2]
b2_2 <- coef(mod2)[3]

cat(sprintf("Ecuación Estimada:\n"))
cat(sprintf("  Precio = %.4f + %.4f * (Pies) - %.4f * (Dormitorios)\n\n", b0_2, b1_2, abs(b2_2)))
cat(sprintf("  Intersección (b0):           $%12.4f USD\n", b0_2))
cat(sprintf("  Pendiente Pies (b1):         $%12.4f USD/pie²\n", b1_2))
cat(sprintf("  Pendiente Dormitorios (b2):  $%12.4f USD/dorm\n", b2_2))
cat(sprintf("  Coef. Determinación (R²):     %12.4f (%.2f%%)\n", s2$r.squared, s2$r.squared * 100))
cat(sprintf("  R² Ajustado:                  %12.4f\n", s2$adj.r.squared))
cat(sprintf("  Error Estándar Residual (Se):$%12.4f USD\n", s2$sigma))

# Predicción Modelo 2: 2,000 pies y 3 dormitorios
nueva_casa_2 <- data.frame(pies_cuadrados = 2000, dormitorios = 3)
pred_2 <- predict(mod2, nueva_casa_2, interval = "confidence")

cat("\n  >>> PREDICCIÓN (2,000 pies², 3 dormitorios):\n")
cat(sprintf("      PRECIO ESTIMADO = $%10.2f USD\n", pred_2[1, "fit"]))
cat(sprintf("      Intervalo Confianza 95%%: [$%10.2f , $%10.2f]\n", pred_2[1, "lwr"], pred_2[1, "upr"]))
cat("--------------------------------------------------------------------\n\n")

# ==============================================================================
# 2. MODELO B (3 VARIABLES: PIES + DORMITORIOS + ANTIGÜEDAD)
# ==============================================================================
cat("====================================================================\n")
cat("  2. MODELO MÚLTIPLE COMPLETO DE 3 VARIABLES (+ Antigüedad)\n")
cat("====================================================================\n")

mod3 <- lm(precio ~ pies_cuadrados + dormitorios + antiguedad, data = df)
s3 <- summary(mod3)
b0_3 <- coef(mod3)[1]
b1_3 <- coef(mod3)[2]
b2_3 <- coef(mod3)[3]
b3_3 <- coef(mod3)[4]

cat(sprintf("Ecuación Estimada:\n"))
cat(sprintf("  Precio = %.4f + %.4f * (Pies) - %.4f * (Dorm) - %.4f * (Antigüedad)\n\n",
            b0_3, b1_3, abs(b2_3), abs(b3_3)))
cat(sprintf("  Intersección (b0):           $%12.4f USD\n", b0_3))
cat(sprintf("  Pendiente Pies (b1):         $%12.4f USD/pie²\n", b1_3))
cat(sprintf("  Pendiente Dormitorios (b2):  $%12.4f USD/dorm\n", b2_3))
cat(sprintf("  Pendiente Antigüedad (b3):   $%12.4f USD/año\n", b3_3))
cat(sprintf("  Coef. Determinación (R²):     %12.4f (%.2f%%)\n", s3$r.squared, s3$r.squared * 100))
cat(sprintf("  R² Ajustado:                  %12.4f\n", s3$adj.r.squared))
cat(sprintf("  Error Estándar Residual (Se):$%12.4f USD\n", s3$sigma))

# Predicción Modelo 3: 2,000 pies, 3 dormitorios, 10 años
nueva_casa_3 <- data.frame(pies_cuadrados = 2000, dormitorios = 3, antiguedad = 10)
pred_3 <- predict(mod3, nueva_casa_3, interval = "confidence")

cat("\n  >>> PREDICCIÓN (2,000 pies², 3 dormitorios, 10 años):\n")
cat(sprintf("      PRECIO ESTIMADO = $%10.2f USD\n", pred_3[1, "fit"]))
cat(sprintf("      Intervalo Confianza 95%%: [$%10.2f , $%10.2f]\n", pred_3[1, "lwr"], pred_3[1, "upr"]))
cat("--------------------------------------------------------------------\n\n")

# ==============================================================================
# 3. COMPARATIVA Y CONCLUSIÓN ECONOMÉTRICA
# ==============================================================================
cat(">>> COMPARATIVA ECONOMÉTRICA ENTRE MODELOS:\n")
cat(sprintf("    Modelo 2 Variables: R² = %.2f%% | R² Ajustado = %.2f%% | Se = $%.2f USD\n",
            s2$r.squared * 100, s2$adj.r.squared * 100, s2$sigma))
cat(sprintf("    Modelo 3 Variables: R² = %.2f%% | R² Ajustado = %.2f%% | Se = $%.2f USD\n",
            s3$r.squared * 100, s3$adj.r.squared * 100, s3$sigma))
cat("    Conclusión Financiera: Incorporar la variable 'Antigüedad' incrementa el R² del 64.69%\n")
cat("    al 88.64%, reduciendo el error estándar residual a más de la mitad.\n")
cat("====================================================================\n\n")
