# Abrir y ver archivos json

import os  # Para manejo de archivos y directorios
import urllib # Una forma estandard de descargar datos
import pandas as pd
import json # Una forma estandar de leer archivos json 


archivo_url = "https://api.github.com/users/juliowaissman/repos"
archivo_nombre = "../data/repos.json"

if not os.path.exists(archivo_nombre):
    urllib.request.urlretrieve(archivo_url, archivo_nombre)

# Como cargarlos y como verlos
df_repos = pd.read_json(archivo_nombre)
df_repos.owner.apply(lambda x: x['login'])

# Ahora usando la librería json