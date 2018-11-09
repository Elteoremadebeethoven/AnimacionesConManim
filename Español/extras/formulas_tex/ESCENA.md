# Contador de fórmulas en varios frames
Sustituir la fórmula
```
"\\frac{1}{t_2 - t_1}", "\\int_{t_1}^{t_2}","g(t)", "e", "^{-2\\pi i","f", "t}", "dt"
```
por la que se desee:

```python3
#Compilar usando -g o -s
from big_ol_pile_of_manim_imports import *
class ContadorFormulas(Scene):
	def construct(self):
		formula = TexMobject("\\frac{1}{t_2 - t_1}", "\\int_{t_1}^{t_2}","g(t)", "e", "^{-2\\pi i","f", "t}", "dt").scale(2)
		self.add(formula)
		contador = 0
		for j in range(len(formula)):
			elemento = TexMobject("%d" %contador)
			texto = formula[j]
			texto.set_color(RED)
			self.add(texto)
			elemento.set_fill(opacity=1)
			elemento.to_edge(UP)
			self.add(elemento)
			self.wait(0.2)
			elemento.set_fill(opacity=0)
			texto.set_color(WHITE)
			contador = contador + 1
```
<p align="center"><img src ="/Español/extras/formulas_tex/gifs/ContadorFormulas.gif" /></p>


# Contador en un sólo frame
## Paso 1:
Corrobora que la fórmula sea correcta, en este caso es:
```latex
\lim_{x\to\infty}{1\over x}=0
```
y desglozala para llegar a:

```python3
from big_ol_pile_of_manim_imports import *

#exporta -g o -s
def imprimir_formula_paso_1(self,texto,escala,escala_inversa,direccion,excepcion,separacion):
	excepcion=0
	self.add(texto.scale(escala))
	contador = 0
	for j in range(len(texto)):
		elemento = TexMobject("%d" %contador)
		texto[j].set_color(RED)
		self.add(texto[j])
		elemento.set_fill(opacity=1)
		elemento.to_edge(UP)
		self.add(elemento)
		self.wait(0.02)
		elemento.set_fill(opacity=0)
		texto[j].set_color(WHITE)
		contador = contador + 1 

#exporta -s
def imprimir_formula_paso_2(self,texto,escala,escala_inversa,direccion,excepcion,separacion):
	texto.scale(escala).set_color(RED)
	self.add(texto)
	contador = 0
	for j in range(len(texto)):
		permiso_imprimir=True
		for w in excepcion:
			if j==w:
				permiso_imprimir=False
		if permiso_imprimir:
			self.add(texto[j].set_color("#808080"))
		contador = contador + 1

	contador=0
	for j in range(len(texto)):
		permiso_imprimir=True
		elemento = TexMobject("%d" %contador,color=WHITE)
		elemento.scale(escala_inversa)
		elemento.next_to(texto[j],direccion,buff=separacion)
		for w in excepcion:
			if j==w:
				permiso_imprimir=False
		if permiso_imprimir:
			self.add(elemento)
		contador = contador + 1 

class Formula(Scene):
	def construct(self):
		formula=TexMobject("\\lim","_","{","x","\\to","\\infty","}","{","1","\\over","x","}","=","0")
		excepcion=[]
		escala=2.5
		escala_inversa=0.5
		direccion=DOWN
		separacion=0
		imprimir_formula_paso_1(self,formula,escala,escala_inversa,direccion,excepcion,separacion)

'''
class Formula_(Scene):
	def construct(self):
		formula=TexMobject(*formulas[])
		excepcion=[]
		escala=2.5
		escala_inversa=0.5
		direccion=DOWN
		separacion=0
		imprimir_formula_paso_2(self,formula,escala,escala_inversa,direccion,excepcion,separacion)
#'''
```
## Paso 2
Modifica 
```
imprimir_formula_paso_1
```
por
```
imprimir_formula_paso_2
```
y vuelve a compilarlo.
## Paso 3
Agrega al arreglo "excepcion" los elementos que están vacios y vuelve a compilar.
