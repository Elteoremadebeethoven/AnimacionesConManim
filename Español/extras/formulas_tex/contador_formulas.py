from big_ol_pile_of_manim_imports import *
class ContadorFormulas(Scene):
	def construct(self):
		formula = TexMobject("\\frac{1}{t_2 - t_1}", "\\int_{t_1}^{t_2}",
		"g(t)", "e", "^{-2\\pi i","f", "t}", "dt").scale(2)
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
			self.wait(1.5)
			elemento.set_fill(opacity=0)
			texto.set_color(WHITE)
			contador = contador + 1