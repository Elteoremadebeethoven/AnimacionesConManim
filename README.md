# Curso de Manim
## Temas del curso (actualizando)
1. Instalación en Windows, GNU/Linux (próximamente en Mac).
2. [Formato de textos](https://github.com/Elteoremadebeethoven/AnimacionesConManim/blob/master/formato_textos.py)
3. Fórmulas en TeX

## ¿Qué es Manim?
[Manim](https://github.com/3b1b/manim) es una herramienta gratuita de animación especializada en temas científicos (especialmente de caracter matemático) creada por [Grant Sanderson](http://www.3blue1brown.com/) ([twitter](https://twitter.com/3blue1brown?lang=es)), Matemático de Stantford y dueño del canal de YouTube [3Blue1Brown](https://www.youtube.com/channel/UCYO_jab_esuFRV4b17AJtAw).

## ¿Para quién va dirigido el curso?
Este curso se dirige especialemte a profesores que quieran explicar de una forma didáctica y gráfica algún desarrollo matemático o resolución de problema especialmente complejo, pero el curso se extiende a cualquier persona que quiera explicar algún tema científico de una forma original.

## ¿Necesito saber programar en Python para entender el curso?
Preferentemente sí, pero no es necesario. Hipotéticamente es posible no saber absolutamente nada de programación y poder entender el curso, aunque además de aprender Python 3 se requerirán conocimientos de TeX para la escritura de las fórmulas, pero de igual forma se darán a conocer herramientas como [Pencil chromestore](http://s1.daumcdn.net/editor/fp/service_nc/pencil/Pencil_chromestore.html) y [Code Cogs](https://www.codecogs.com/latex/eqneditor.php) para aprender a escribir fórmulas en TeX.

## ¿Necesito una computadora moderna para usar Manim?
No, con 512 MB de Ram y mínimo un procesador Intel Core Duo (o similar) es más que suficiente, la única diferencia entre una máquina potente y una de bajos recursos será el tiempo de compilación (entre menos recursos más tiempo demorará en compilar).

## ¿Qué ventajas ofrece Manim en contraste con otras herramientas de animación profesionales?
### Ventajas:
* Es gratis y legal.
* Funciona en Windows, GNU/Linux (cualquier distribución) y Mac perfectamente, aunque es preferible usar Mac o GNU/Linux.
* Se puede usar en computadoras antiguas.
* Constantemente se está mejorando ya que nuevos usuarios tabajan en él a través de su repositorio oficial en [GitHub](https://github.com/3b1b/manim).
* Los archivos de video .mp4 que exporta, aún siendo de muy alta calidad (1440p), son muy ligeros.
* Las animaciones son creadas usando comandos TeX, por lo que son de calidad profesional (en lo que respecta a la comunidad científica).
* En caso de no tener conocimientos en programación, es una buena excusa para empezar a aprender Python 3 y LaTeX.
### Desventajas:
* Si no tienes la paquetería de LaTeX (completa) instalada ocupará más de 6 GB de espacio en tu computadora.
* No se usa una interfaz gráfica para realizar las animaciones, todo se basa en comandos de Python 3. El ejemplo del cásico Hello world! sería ([ver en YouTube](https://www.youtube.com/watch?v=wlq86KsAnUA)):
```python
from big_ol_pile_of_manim_imports import *
class HelloWorld(Scene):
    def construct(self):
        helloWorld = TextMobject("Hello world!")
        self.play(Write(helloWorld))
        self.wait()
```
[![https://i9.ytimg.com/vi/wlq86KsAnUA/mq2.jpg?sqp=CJiLzt0F&rs=AOn4CLDDAXHAYHC7c66tUU3T6dCB2IL7Mw](http://img.youtube.com/vi/wlq86KsAnUA/0.jpg)](http://www.youtube.com/watch?v=wlq86KsAnUA "Hello world! (in Manim)")
## Requermientos
* Python 3.5 (o superior)
* pip3 (para instalar la lista de requirements.txt)
* pycairo (suele dar problemas en la instalación de requirements.txt por lo que es recomendable instalarla antes)
* ffmpeg
* LaTeX (Miktex para Windows y TexLive para Linux/Mac) completo
* sox
* Requerimeitos en la lista de requirements.txt

Peso total aproximado: 8 GB

