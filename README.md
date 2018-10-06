# Curso de Manim
## Temas del curso (actualizando)
0. Instalación en Windows y GNU/Linux (próximamente en Mac).
1. [Formato de textos (PDF)](https://drive.google.com/open?id=1BaWn_QJEz7hsizaLXFpM0YVOn9Gxi_Yn)/YouTube/[Resumen]()
* [Fórmulas en TeX (PDF)](https://drive.google.com/open?id=1sPksk698UezNpYn7piEuGEwIqJd8TZMd)/YouTube/[Resumen]()
2. [(PDF)]()/YouTube/[Resumen]()
3. [(PDF)]()/YouTube/[Resumen]()
4. [(PDF)]()/YouTube/[Resumen]()
5. /YouTube.

## ¿Qué es Manim?
[Manim](https://github.com/3b1b/manim) es una herramienta gratuita de animación creada por [Grant Sanderson](http://www.3blue1brown.com/) ([twitter](https://twitter.com/3blue1brown?lang=es)), matemático de Stantford y dueño del canal de YouTube [3Blue1Brown](https://www.youtube.com/channel/UCYO_jab_esuFRV4b17AJtAw). Está especializada en temas científicos, principalmente de carácter matemático, por lo que está basada en comandos de LaTeX (principalmente en TeX).

## ¿Qué es LaTeX?
LaTeX es un procesador de textos especializada en el ambito científico, sin embargo, Manim sólo utiliza los comandos TeX (con algunas excepciones), que se refieren a la escritura de fórmulas. Un ejemplo del código en TeX es:
```latex
\frac{d}{dx}f(x)=\lim_{h\to 0}\frac{f(x+h)-f(x)}{h}.
```
Este comando TeX lo compila como:
<p align="center"><img src ="http://www.sciweavers.org/upload/Tex2Img_1538658756/render.png" /></p>

## ¿Para quién va dirigido el curso?
Este curso se dirige principalmente a profesores que quieran explicar de una forma didáctica y gráfica algún desarrollo matemático o la resolución de problemas especialmente complejos. El curso se extiende a cualquier persona que quiera explicar algún tema científico de una forma original.

## ¿Necesito saber programar en Python y LaTeX para entender el curso?
Para entender el curso es posible no saber absolutamente nada de programación (aunque es preferible para que el aprendizage sea más rápido). Además de aprender Python 3 se requerirán conocimientos de TeX para la escritura de las fórmulas. De igual forma se darán a conocer herramientas como [Pencil chromestore](http://s1.daumcdn.net/editor/fp/service_nc/pencil/Pencil_chromestore.html), [Codecogs](https://www.codecogs.com/latex/eqneditor.php), [Rinconmatematico](http://rinconmatematico.com/mathjax/), [latex4technics](https://www.latex4technics.com/), [sciweavers](http://www.sciweavers.org/free-online-latex-equation-editor) entre otras páginas para aprender a escribir fórmulas en TeX.

## ¿Necesito una computadora moderna para usar Manim?
No, con 512 MB de Ram y un procesador Intel Core Duo (o similar) es más que suficiente, la única diferencia entre una máquina potente y una de bajos recursos es el tiempo de compilación (entre menos recursos más tiempo demorará en compilar).

## ¿Qué ventajas ofrece Manim en contraste con otras herramientas de animación profesionales?
### Ventajas:
* Es gratis y legal.
* Funciona en Windows, GNU/Linux (cualquier distribución) y Mac perfectamente, aunque es preferible usar Mac o GNU/Linux.
* Se puede usar en computadoras antiguas.
* Al ser de código abierto es completamente personalizable al gusto del usuario.
* Constantemente se está mejorando ya que nuevos usuarios tabajan en él a través de su repositorio oficial en [GitHub](https://github.com/3b1b/manim).
* Los archivos de video .mp4 que exporta, aún siendo de muy alta calidad (1440p), son muy ligeros.
* Las fórmulas son creadas usando comandos TeX, por lo que son de calidad profesional (en lo que respecta a la comunidad científica).
* En caso de no tener conocimientos de programación, es una buena herramienta para empezar a aprender Python 3 y LaTeX.
### Desventajas:
* Si no tienes la paquetería de LaTeX (completa) instalada ocupará más de 6 GB de espacio en tu computadora.
* No se usa una interfaz gráfica para realizar las animaciones, todo se basa en comandos de Python 3 y TeX. El ejemplo del cásico Hello world! sería:
```python
from big_ol_pile_of_manim_imports import *
class HelloWorld(Scene):
    def construct(self):
        helloWorld = TextMobject("Hello world!")
        self.play(Write(helloWorld))
        self.wait()
```
<p align="center"><img src ="/HelloWorld.gif" /></p>

## Requerimientos
* Python 3.5 (o superior)
* pip3 (para instalar la lista de requirements.txt)
* pycairo (suele dar problemas en la instalación de requirements.txt por lo que es recomendable instalarla antes)
* ffmpeg
* LaTeX (Miktex para Windows y TexLive para GNU/Linux o Mac) completo
* sox
* Requerimientos en la lista de requirements.txt

Peso total aproximado: 8 GB

