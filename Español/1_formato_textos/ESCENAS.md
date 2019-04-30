# Formato de textos
Importante: Recuerda que antes de todo se deben importar las paqueterías estandar usando
```python3
from big_ol_pile_of_manim_imports import *
```
como primera linea.

# Configuración de LaTeX
Para los hispanohablantes la configuración de los símbolos son especiales, ya que usamos la "ñ" y los acentos. Así que hay que cambiar la configuración.

## Para los usarios de Windows
Hay que ir a manimlib/tex_template.txt, lo abrimos con un editor de texto y cambiamos la linea 3:

```latex
\usepackage[english]{babel}
```

por

```latex
\usepackage[latin1]{inputenc}
\usepackage[T1]{fontenc}
```

En caso de que aún así nos genere un error entonces en lugar de ```latin1``` escribimos ```utf8```.

## Para los usarios de Mac y Linux
Hay que ir a manimlib/tex_template.txt, lo abrimos con un editor de texto y cambiamos la linea 3:

```latex
\usepackage[english]{babel}
```

por

```latex
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
```

En caso de que aún así nos genere un error entonces en lugar de ```utf8``` escribimos ```latin1```.


## Programas

### 
```python3
class TextoWrite(Scene): 
    def construct(self): 
        texto = TextMobject("Esto es un texto normal")
        self.play(Write(texto))
        self.wait(3)
```
<p align="center"><img src ="/Español/1_formato_textos/gifs/TextoWrite.gif" /></p>

### 
```python3
class TextoAdd(Scene): 
    def construct(self): 
        texto = TextMobject("Esto es un texto normal")
        self.add(texto)
        self.wait(3)
```
<p align="center"><img src ="/Español/1_formato_textos/gifs/TextoAdd.gif" /></p>

### 
```python3
class Formula(Scene): 
    def construct(self): 
        formula = TexMobject("Esto es una formula")
        self.play(Write(formula))
        self.wait(3)
```
<p align="center"><img src ="/Español/1_formato_textos/gifs/Formula.gif" /></p>

### 
```python3
class TextoMixto(Scene): 
    def construct(self): 
        textoMixto = TextMobject("""
        	Esto es un texto normal,
        	$esto es una formula$,
        	$$esto es una formula$$
        	""")
        self.play(Write(textoMixto))
        self.wait(3)
```
<p align="center"><img src ="/Español/1_formato_textos/gifs/TextoMixto.gif" /></p>

### 
```python3
class TextoMixto2(Scene): 
    def construct(self): 
        textoMixto = TextMobject("""
        	Esto es un texto normal,
        	$\\frac{x}{y}$,
        	$$x^2+y^2=a^2$$
        	""")
        self.play(Write(textoMixto))
        self.wait(3)
```
<p align="center"><img src ="/Español/1_formato_textos/gifs/TextoMixto2.gif" /></p>

### 
```python3
class TextoMixtoDisplay(Scene): 
    def construct(self): 
        textoMixto = TextMobject("""
        	Esto es un texto normal,
        	$\\displaystyle\\frac{x}{y}$,
        	$$x^2+y^2=a^2$$
        	""")
        self.play(Write(textoMixto))
        self.wait(3)
```
<p align="center"><img src ="/Español/1_formato_textos/gifs/TextoMixtoDisplay.gif" /></p>

### 
```python3
class PosicionTextoCentro(Scene):
    def construct(self):
        texto = TextMobject("Texto genérico.")
        self.play(Write(texto))
        self.wait(3)
```
<p align="center"><img src ="/Español/1_formato_textos/gifs/PosicionTextoCentro.gif" /></p>

### 
```python3
class PosicionTextoSuperior(Scene):
    def construct(self):
        texto = TextMobject("Texto genérico.")
        texto.to_edge(UP)
        self.play(Write(texto))
        self.wait(3)
```
<p align="center"><img src ="/Español/1_formato_textos/gifs/PosicionTextoSuperior.gif" /></p>

### 
```python3
class PosicionTextoInferior(Scene):
    def construct(self):
        texto = TextMobject("Texto genérico.")
        texto.to_edge(DOWN)
        self.play(Write(texto))
        self.wait(3)
```
<p align="center"><img src ="/Español/1_formato_textos/gifs/PosicionTextoInferior.gif" /></p>

