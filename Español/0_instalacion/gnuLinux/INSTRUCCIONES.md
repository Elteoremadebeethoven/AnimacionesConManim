# Instación en GNU/Linux

Ver video tutorial en [YouTube](https://www.youtube.com/watch?v=dwiBKFTJWY8).

## Pasos previos a la instalación

### 1. Descargar de Manim 

* Ir al [repositorio oficial](https://github.com/3b1b/manim), click en el recuadro verde "Clone or download" y luego click en "Download ZIP".

<p align="center"><img src ="/Español/0_instalacion/gnuLinux/gifs/manimDescarga.png" /></p>

* Descomprimir carpeta manim-master preferentemente en el directorio principal.


## Instalación usando la terminal:
Abrir terminal y copiar los siguientes comandos.

### Instalación de LaTeX:
Debian:
```sh
$ sudo apt-get install texlive-full
```
Arch:
```sh
$ sudo pacman -S texlive-most
```
Fedora:
```sh
# yum -y install texlive-collection-latexextra
```
### Instalación de Python3.7
Debian:
```sh
$ sudo apt-get install python3.7-minimal
```

Arch: Siempre está al día.

Fedora:
```sh
# yum install gcc openssl-devel bzip2-devel libffi-devel
# cd /usr/src
# wget https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tgz
# tar xzf Python-3.7.3.tgz
# cd Python-3.7.3
# ./configure --enable-optimizations
# make altinstall
# rm /usr/src/Python-3.7.3.tgz
```

### Instalación de pip:
Todas las distros:
```sh
$ mkdir pip
$ cd pip
$ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
$ python3 get-pip.py
```

### Instalación de ffmpeg:
Debian
```sh
$ sudo apt-get install ffmpeg
```
Arch-Linux:
```sh
$ sudo pacman -S ffmpeg
```
Fedora:
```sh
$ sudo dnf install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm
$ sudo dnf install https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
$ sudo dnf install ffmpeg ffmpeg-devel
```

### Instalación de sox:
Debian
```sh
$ sudo apt-get install sox
```
Arch-Linux (with AUR):
```sh
$ aurman -S sox
```
Fedora:
Descárgalo de: https://pkgs.org/download/sox

### Instalación de paqueterías previas para instalar pycairo:
Para todas las distros:
```sh
$ python3.7 -m pip install pyreadline
$ python3.7 -m pip install pydub
```
Además, para las basadas en Debian:
```sh
$ sudo apt-get install libcairo2-dev libjpeg-dev libgif-dev python3-dev libffi-dev
```

## Instalación de requerimientos:
Moverse a la carpeta de manim:

```sh
~/manim-master$
```

Luego escribir:

```sh
$ python3.7 -m pip install -r requirements.txt
```

# Ejecución de Manim

Para ejecutar Manim por primera vez hay que ir a la carpeta de manim y escribir:

```sh
$ python3 -m manim example_scenes.py SquareToCircle -pl
```

Ese código debería generar algo como esto:

<p align="center"><img src ="/Español/0_instalacion/gnuLinux/gifs/compilacion.gif" /></p>

