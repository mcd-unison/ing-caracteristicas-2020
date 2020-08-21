#%% Carga archivos desde internet (muchas formas de hacerlo)

import os  # Para manejo de archivos y directorios
import urllib # Una forma estandard de descargar datos
import requests # Otra forma no de las librerías de uso comun

import datetime # Fecha de descarga
import pandas as pd # Solo para ver el archivo descargado
import zipfile # Descompresión de archivos

# pwd
print(os.getcwd())

#%% Carga datos de internet

# Verifica un directorio
if not os.path.exists("../data/"):
    os.mkdir("../data/")

# Selecciona dirección y nombre de archivo a guardar
archivo_url = "https://data.baltimorecity.gov/api/views/dz54-2aru/rows.csv?accessType=DOWNLOAD"
archivo_nombre = "../data/cameras.csv"

# Vamos a borrar primero el archivo si existe para
# probar diferentes métodos
if os.path.exists(archivo_nombre):
    os.remove(archivo_nombre)

# Metodo de base: usando urllib
if not os.path.exists(archivo_nombre):
    urllib.request.urlretrieve(archivo_url, archivo_nombre)

# En muchos casos es bueno apuntar la hora de descarga y guardarla en un archivo
fecha_descarga = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
with open("../data/timestamp.txt", "w") as fp:
    fp.write("Nombre del archivo: " + archivo_nombre)
    fp.write("\nDireccion: " + archivo_url)
    fp.write("\nFecha de descarga: " + fecha_descarga)

# Y vamos a ver si está el archivo donde lo guardamos
df = pd.read_csv(archivo_nombre)
print(df.describe())
print(df.head())

#%% Ahora vamos a bajar los datos de COVID y leer un archivo excel
covid_url = "http://datosabiertos.salud.gob.mx/gobmx/salud/datos_abiertos/datos_abiertos_covid19.zip"
covid_archivo = "../data/datos_abiertos_covid19.zip"
covid_dic_conceptos_url = "http://epidemiologia.salud.gob.mx/gobmx/salud/datos_abiertos/diccionario_datos_covid19.zip"
covid_dic_conceptos_archivo = "../data/diccionario.zip"

if not os.path.exists(covid_archivo):
    urllib.request.urlretrieve(covid_url, covid_archivo)  
    with zipfile.ZipFile(covid_archivo, "r") as zip_ref:
        zip_ref.extractall("../data/")
    
    urllib.request.urlretrieve(covid_dic_conceptos_url, covid.dic_conceptos_archivo)  
    with zipfile.ZipFile(covid.dic_conceptos_archivo, "r") as zip_ref:
        zip_ref.extractall("../data/")


df_covid = pd.read_csv("../data/200814COVID19MEXICO.csv", encoding="latin_1")
df_dic_conceptos = pd.read_excel("../data/diccionario_datos_covid19/Descriptores_0419.xlsx")

print(df_covid.head())
print(df_dic_conceptos.head())
