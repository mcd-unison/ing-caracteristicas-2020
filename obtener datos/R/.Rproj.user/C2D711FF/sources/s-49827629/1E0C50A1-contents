# Descargando y abriendo archivos


# 1. setwd() y getwd()
# 2. Archivos con dirección relativa y absoluta
getwd()
setwd("/Users/juliowaissman/Documents/cursos/Ingeniería de características/obtener datos/R")

# En R es por convención usar . como parte de los nombres
if (!dir.exists("../data/")){
  dir.create("../data")
}

# Descargar archivo (una sola vez)
archivo.url <- "https://data.baltimorecity.gov/api/views/dz54-2aru/rows.csv?accessType=DOWNLOAD"
archivo.nombre <- "../data/cameras.csv"
if(!file.exists(archivo.nombre)){
  download.file(archivo.url, destfile = archivo.nombre, method = "curl")  
  fecha.descarga <- date()
}

# Vamos a ver si lo pudimos bajar
df <- read.csv(archivo.nombre)


# Ahora vamos a ver como le hacemos con archivos excel

covid.url <- "http://datosabiertos.salud.gob.mx/gobmx/salud/datos_abiertos/datos_abiertos_covid19.zip"
covid.archivo <- "../data/datos_abiertos_covid19.zip"
covid.dic.conceptos.url <- "http://epidemiologia.salud.gob.mx/gobmx/salud/datos_abiertos/diccionario_datos_covid19.zip"
covid.dic.conceptos.archivo <- "../data/diccionario.zip"

# ¿No suena parecido? Hagamos una función
if(!file.exists(covid.archivo)){
  download.file(covid.url, destfile = covid.archivo)  
  unzip(covid.archivo, exdir = "../data/")
  download.file(covid.dic.conceptos.url, destfile = covid.dic.conceptos.archivo)  
  unzip(covid.dic.conceptos.archivo, exdir = "../data/")
  fecha.descarga <- date()
}


# Vamos a ver si lo podemos abrir bien
df.covid = read.csv("../data/200814COVID19MEXICO.csv")
df.covid.dic.con <- readxl::read_excel("../data/diccionario_datos_covid19/Descriptores_0419.xlsx")


