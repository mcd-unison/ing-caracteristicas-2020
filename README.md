<img src="logo.png" width="150">

# Repositorio con material del curso de Ingeniería de Características

## 1. Instalación del entorno de trabajo

### 1.1 Instalación de git y este repositorio

1. Si tienes Window 10 (2016 o superior), priero instala el [*subsistema Linux para windows*](https://www.laptopmag.com/articles/use-bash-shell-windows-10) ([aqui otra guía](https://hackernoon.com/how-to-install-bash-on-windows-10-lqb73yj3), ero hay muchas en internet). Si tienes una versión más viejita de Windows, puedes descargarlo de [este lugar](https://gitforwindows.org). Usuarios de Linux y MacOS ir directamente a su terminal favorita.
2. Realiza el comando `$ git --version` en tu terminal *bash* y si no reconoce el comando, puedes descargar e instalar *git* de [este lugar](https://git-scm.com). 
3. En el MIT desarrollaron una clase que se llama [The Missing Semester of Your CS Education](https://missing.csail.mit.edu). Toda está muy interesante, pero en la [primera sesión](https://missing.csail.mit.edu/2020/course-shell/) enseñan a usar lo básico del *bash* y en la [sesión 6](https://missing.csail.mit.edu/2020/version-control/) explican el uso de *git*. En todas las sesiones nos presumen el pizarronzote y las instalaciones que tiene el MIT para dar clases.
4. Si usas MacOS, te recomiendo probar [iTerm2](https://www.iterm2.com), y en todos los casos yo les recomiendo revisar el uso de [`zsh + oh my zsh`](https://ohmyz.sh). *Zsh* es un *shield* que es mas bonito que *bash* (y casi igual, lo que haces en *bash* se hace de la misma manera en *zsh*). Es fácil buscar posts para tunear la linea de comandos en cualquiera de los sistemas operativos en los que trabajes.
5. Descarga este repositorio en el directorio que tu quieras con el comando  
   ```bash
   $ git clone https://github.com/mcd-unison/ing-caracteristicas.git
   ```

### 1.2. Instalación de `python`

1. Si ya se tiene la distribución de *Anaconda* instalada, pasar al siguiente paso, si no, instalas la versión mímina *Miniconda* de *python 3.X* con [estas instrucciones](https://docs.conda.io/en/latest/miniconda.html).
2. En la terminal utilizar el comando *conda* para crear un entorno virtual a partir del archivo `requirements.yml` que viene en el repositorio.
   ```bash
   $ conda env -f requirements.yml -n ing-car
   ```
   o cualquier otro nombre que se le quiera poner al entorno
3. Cada vez que se vaya a utilizar el entorno, utilizar:
   ```bash
   $ conda activate ing-car
   ```
4. Cuando ya se termine de usar, desactivar el entorno virtual ( y mantener a cada proyecto con su propio entorno virtual)
   ```bash
   $ conda deactivate
   ```

### 1.3. Instalación de R y Rstudio

1. Instalar el lenguaje R, descargandolo de su [portal oficial](https://cran.itam.mx), y [RStudio Desktop](https://rstudio.com/products/rstudio/download/).
2. Dentro de RStudio, instalar las librerías de [tidyverse](https://www.tidyverse.org), en la consola con el comando:
   ```r
   > install.package('tidyverse')
   ```
3. En cada sección donde hay codigo en R se encuentra un archivo `xxxx.Rproj`. Abrirlo para ajustar el directorio de trabajo y demás configuraciones. Por ejemplo, para la obtención de datos abrir el proyecto `./obtener\ datos/R/R.Rproj`.
   
