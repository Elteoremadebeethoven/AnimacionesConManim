# Transformaciones y copiado de texto
## Programas
### 
```python3
class TransformacionTexto1v1(Scene):
	def construct(self):
		texto1 = TextMobject("Primer texto")
		texto2 = TextMobject("Segundo texto")
		self.play(Write(texto1))
		self.wait()
		self.play(Transform(texto1,texto2))
		self.wait()
```
<p align="center"><img src ="/Español/3_transformaciones_texto/gifs/TransformacionTexto1v1.gif" /></p>

### 
```python3
class TransformacionTexto1v2(Scene):
	def construct(self):
		texto1 = TextMobject("Primer texto")
		texto1.to_edge(UP)
		texto2 = TextMobject("Segundo texto")
		self.play(Write(texto1))
		self.wait()
		self.play(Transform(texto1,texto2))
		self.wait()
```
<p align="center"><img src ="/Español/3_transformaciones_texto/gifs/TransformacionTexto1v2.gif" /></p>

### 
```python3
class TransformacionTexto2(Scene):
	def construct(self):
		texto1 = TextMobject("Función")
		texto2 = TextMobject("Derivada")
		texto3 = TextMobject("Integral")
		texto4 = TextMobject("Transformada")
		self.play(Write(texto1))
		self.wait()
		#Trans texto1 -> texto2
		self.play(ReplacementTransform(texto1,texto2))
		self.wait()
		#Trans texto2 -> texto3
		self.play(ReplacementTransform(texto2,texto3))
		self.wait()
		#Trans texto3 -> texto4
		self.play(ReplacementTransform(texto3,texto4))
		self.wait()
```
<p align="center"><img src ="/Español/3_transformaciones_texto/gifs/TransformacionTexto2.gif" /></p>

### 
```python3
class CopiadoTextoV1(Scene):
	def construct(self):
		formula = TexMobject("\\frac{d}{dx}",
			"(","u","+","v",")","=",
			"\\frac{d}{dx}","u","+","\\frac{d}{dx}","v"
			)
		formula.scale(2)
		self.play(Write(formula[0:7]))
		self.wait()
		self.play(
			ReplacementTransform(formula[2].copy(),formula[8]),
			ReplacementTransform(formula[4].copy(),formula[11]),
			ReplacementTransform(formula[3].copy(),formula[9])
			)
		self.wait()
		self.play(
			ReplacementTransform(formula[0].copy(),formula[7]),
			ReplacementTransform(formula[0].copy(),formula[10])
			)
		self.wait()
```
<p align="center"><img src ="/Español/3_transformaciones_texto/gifs/CopiadoTextoV1.gif" /></p>

### 
```python3
class CopiadoTextoV2(Scene):
	def construct(self):
		formula = TexMobject("\\frac{d}{dx}",
			"(","u","+","v",")","=",
			"\\frac{d}{dx}","u","+","\\frac{d}{dx}","v"
			)
		formula.scale(2)
		self.play(Write(formula[0:7]))
		self.wait()
		self.play(
			ReplacementTransform(formula[2].copy(),formula[8]),
			ReplacementTransform(formula[4].copy(),formula[11]),
			ReplacementTransform(formula[3].copy(),formula[9]),
			run_time=3
			)
		self.wait()
		self.play(
			ReplacementTransform(formula[0].copy(),formula[7]),
			ReplacementTransform(formula[0].copy(),formula[10]),
			run_time=3
			)
		self.wait()
```
<p align="center"><img src ="/Español/3_transformaciones_texto/gifs/CopiadoTextoV2.gif" /></p>

