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
2. En la terminal utilizar el comando *conda* para crear un entorno virtual.