### 
```python3
class PosicionTextoDerecha(Scene): #Probar con "Texto genérico ampliado"
    def construct(self):
        texto = TextMobject("Texto genérico.")
        texto.to_edge(RIGHT)
        self.play(Write(texto))
        self.wait(3)
```
<p align="center"><img src ="/Español/1_formato_textos/gifs/PosicionTextoDerecha.gif" /></p>

### 
```python3
class PosicionTextoIzquierda(Scene):
    def construct(self):
        texto = TextMobject("Texto genérico.")
        texto.to_edge(LEFT)
        self.play(Write(texto))
        self.wait(3)
```
<p align="center"><img src ="/Español/1_formato_textos/gifs/PosicionTextoIzquierda.gif" /></p>

### 
```python3
class PosicionTextoSuperiorDerecha(Scene):
    def construct(self):
        texto = TextMobject("Texto genérico.")
        texto.to_edge(UP+RIGHT)
        self.play(Write(texto))
        self.wait(3)
```
<p align="center"><img src ="/Español/1_formato_textos/gifs/PosicionTextoSuperiorDerecha.gif" /></p>

### 
```python3
class PosicionTextoInferiorIzquierda(Scene): 
    def construct(self): #Este es un comentario, no es código
        texto = TextMobject("Texto genérico.") #Este es un comentario, no es código
        texto.to_edge(LEFT+DOWN)
        self.play(Write(texto))
        self.wait(3)
```
<p align="center"><img src ="/Español/1_formato_textos/gifs/PosicionTextoInferiorIzquierda.gif" /></p>

### 
```python3
class PosicionPersonalizado1(Scene):
    def construct(self):
        textoM = TextMobject("Texto genérico.")
        textoC = TextMobject("Texto genérico central.") #Texto de referencia
        textoM.move_to(0.25*UP)  #Jugar con los valores numéricos
        self.play(Write(textoM),Write(textoC))
        self.wait(3)
```
<p align="center"><img src ="/Español/1_formato_textos/gifs/PosicionPersonalizado1.gif" /></p>

### 
```python3
class PosicionPersonalizado2(Scene): #move_to siempre es referente al centro
    def construct(self):
        textoM = TextMobject("Texto genérico.")
        textoC = TextMobject("Texto genérico central.")
        textoM.move_to(1*UP+1*RIGHT)
        self.play(Write(textoM),Write(textoC))
        self.wait(1)
        textoM.move_to(1*UP+1*RIGHT) #El sistema de referencia es el centro
        self.play(Write(textoM))
        self.wait(3)
```
<p align="center"><img src ="/Español/1_formato_textos/gifs/PosicionPersonalizado2.gif" /></p>

### 
```python3
class PosicionRelativa1(Scene):
    def construct(self):
        textoM = TextMobject("Texto relativo.")
        textoC = TextMobject("Texto de referencia.")
        textoM.next_to(textoC,LEFT,buff=1) #La posición toma como referencia la posición de textoC
        self.play(Write(textoM),Write(textoC))
        self.wait(3)
```
<p align="center"><img src ="/Español/1_formato_textos/gifs/PosicionRelativa1.gif" /></p>

### 
```python3
class PosicionRelativa2(Scene):
    def construct(self):
        textoM = TextMobject("Texto relativo.")
        textoC = TextMobject("Texto de referencia.")
        textoM.shift(UP*0.1) #La referencia es el mismo textoM, texto u objeto
        self.play(Write(textoM),Write(textoC))
        self.wait(3)
```
<p align="center"><img src ="/Español/1_formato_textos/gifs/PosicionRelativa2.png" /></p>

### 
```python3
class Rotacion(Scene):
    def construct(self):
        textoM = TextMobject("Texto relativo.")
        textoC = TextMobject("Texto de referencia.")
        textoM.shift(UP)
        textoM.rotate(PI/4) #El centro es el centro de area del texto, en radianes, texto u objeto
        self.play(Write(textoM),Write(textoC))
        self.wait(2)
        textoM.rotate(PI/4)
        self.wait(2)
        textoM.rotate(PI/4)
        self.wait(2)
        textoM.rotate(PI/4)
        self.wait(2)
        textoM.rotate(PI)
        self.wait(2)
```
<p align="center"><img src ="/Español/1_formato_textos/gifs/Rotacion.gif" /></p>

