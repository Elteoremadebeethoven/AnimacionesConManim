# Instación en MacOS

## Recomendaciones a la hora de instalar Manim
* Instalar algún editor de texto plano (recomiendo SublimteText).
* Descargar Manim del [repositorio oficial](https://github.com/3b1b/manim), click en "Clone or download" y luego click en "Download ZIP".
* Descomprimir el archivo en "Documents".
* Abrir la terminal (se puede usar el buscador Spotlight).

<p align="center"><img src ="/Español/0_instalacion/macOS/gifs/terminal.png" /></p>

## Instalar Homebrew
Copiar el código de la página oficial de [Homebrew](https://brew.sh/index_es) y pegarlo en la terminal (y dar enter).

<p align="center"><img src ="/Español/0_instalacion/macOS/gifs/MacP1.gif" /></p>

## Instalar LaTeX (versión completa)
Ir a la página oficial de [MacTeX](http://www.tug.org/mactex/), descargar el .pkg e instalar la versión completa.

<p align="center"><img src ="/Español/0_instalacion/macOS/gifs/MacP2.gif" /></p>

## Instalar Python 3
Ir a la página oficial de [Python](https://www.python.org/), a la zona de descargas y descargar la versión estable más reciente dependiendo de la versión que uses de Mac.

<p align="center"><img src ="/Español/0_instalacion/macOS/gifs/MacP3.gif" /></p>

## Instalar pip3
Ir a la página oficial de [pip](https://pip.pypa.io/en/stable/installing/), ir al archivo get-pip.py, copiar el texto en un documento de texto plano y guardar como get_pip.py en Documents.

Posteriormente moverse a la carpeta Documents usando la terminal con el comando:

```sh
MacPro-de-TB: ~ Alex$ cd Documents
MacPro-de-TB: Documents Alex$
```

Para corroborar que el archivo se encuentra ahí escribir:

```sh
MacPro-de-TB: Documents Alex$ ls
...
...
get_pip.py
...
...
```
Una vez corroborada la ubicación del archivo lo compilamos usando:
```sh
MacPro-de-TB: Documents Alex$ python3 get_pip.py
```
Y continuar con la instalación.

<p align="center"><img src ="/Español/0_instalacion/macOS/gifs/MacP4.gif" /></p>

## Instalar paqueterías usando Homebrew
Copiar y pegar cada uno de los siguientes comandos:

### FFmpeg
```sh
MacPro-de-TB: Documents Alex$ brew install ffmpeg
```
### Sox
```sh
MacPro-de-TB: Documents Alex$ brew install sox
```
### Paqueterías extra
```sh
MacPro-de-TB: Documents Alex$ brew install cairo --use-clang
```

```sh
MacPro-de-TB: Documents Alex$ brew install py2cairo
```

```sh
MacPro-de-TB: Documents Alex$ brew install pkg-config
```

<p align="center"><img src ="/Español/0_instalacion/macOS/gifs/MacP5.gif" /></p>

## Instalar lista requirements.txt
Dentro de la carpeta "Documents" nos desplazamos a la carpeta de "manim-master" usando la terminal con el comando:

```sh
MacPro-de-TB: Documents Alex$ cd manim-master
MacPro-de-TB: manim-master Alex$
```

Luego copiar y pegar el siguiente comando:

```sh
MacPro-de-TB: manim-master Alex$ python3 -m pip install -r requirements.txt
```
Y continuar con la instalación

<p align="center"><img src ="/Español/0_instalacion/macOS/gifs/MacP6.gif" /></p>

# Ejecución de Manim

## Modificar el archivo constants.py
Abrir el archivo constants.py usando un editor de texto y cambiar el código que dice "Dropbox (3Blue1Brown)/3Blue1Brown Team Folder" por la dirección de otra carpeta dedicada a los archivos de Manim, yo recomiendo usar 

```
/Users/NombrePropietario/Movies
```

o símplemente 

```
Movies
```
Y guardar cambios.

<p align="center"><img src ="/Español/0_instalacion/macOS/gifs/MacP7.gif" /></p>

## Compilación
Con la terminal posicionada en la carpeta manim-master copiar y pegar el siguiente código:

```sh
MacPro-de-TB: manim-master Alex$ python3 extract_scene.py example_scenes.py WriteStuff -pl
```

Esto se deberá ver como:

<p align="center"><img src ="/Español/0_instalacion/macOS/gifs/MacP8.gif" /></p>

# Almacenamiento
El video se almacenará ya sea en la misma carpeta de "manim-master" (en una subcarpeta que se va a llamar igual al archivo .py) o bien en la subcarpeta "animations" que estará dentro de la carpeta que definiste en constants.py (que en nuestro ejemplo es "Movies"). Para el ejemplo de "WriteStuff" el video estará ya sea en

```
manim-master/WriteStuff/420p15
```
o en 
```
Movies/animations/WriteStuff/420p15
```

El 420p15 se refiere a la calidad del video a la que fue exportado. Dependerá de la versión de manim que descargaste el lugar donde se guarde el archivo.

<p align="center"><img src ="/Español/0_instalacion/macOS/gifs/almacenamiento.png" /></p>