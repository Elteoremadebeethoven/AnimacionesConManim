# Instación en GNU/Linux

Ver video tutorial en YouTube.

## Pasos previos a la instalación

### 1. Descargar de Manim 

* Ir al [repositorio oficial](https://github.com/3b1b/manim), click en el recuadro verde "Clone or download" y luego click en "Download ZIP".

<p align="center"><img src ="/Español/0_instalacion/gnuLinux/gifs/manimDescarga.png" /></p>

* Descomprimir carpeta manim-master preferentemente en el directorio principal y cambiar nombre de la carpeta a "manim".
* Crear otra carpeta (preferentemente en el directorio principal) dedicada a los videos de Manim, por ejemplo "vmanim".

<p align="center"><img src ="/Español/0_instalacion/gnuLinux/gifs/carp.png" /></p>

### 2. Modificar el archivo constants.py
Cambiar el código del archivo constants.py, en la linea que dice:
"Dropbox (3Blue1Brown)/3Blue1Brown Team Folder"
por la dirección de la carpeta dedicada los videos de manim (en nuestro ejemplo es "vmanim"). 

<p align="center"><img src ="/Español/0_instalacion/gnuLinux/gifs/nom.png" /></p>

## Instalación usando la terminal:
Abrir terminal y copiar los siguientes comandos.
### Instalación de LaTeX:

```sh
$ sudo apt-get install texlive-full
```

### Instalación de pip3:

```sh
$ sudo apt-get install python3-pip
```
### Instalación de ffmpeg:

```sh
$ sudo apt-get install ffmpeg
```

### Instalación de sox:

```sh
$ sudo apt-get install sox
```

### Instalación de paqueterías previas para instalar pycairo:

```sh
$ sudo apt-get install libcairo2-dev libjpeg-dev libgif-dev python3-dev libffi-dev
```

### Instalación de pycairo:

```sh
$ pip3 install pycairo
```

## Instalación de requerimientos:
Moverse a la carpeta de manim usando

```sh
~$ cd manim
~/manim$
```

Luego escribir:

```sh
~/manim$ python3 -m pip install -r requirements.txt
```

# Ejecución de Manim

Para ejecutar Manim por primera vez hay que ir a la carpeta de manim y escribir:

```sh
~/manim$ python3 extract_scene.py example_scenes.py SquareToCircle -pl
```

Ese código debería generar algo como esto:

<p align="center"><img src ="/Español/0_instalacion/gnuLinux/gifs/compilacion.gif" /></p>

# Almacenamiento

El video se almacenará ya sea en la misma carpeta de "manim" (en una subcarpeta que se va a llamar igual al archivo .py) o bien en la subcarpeta "animations" que estará dentro de la carpeta que definiste en constants.py (que en nuestro ejemplo es "vmanim"). Para el ejemplo de "SquareToCircle" el video estará ya sea en

```
~/manim/example_scenes/SquareToCircle/420p15
```
o en 
```
~/vmanim/example_scenes/animations/SquareToCircle/420p15
```

El 420p15 se refiere a la calidad del video a la que fue exportado. Dependerá de la versión de manim que descargaste el lugar donde se guarde el archivo.
