#!/usr/bin/env Rscript
# ==============================================================================
# Práctica 2: Análisis Estadístico de Sexenios en R
# Asignatura: Métodos Cuantitativos Aplicados a las Finanzas
#
# Objetivo: Calcular las 6 métricas exactas del Tipo de Cambio USD/MXN
#           (FIX - Banco de México) para cada Sexenio Presidencial.
#
# Compatibilidad: Ubuntu / Linux / macOS / Windows mediante CLI terminal.
# ==============================================================================

# Función para localizar el directorio de trabajo dinámicamente
obtener_ruta_datos <- function() {
  posibles_rutas <- c(
    ".",
    "02_practica_r_sexenios",
    "data/sexenios",
    "../data/sexenios"
  )
  for (r in posibles_rutas) {
    if (file.exists(file.path(r, "sexenio-1.csv")) || file.exists(file.path(r, "sexenio-1.xls"))) {
      return(r)
    }
  }
  return(".")
}

# Cargar serie de datos (Usa base R con CSV para no requerir dependencias externas)
cargar_serie_sexenio <- function(dir_datos, nombre_base) {
  ruta_csv <- file.path(dir_datos, paste0(nombre_base, ".csv"))
  ruta_xls <- file.path(dir_datos, paste0(nombre_base, ".xls"))

  if (file.exists(ruta_csv)) {
    # Base R nativo sin dependencias
    datos <- read.csv(ruta_csv, stringsAsFactors = FALSE)
    if ("Determinacion" %in% colnames(datos)) {
      serie <- suppressWarnings(as.numeric(datos$Determinacion))
    } else {
      serie <- suppressWarnings(as.numeric(datos[[2]]))
    }
    return(na.omit(serie))
  }

  if (file.exists(ruta_xls)) {
    if (!requireNamespace("readxl", quietly = TRUE)) {
      stop("Se requiere el archivo CSV o el paquete 'readxl' instalado para leer archivos .xls.")
    }
    df <- readxl::read_excel(ruta_xls, skip = 6, na = c("", "NA", "N/E"))
    serie <- suppressWarnings(as.numeric(df[[2]]))
    return(na.omit(serie))
  }

  stop(paste("No se encontró el archivo de datos para:", nombre_base))
}

# Función para imprimir el reporte exacto solicitado
imprimir_metricas <- function(serie, titulo) {
  datos <- na.omit(as.numeric(serie))
  n <- length(datos)
  media <- mean(datos)
  varianza <- var(datos)
  desv_std <- sd(datos)
  maximo <- max(datos)
  minimo <- min(datos)
  rango <- maximo - minimo

  cat("\n============================================================\n")
  cat(sprintf("        %s (N = %d observaciones)\n", titulo, n))
  cat("============================================================\n")
  cat(sprintf("  MEDIA:               %12.4f MXN/USD\n", media))
  cat(sprintf("  VARIANZA:            %12.4f\n", varianza))
  cat(sprintf("  DESVIACION ESTANDAR: %12.4f MXN\n", desv_std))
  cat(sprintf("  MAXIMO:              %12.4f MXN/USD\n", maximo))
  cat(sprintf("  MINIMO:              %12.4f MXN/USD\n", minimo))
  cat(sprintf("  RANGO:               %12.4f MXN\n", rango))
  cat("============================================================\n")

  return(list(
    media = media,
    varianza = varianza,
    desv_std = desv_std,
    maximo = maximo,
    minimo = minimo,
    rango = rango
  ))
}

# ------------------------------------------------------------------------------
# Ejecución Principal
# ------------------------------------------------------------------------------
cat("\n##############################################################\n")
cat("  EJERCICIO 2: ANALISIS ESTADISTICO EN R (SEXENIOS)\n")
cat("  Metodos Cuantitativos Aplicados a las Finanzas\n")
cat("##############################################################\n")

dir_datos <- obtener_ruta_datos()

serie1 <- cargar_serie_sexenio(dir_datos, "sexenio-1")
m1 <- imprimir_metricas(serie1, "RESULTADOS: SEXENIO 1")

serie2 <- cargar_serie_sexenio(dir_datos, "sexenio-2")
m2 <- imprimir_metricas(serie2, "RESULTADOS: SEXENIO 2")

# Comparativa financiera
dif_media <- m2$media - m1$media
pct_cambio <- (dif_media / m1$media) * 100

cat("\n>>> COMPARATIVA FINANCIERA (R):\n")
cat(sprintf("    Variación Media: +$%.4f MXN (+%.2f%%)\n", dif_media, pct_cambio))
cat(sprintf("    Volatilidad (sd): Sexenio 1 = %.4f vs Sexenio 2 = %.4f\n", m1$desv_std, m2$desv_std))
cat("--------------------------------------------------------------\n\n")