### 
```python3
class CopiadoTextoV3(Scene):
	def construct(self):
		formula = TexMobject("\\frac{d}{dx}",
			"(","u","+","v",")","=",
			"\\frac{d}{dx}","u","+","\\frac{d}{dx}","v"
			)
		formula.scale(2)
		formula[8].set_color(RED)
		formula[11].set_color(BLUE)
		self.play(Write(formula[0:7]))
		self.wait()
		self.play(
			ReplacementTransform(formula[2].copy(),formula[8]),
			ReplacementTransform(formula[4].copy(),formula[11]),
			ReplacementTransform(formula[3].copy(),formula[9]),
			run_time=3
			)
		self.wait()
		self.play(
			ReplacementTransform(formula[0].copy(),formula[7]),
			ReplacementTransform(formula[0].copy(),formula[10]),
			run_time=3
			)
		self.wait()
```
<p align="center"><img src ="/Español/3_transformaciones_texto/gifs/CopiadoTextoV3.gif" /></p>

### 
```python3
class CopiadoTextoV4(Scene):
	def construct(self):
		formula = TexMobject("\\frac{d}{dx}",
			"(","u","+","v",")","=",
			"\\frac{d}{dx}","u","+","\\frac{d}{dx}","v"
			)
		formula.scale(2)
		for letra,color in [("u",RED),("v",BLUE)]:
			formula.set_color_by_tex(letra,color)
		self.play(Write(formula[0:7]))
		self.wait()
		self.play(
			ReplacementTransform(formula[2].copy(),formula[8]),
			ReplacementTransform(formula[4].copy(),formula[11]),
			ReplacementTransform(formula[3].copy(),formula[9]),
			run_time=3
			)
		self.wait()
		self.play(
			ReplacementTransform(formula[0].copy(),formula[7]),
			ReplacementTransform(formula[0].copy(),formula[10]),
			run_time=3
			)
		self.wait()
```
<p align="center"><img src ="/Español/3_transformaciones_texto/gifs/CopiadoTextoV4.gif" /></p>

### 
```python3
class CopiadoDosFormulas1(Scene):
	def construct(self):
		formula1 = TexMobject(
				"\\neg","\\forall","x",":","P(x)"
			)
		formula2 = TexMobject(
				"\\exists","x",":","\\neg","P(x)"
			)
		for tam,pos,formula in [(2,2*UP,formula1),(2,2*DOWN,formula2)]:
			formula.scale(tam)
			formula.move_to(pos)
		self.play(Write(formula1))
		self.wait()
		cambios = [
			[(0,1,2,3,4),(3,0,1,2,4)],
		]
		for pre_ind,post_ind in cambios:
			self.play(*[
				ReplacementTransform(
					formula1[i].copy(),formula2[j]
					)
				for i,j in zip(pre_ind,post_ind)
				],
				run_time=2
			)
			self.wait()
```
<p align="center"><img src ="/Español/3_transformaciones_texto/gifs/CopiadoDosFormulas1.gif" /></p>

### 
```python3
class CopiadoDosFormulas2(Scene):
	def construct(self):
		formula1 = TexMobject(
				"\\neg","\\forall","x",":","P(x)"
			)
		formula2 = TexMobject(
				"\\exists","x",":","\\neg","P(x)"
			)
		for tam,pos,formula in [(2,2*UP,formula1),(2,2*DOWN,formula2)]:
			formula.scale(tam)
			formula.move_to(pos)
		self.play(Write(formula1))
		self.wait()
		cambios = [
			[(2,3,4),(1,2,4)],
			[(0,),(3,)],
			[(1,),(0,)]
		]
		for pre_ind,post_ind in cambios:
			self.play(*[
				ReplacementTransform(
					formula1[i].copy(),formula2[j]
					)
				for i,j in zip(pre_ind,post_ind)
				],
				run_time=2
			)
			self.wait()
```
<p align="center"><img src ="/Español/3_transformaciones_texto/gifs/CopiadoDosFormulas2.gif" /></p>

