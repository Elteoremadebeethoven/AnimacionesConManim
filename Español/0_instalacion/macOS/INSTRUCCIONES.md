# Instación en MacOS

Ver video tutorial en YouTube.

## Instalación de Manim

### Abrir la terminal 
Se puede usar el buscador Spotlight escribiendo "terminal"

<p align="center"><img src ="/Español/0_instalacion/macOS/gifs/terminal.png" /></p>

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
Abrir la terminal y ejecutar:

```sh
brew install curl
mkdir ManimInstall
cd ManimInstall
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
```

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

### Descargar Manim del [repositorio oficial](https://github.com/3b1b/manim)
Click en "Clone or download" y luego click en "Download ZIP".

<p align="center"><img src ="/Español/0_instalacion/macOS/gifs/DescargarManim.gif" /></p>

### Descomprimir el archivo (de preferencia en "Documents" o "Downloads").
Aunque puede ser en cualquier lugar que desees, siempre y cuando el nombre de la carpeta no use espacios. Se usará "Documents" para este ejemplo.

<p align="center"><img src ="/Español/0_instalacion/macOS/gifs/pd.png" /></p>

<p align="center"><img src ="/Español/0_instalacion/macOS/gifs/MacP5.gif" /></p>

### Instalar lista requirements.txt
Nos movemos a la carpeta de manim con la terminal y luego copiamos y pegamos los siguientes comandos:

```sh
python3 -m pip install -r requirements.txt
python3 -m pip install pyreadline
```
Y continuar con la instalación

<p align="center"><img src ="/Español/0_instalacion/macOS/gifs/MacP6.gif" /></p>

# Ejecución de Manim

Con la terminal posicionada en la carpeta manim-master copiar y pegar el siguiente código:

```sh
python3 -m manim example_scenes.py WriteStuff -pl
```

Esto se deberá ver como:

<p align="center"><img src ="/Español/0_instalacion/macOS/gifs/MacP8.gif" /></p>

# Almacenamiento
Al ejecutar manim por primera vez se crearà una carpeta llamada "media" y un archvio de texto "media_dir.txt". En la carpeta "media" se almacenaràn los videos por defecto, si deseas modificar la carpeta donde se exporten los videos tienes que escribir el directorio completo en el archivo "media_dir.txt".

# Recomendación final: Instalar algún editor de texto plano 
Recomiendo SublimteText, ver [video de instalación](https://www.youtube.com/watch?v=qqlLQ-5jH0c).

<p align="center"><img src ="/Español/0_instalacion/macOS/gifs/DescargarSublimeText.gif" /></p>
