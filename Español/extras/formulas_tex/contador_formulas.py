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
		formula=TexMobject()
		excepcion=[]
		escala=3.5
		escala_inversa=0.5
		direccion=DOWN
		separacion=0
		imprimir_formula_paso_2(self,formula,escala,escala_inversa,direccion,excepcion,separacion)

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