### 
```python3
class CopiadoDosFormulas2Color(Scene):
	def construct(self):
		formula1 = TexMobject(
				"\\neg","\\forall","x",":","P(x)"
			)
		formula2 = TexMobject(
				"\\exists","x",":","\\neg","P(x)"
			)
		parametros = [(2,2*UP,formula1,GREEN,"\\forall"),
					  (2,2*DOWN,formula2,ORANGE,"\\exists")]
		for tam,pos,formula,col,sim in parametros:
			formula.scale(tam)
			formula.move_to(pos)
			formula.set_color_by_tex(sim,col)
			formula.set_color_by_tex("\\neg",PINK)
		self.play(Write(formula1))
		self.wait()
		cambios = [
			[(2,3,4),(1,2,4)],
			[(0,),(3,)],
			[(1,),(0,)]
		]
		for pre_ind,post_ind in cambios:
			self.play(*[
				ReplacementTransform(
					formula1[i].copy(),formula2[j]
					)
				for i,j in zip(pre_ind,post_ind)
				],
				run_time=2
			)
			self.wait()
```
<p align="center"><img src ="/Español/3_transformaciones_texto/gifs/CopiadoDosFormulas2Color.gif" /></p>

### 
```python3
class CopiadoDosFormulas3(Scene):
	def construct(self):
		formula1 = TexMobject(
				"\\neg","\\forall","x",":","P(x)"
			)
		formula2 = TexMobject(
				"\\exists","x",":","\\neg","P(x)"
			)
		parametros = [(2,2*UP,formula1,GREEN,"\\forall"),
					  (2,2*DOWN,formula2,ORANGE,"\\exists")]
		for tam,pos,formula,col,sim in parametros:
			formula.scale(tam)
			formula.move_to(pos)
			formula.set_color_by_tex(sim,col)
			formula.set_color_by_tex("\\neg",PINK)
		self.play(Write(formula1))
		self.wait()
		cambios = [
			[(2,3,4),(1,2,4)],
			[(0,),(3,)],
			[(1,),(0,)]
		]
		for pre_ind,post_ind in cambios:
			self.play(*[
				ReplacementTransform(
					formula1[i],formula2[j]
					)
				for i,j in zip(pre_ind,post_ind)
				],
				run_time=2
			)
			self.wait()
```
<p align="center"><img src ="/Español/3_transformaciones_texto/gifs/CopiadoDosFormulas3.gif" /></p>

### 
```python3
class CambioColorTexto(Scene):
	def construct(self):
		texto = TextMobject("Texto")
		texto.scale(3)
		self.play(Write(texto))
		self.wait()
		self.play(
                texto.set_color, YELLOW,
                run_time=2
            )
		self.wait()
```
<p align="center"><img src ="/Español/3_transformaciones_texto/gifs/CambioColorTexto.gif" /></p>

### 
```python3
class AnimacionTamanho(Scene):
	def construct(self):
		texto = TextMobject("Texto")
		texto.scale(2)
		self.play(Write(texto))
		self.wait()
		self.play(
                texto.scale, 3,
                run_time=2
            )
		self.wait()
```
<p align="center"><img src ="/Español/3_transformaciones_texto/gifs/AnimacionTamanho.gif" /></p>

### 
```python3
class MovimientoTexto(Scene):
	def construct(self):
		texto = TextMobject("Texto")
		texto.scale(2)
		texto.move_to(LEFT*2)
		self.play(Write(texto))
		self.wait()
		self.play(
                texto.move_to, RIGHT*2,
                run_time=2,
                path_arc=0 #Sustituir 0 por otro valor, -np.pi
            )
		self.wait()
```
<p align="center"><img src ="/Español/3_transformaciones_texto/gifs/MovimientoTexto.gif" /></p>

### 
```python3
class CambioPosicionTamanhoColorTexto(Scene):
	def construct(self):
		texto = TextMobject("Texto")
		texto.scale(2)
		texto.move_to(LEFT*2)
		self.play(Write(texto))
		self.wait()
		self.play(
                texto.move_to, RIGHT*2,
                texto.scale, 2,
                texto.set_color, RED,
                run_time=2,
            )
		self.wait()
```
<p align="center"><img src ="/Español/3_transformaciones_texto/gifs/CambioPosicionTamanhoColorTexto.gif" /></p>
