from big_ol_pile_of_manim_imports import *
#RENOMBRAR: Formato_textos
class Animacion1(Scene): #Este es un comentario, no es código
    def construct(self): #Este es un comentario, no es código
        texto = TextMobject(
            """Esto es texto normal, $esto es una formula$
            $$esto es una formula$$"""
        )
        self.play(Write(texto))
        self.wait(3)

class Animacion2(Scene):
    def construct(self):
        texto = TextMobject(
            """Esto es texto normal, $\\frac{x}{y}$
            $$x^2+y^2=a^2$$"""
        )
        self.play(Write(texto))
        self.wait(3)

class Animacion3(Scene):
    def construct(self):
        texto = TextMobject(
            """Esto es texto normal, $\\displaystyle\\frac{x}{y}$
            $$x^2+y^2=a^2$$"""
        )
        self.play(Write(texto))
        self.wait(3)

class Animacion4(Scene): #usando add
    def construct(self):
        texto = TextMobject(
            """Esto es texto normal, $\\displaystyle\\frac{x}{y}$
            $$x^2+y^2=a^2$$"""
        )
        self.add(texto)
        self.wait(3)

class Formula(Scene):
	def construct(self):
		tex = TexMobject("\\sqrt{\\frac{x}{y}}")
		self.play(Write(tex))
		self.wait(3)

class PosicionamientoTextoCentro(Scene):
    def construct(self):
        texto = TextMobject("Texto genérico.")
        self.play(Write(texto))
        self.wait(3)

class PosicionamientoTextoSuperior(Scene):
    def construct(self):
        texto = TextMobject("Texto genérico.")
        texto.to_edge(UP)
        self.play(Write(texto))
        self.wait(3)

class PosicionamientoTextoInferior(Scene):
    def construct(self):
        texto = TextMobject("Texto genérico.")
        texto.to_edge(DOWN)
        self.play(Write(texto))
        self.wait(3)

class PosicionamientoTextoDerecha(Scene):
    def construct(self):
        texto = TextMobject("Texto genérico ampliado.")
        texto.to_edge(RIGHT)
        self.play(Write(texto))
        self.wait(3)

class PosicionamientoTextoIzquierda(Scene):
    def construct(self):
        texto = TextMobject("Texto genérico.")
        texto.to_edge(LEFT)
        self.play(Write(texto))
        self.wait(3)

class PosicionamientoTextoSuperiorDerecha(Scene):
    def construct(self):
        texto = TextMobject("Texto genérico.")
        texto.to_edge(UP+RIGHT)
        self.play(Write(texto))
        self.wait(3)

class PosicionamientoTextoInferiorIzquierda(Scene): 
    def construct(self): #Este es un comentario, no es código
        texto = TextMobject("Texto genérico.") #Este es un comentario, no es código
        texto.to_edge(LEFT+DOWN)
        self.play(Write(texto))
        self.wait(3)

class PosicionamientoTextoEspecial1(Scene): #introdiccion con move_to
    def construct(self):
        textoM = TextMobject("Texto genérico.")
        textoC = TextMobject("Texto genérico.")
        textoM.move_to(0.25*UP)
        self.play(Write(textoM),Write(textoC))
        self.wait(3)

class PosicionamientoTextoEspecial2(Scene): #move_to siempre es referente al centro
    def construct(self):
        textoM = TextMobject("Texto genérico.")
        textoC = TextMobject("Texto genérico.")
        textoM.move_to(0.5*UP+0.5*RIGHT)
        self.play(Write(textoM),Write(textoC))
        self.wait(1)
        textoM.move_to(1*UP+1*RIGHT) #El sistema de referencia es el centro
        self.play(Write(textoM))

class PosicionamientoTextoEspecial3v1(Scene): 
    def construct(self):
    	#Escribe primero 
        textoM = TextMobject("Texto genérico.")
        textoC = TextMobject("Texto genérico.")
        textoC.move_to(1*UP+1*RIGHT)
        textoM.move_to(1*UP+1*RIGHT)
        self.play(Write(textoM),Write(textoC))
        self.wait(1)

class PosicionamientoTextoEspecial3v2(Scene): #usando next_to,posicionamiento relativo con move_to
    def construct(self):
    	#Escribe primero 
        textoM = TextMobject("Texto relativo.")
        textoC = TextMobject("Texto de referencia.")
        textoC.move_to(1*UP+1*RIGHT)
        textoM.next_to(textoC,LEFT,buff=1) #jugar con los valores de buff y posición
        self.play(Write(textoM),Write(textoC))
        self.wait(1)

class PosicionamientoTextoEspecial3v3(Scene): #usando next_to con to_edge
    def construct(self):
    	#Escribe primero 
        textoM = TextMobject("Texto relativo.")
        textoC = TextMobject("Texto de referencia.")
        textoC.to_edge(UP+RIGHT)
        textoM.next_to(textoC,DOWN,buff=1) #jugar con los valores de buff y posición
        self.play(Write(textoM),Write(textoC))
        self.wait(1)

class Fonts(Scene):
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

class TamanhosPersonalizados(Scene):
	def construct(self):
		texto = TextMobject("{\\fontsize{60}{70}\\selectfont Texto.}")
		self.play(Write(texto))
		self.wait(3)

class TextoColores(Scene):
	def construct(self):
		texto = TextMobject("{\\color{red} Rojo}")
		self.play(Write(texto))
		self.wait(3)