### 
```python3
class Espejo(Scene):
    def construct(self):
        textoM = TextMobject("Texto referencia.")
        textoM.flip(UP) # Texto y objeto
        self.play(Write(textoM))
        self.wait(2)
```
<p align="center"><img src ="/Español/1_formato_textos/gifs/Espejo.gif" /></p>

### 
```python3
class Tamanhos(Scene):
	def construct(self):
		textoHuge = TextMobject("{\\Huge Huge Texto 012.\\#!?} Texto normal")
		textohuge = TextMobject("{\\huge huge Texto 012.\\#!?} Texto normal")
		textoLARGE = TextMobject("{\\LARGE LARGE Texto 012.\\#!?} Texto normal")
		textoLarge = TextMobject("{\\Large Large Texto 012.\\#!?} Texto normal")
		textolarge = TextMobject("{\\large large Texto 012.\\#!?} Texto normal")
		textoNormal = TextMobject("{\\normalsize normal Texto 012.\\#!?} Texto normal")
		textosmall = TextMobject("{\\small small Texto 012.\\#!?} Texto normal")
		textofootnotesize = TextMobject("{\\footnotesize footnotesize Texto 012.\\#!?} Texto normal")
		textoscriptsize = TextMobject("{\\scriptsize scriptsize Texto 012.\\#!?} Texto normal")
		textotiny = TextMobject("{\\tiny tiny Texto 012.\\#!?} Texto normal")
		textoHuge.to_edge(UP)
		textohuge.next_to(textoHuge,DOWN,buff=0.1)
		textoLARGE.next_to(textohuge,DOWN,buff=0.1)
		textoLarge.next_to(textoLARGE,DOWN,buff=0.1)
		textolarge.next_to(textoLarge,DOWN,buff=0.1)
		textoNormal.next_to(textolarge,DOWN,buff=0.1)
		textosmall.next_to(textoNormal,DOWN,buff=0.1)
		textofootnotesize.next_to(textosmall,DOWN,buff=0.1)
		textoscriptsize.next_to(textofootnotesize,DOWN,buff=0.1)
		textotiny.next_to(textoscriptsize,DOWN,buff=0.1)
		self.add(textoHuge,textohuge,textoLARGE,textoLarge,textolarge,textoNormal,textosmall,textofootnotesize,textoscriptsize,textotiny)
		self.wait(3)
```
<p align="center"><img src ="/Español/1_formato_textos/gifs/Tamanhos.gif" /></p>

### 
```python3
class TamanhosPersonalizados(Scene):
	def construct(self):
		texto = TextMobject("{\\fontsize{60}{70}\\selectfont Texto.}")
		self.play(Write(texto))
		self.wait(3)
```
<p align="center"><img src ="/Español/1_formato_textos/gifs/TamanhosPersonalizados.gif" /></p>

### 
```python3
class Fuentes(Scene):
	def construct(self):
		textoNormal = TextMobject("{Texto normal 012.\\#!?} Texto normal")
		textoItalica = TextMobject("\\textit{Texto en itálicas 012.\\#!?} Texto normal")
		textoMaquina = TextMobject("\\texttt{Texto en máquina 012.\\#!?} Texto normal")
		textoNegritas = TextMobject("\\textbf{Texto en negritas 012.\\#!?} Texto normal")
		textoSL = TextMobject("\\textsl{Texto en sl 012.\\#!?} Texto normal")
		textoSC = TextMobject("\\textsc{Texto en sc 012.\\#!?} Texto normal")
		textoNormal.to_edge(UP)
		textoItalica.next_to(textoNormal,DOWN,buff=.5)
		textoMaquina.next_to(textoItalica,DOWN,buff=.5)
		textoNegritas.next_to(textoMaquina,DOWN,buff=.5)
		textoSL.next_to(textoNegritas,DOWN,buff=.5)
		textoSC.next_to(textoSL,DOWN,buff=.5)
		self.add(textoNormal,textoItalica,textoMaquina,textoNegritas,textoSL,textoSC)
		self.wait(3)
```
<p align="center"><img src ="/Español/1_formato_textos/gifs/Fuentes.gif" /></p>
