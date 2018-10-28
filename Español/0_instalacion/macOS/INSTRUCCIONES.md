# Instación en MacOS

Ver video tutorial en YouTube.

## Pasos previos a la instalción
### 1. Instalar algún editor de texto plano 
Recomiendo SublimteText, ver [video de instalación](https://www.youtube.com/watch?v=qqlLQ-5jH0c).

<p align="center"><img src ="/Español/0_instalacion/macOS/gifs/DescargarSublimeText.gif" /></p>

### 2. Descargar Manim del [repositorio oficial](https://github.com/3b1b/manim)
Click en "Clone or download" y luego click en "Download ZIP".

<p align="center"><img src ="/Español/0_instalacion/macOS/gifs/DescargarManim.gif" /></p>

### 3. Descomprimir el archivo (de preferencia en "Documents").
Aunque puede ser en cualquier lugar que desees, se usará "Documents" para este ejemplo.

<p align="center"><img src ="/Español/0_instalacion/macOS/gifs/pd.png" /></p>

### 4. Modificar el archivo constants.py
Abrir el archivo constants.py en la carpeta manim-master usando un editor de texto y cambiar el código que dice "Dropbox (3Blue1Brown)/3Blue1Brown Team Folder" por la dirección de otra carpeta dedicada a los archivos de Manim, yo recomiendo usar 

```
/Users/NombrePropietario/Movies
```

o símplemente 

```
Movies
```
Y guardar cambios.

<p align="center"><img src ="/Español/0_instalacion/macOS/gifs/MacP7.gif" /></p>

### 5. Abrir la terminal 
Se puede usar el buscador Spotlight escribiendo "terminal"

<p align="center"><img src ="/Español/0_instalacion/macOS/gifs/terminal.png" /></p>

## Instalación de Manim
### Instalar Homebrew
Copiar el código de la página oficial de [Homebrew](https://brew.sh/index_es) y pegarlo en la terminal (y dar enter).

<p align="center"><img src ="/Español/0_instalacion/macOS/gifs/MacP1.gif" /></p>

### Instalar LaTeX (versión completa)
Ir a la página oficial de [MacTeX](http://www.tug.org/mactex/), descargar el .pkg e instalar la versión completa ([video ayuda](https://www.youtube.com/watch?v=5CNmIaRxS20)).

<p align="center"><img src ="/Español/0_instalacion/macOS/gifs/MacP2.gif" /></p>

### Instalar Python 3
Ir a la página oficial de [Python](https://www.python.org/), a la zona de descargas y descargar la versión estable más reciente dependiendo de la versión que uses de Mac ([video ayuda](https://www.youtube.com/watch?v=0hGzGdRQeak)).

<p align="center"><img src ="/Español/0_instalacion/macOS/gifs/MacP3.gif" /></p>

### Instalar pip3
Ir a la página oficial de [pip](https://pip.pypa.io/en/stable/installing/), ir al archivo get-pip.py, copiar el texto en un documento de texto plano y guardar como get_pip.py en Documents.

Posteriormente moverse a la carpeta Documents usando la terminal con el comando "cd Documents":

```sh
MacPro-de-TB: ~ Alex$ cd Documents
MacPro-de-TB: Documents Alex$
```

Para corroborar que el archivo se encuentra ahí hay que escribir escribir "ls":

```sh
MacPro-de-TB: Documents Alex$ ls
...
...
get_pip.py
...
...
```
Una vez corroborada la ubicación del archivo lo compilamos usando "python3 get_pip.py":
```sh
MacPro-de-TB: Documents Alex$ python3 get_pip.py
```
Y continuar con la instalación.

<p align="center"><img src ="/Español/0_instalacion/macOS/gifs/MacP4.gif" /></p>

### Instalar paqueterías usando Homebrew
Copiar y pegar cada uno de los siguientes comandos a la terminal:

#### FFmpeg
```sh
brew install ffmpeg
```
#### Sox
```sh
brew install sox
```
#### Paqueterías extra
```sh
brew install cairo --use-clang
```

```sh
brew install py2cairo
```

```sh
brew install pkg-config
```

<p align="center"><img src ="/Español/0_instalacion/macOS/gifs/MacP5.gif" /></p>

### Instalar lista requirements.txt
Dentro de la carpeta "Documents" nos desplazamos a la carpeta de "manim-master" usando la terminal con el comando:

```sh
MacPro-de-TB: Documents Alex$ cd manim-master
MacPro-de-TB: manim-master Alex$
```

Luego copiar y pegar el siguiente comando:

```sh
python3 -m pip install -r requirements.txt
```
Y continuar con la instalación

<p align="center"><img src ="/Español/0_instalacion/macOS/gifs/MacP6.gif" /></p>

# Ejecución de Manim

Con la terminal posicionada en la carpeta manim-master copiar y pegar el siguiente código:

```sh
python3 extract_scene.py example_scenes.py WriteStuff -pl
```

Esto se deberá ver como:

<p align="center"><img src ="/Español/0_instalacion/macOS/gifs/MacP8.gif" /></p>

# Almacenamiento
El video se almacenará ya sea en la misma carpeta de "manim-master" (en una subcarpeta que se va a llamar igual al archivo .py) o bien en la subcarpeta "animations" que estará dentro de la carpeta que definiste en constants.py (que en nuestro ejemplo es "Movies"). Para el ejemplo de "WriteStuff" el video estará ya sea en

```
manim-master/example_scenes/WriteStuff/420p15
```
o en 
```
Movies/animations/example_scenes/WriteStuff/420p15
```

El 420p15 se refiere a la calidad del video a la que fue exportado. Dependerá de la versión de manim que descargaste el lugar donde se guarde el archivo.

<p align="center"><img src ="/Español/0_instalacion/macOS/gifs/almacenamiento.png" /></p>
