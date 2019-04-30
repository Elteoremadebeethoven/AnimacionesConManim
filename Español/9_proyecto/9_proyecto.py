from big_ol_pile_of_manim_imports import *
from tutorial.formulas_txt.formulas import formulas
#Inicia parametros -----------------------------------------

class DespejeEcuacion2doGrado(Scene):
	def construct(self):
		self.importar_formulas()
		self.imprime_formula()
		self.configurar_cambios()
		self.conversion_formulas(n_paso=1,
			cambios=self.conjunto_cambios[0],
			fade=[10],
			arco=-PI/2
			)
		self.conversion_formulas(n_paso=2,
			cambios=self.conjunto_cambios[1],
			write=[6,14],
			pre_copias=[0],
			pos_copias=[15]
			)
		self.conversion_formulas(n_paso=3,
			cambios=self.conjunto_cambios[2],
			pos_write=[10,	11,	13,	14,	15,	16,	18,	20,	28,	29,	31,	32,	33,	34,	36,	38],
			)
		self.conversion_formulas(n_paso=4,
			cambios=self.conjunto_cambios[3],
			)
		self.conversion_formulas(n_paso=5,
			cambios=self.conjunto_cambios[4],
			fade=[20,27],
			pre_copias=[29],
			pos_copias=[28]
			)
		self.conversion_formulas(n_paso=6,
			cambios=self.conjunto_cambios[5],
			fade=[19],
			)
		self.conversion_formulas(n_paso=7,
			cambios=self.conjunto_cambios[6],
			pos_write=[25,28],
			)
		self.conversion_formulas(n_paso=8,
			cambios=self.conjunto_cambios[7],
			pos_write=[32,26],
			)
		self.conversion_formulas(n_paso=9,
			cambios=self.conjunto_cambios[8],
			)
		self.conversion_formulas(n_paso=10,
			cambios=self.conjunto_cambios[9],
			pos_write=[0,	1,	16,	18,	20],
			)
		self.conversion_formulas(n_paso=11,
			cambios=self.conjunto_cambios[10],
			fade=[0,	1,	2,	12,	14]
			)
		self.conversion_formulas(n_paso=12,
			cambios=self.conjunto_cambios[11],
			)
		self.conversion_formulas(n_paso=13,
			cambios=self.conjunto_cambios[12],
			fade=[25]
			)
		self.conversion_formulas(n_paso=14,
			cambios=self.conjunto_cambios[13],
			)
		#
		c1=SurroundingRectangle(self.formulas[14],buff=0.2)
		c2=SurroundingRectangle(self.formulas[14],buff=0.2)
		c2.rotate(PI)
		self.play(ShowCreationThenDestruction(c1),ShowCreationThenDestruction(c2))
		self.wait(2)

	def importar_formulas(self):
		self.formulas=formulas


	def imprime_formula(self):
		self.play(Write(self.formulas[0]))

	def configurar_cambios(self):
		self.conjunto_cambios=[
		#1
		[[
						(	0,	1,	3,	4,	5,	6,	7,	8,	9	),
						(	0,	1,	3,	4,	5,	6,	8,	9,	7	)
		]],
		#2
		[[
						(	0,		1,	3,	4,	5,	6,	7,	8,	9	),
						(	7,		0,	2,	3,	5,	9,	10,	11,	13	)
		]],
		#3
		[[
			(	0,	2,	3,	5,	6,	7,	9,	10,	11,	13,	14,	15	),
			(	0,	2,	3,	5,	6,	7,	9,	21,	22,	24,	25,	26	)
		]],
		#4
		[[
				(	0,	2,	10,	11,	13,	14,	15,	16,	18,	20,	21,	22,	24,	25,	26,	28,	29,	31,	32,	33,	34,	36,	38	,5,6,7,9,3),
				(	1,	11,	2,	0,	4,	5,	6,	7,	9,	11,	12,	13,	15,	16,	17,	19,	20,	22,	23,	24,	25,	27,	29	,4,5,7,1,2)
		]],
		#5
		[[
		(	0,	1,	2,	4,	5,	6,	7,	9,	11,	12,	13,	15,	16,	17,	19,	22,	23,	24,	25,	29),
		(	0,	1,	2,	4,	5,	6,	7,	9,	11,	12,	13,	15,	16,	17,	19,	21,	24,	25,	26,	23)
		]],
		#6
		[[
			(	0,	1,	2,	4,	5,	6,	7,	9,	11,	12,	13,	15,	16,	17,	21,	23,	24,	25,	26,	28	),
			(	0,	1,	2,	4,	5,	6,	7,	9,	11,	12,	23,	25,	26,	27,	14,	16,	17,	18,	19,	21	)
		]],
		#7
		[[
			(	0,	1,	2,		4,	5,	6,	7,		9,		11,	12,		14,		16,	17,	18,	19,		21,		23,		25,	26,	27	),
			(	0,	1,	2,		4,	5,	6,	7,		9,		11,	12,		14,		16,	17,	18,	19,		21,		23,		26,	27,	29	)
		]],
		#8
		[[
			(	0,	1,	2,		4,	5,	6,	7,		9,		11,	12,		14,		16,	17,	18,	19,		21,		23,		25,	26,	27,	28,	29,	),
			(	0,	1,	2,		4,	5,	6,	7,		9,		11,	12,		14,		16,	17,	18,	19,		21,		23,		25,	27,	28,	29,	30,	)
		]],
		#9
		[[
			(	0,	1,	2,		4,	5,	6,	7,		9,		11,	12,		14,		16,	17,	18,	19,		21,		23,		25,	26,	27,	28,	29,	30,		32,	),
			(	0,	1,	2,		4,	5,	6,	7,		9,		11,	12,		14,		16,	21,	22,	23,		25,		17,		18,	19,	20,	21,	22,	23,		25,	)
		]],
		#10
		[[
			(	0,	1,	2,		4,	5,	6,	7,		9,		11,	12,		14,		16,	17,	18,	19,	20,	21,	22,	23,		25,	),
			(	2,	3,	5,		6,	7,	8,	10,		12,		14,	15,		21,		22,	23,	24,	25,	26,	27,	30,	31,		32,	)
		]],
		#11
		[[
			(				3,		5,	6,	7,	8,		10,					15,	16,		18,		20,	21,	22,	23,	24,	25,	26,	27,			30,	31,	32,	),
			(				0,		1,	3,	4,	5,		6,					8,	9,		10,		12,	14,	15,	16,	17,	18,	19,	20,			21,	24,	25,	)
		]],
		#12
		[[
			(	0,	1,		3,	4,	5,	6,		8,	9,	10,		12,		14,	15,	16,	17,	18,	19,	20,	21,			24,	25,	),
			(	0,	2,		4,	5,	6,	7,		1,	9,	10,		12,		14,	15,	16,	17,	18,	19,	20,	21,			24,	25,	)
		]],
		#13
		[[
			(	0,	1,	2,		4,	5,	6,	7,		9,	10,		12,		14,	15,	16,	17,	18,	19,	20,	21,			24,	),
			(	0,	1,	2,		4,	5,	6,	7,		9,	11,		12,		14,	15,	16,	17,	18,	20,	21,	22,			23,	)
		]],
		#14
		[[
			(	0,	1,	2,		4,	5,	6,	7,		9,		11,	12,		14,	15,	16,	17,	18,		20,	21,	22,	23,	),
			(	0,	1,	3,		4,	16,	17,	18,		5,		6,	7,		9,	10,	11,	12,	13,		15,	16,	17,	18,	)
		]]
		]

	def conversion_formulas(self,
							pre_write=[],
							pos_write=[],
							pre_fade=[],
							pos_fade=[],
							fade=[],
							write=[],
							cambios=[[]],
							arco=0,
							n_paso=0,
							pre_copias=[],
							pos_copias=[],
							tiempo_pre_cambios=0.3,
							tiempo_cambios_final=0.3,
							run_time=2,
							tiempo_final=0.3,
							pre_orden=["w","f"],
							pos_orden=["w","f"]
							):
		formula_copia=[]
		for c in pre_copias:
			formula_copia.append(self.formulas[n_paso-1][c].copy())

		for ani_ in pre_orden:
			if len(pre_write)>0 and ani_=="w":
				self.play(*[Write(self.formulas[n_paso-1][w])for w in pre_write])
			if len(pre_fade)>0 and ani_=="f":
				self.play(*[FadeOut(self.formulas[n_paso-1][w])for w in pre_fade])

		self.wait(tiempo_pre_cambios)

		for pre_ind,post_ind in cambios:
			self.play(*[
				ReplacementTransform(
					self.formulas[n_paso-1][i],self.formulas[n_paso][j],
					path_arc=arco
					)
				for i,j in zip(pre_ind,post_ind)
				],
				*[FadeOut(self.formulas[n_paso-1][f])for f in fade if len(fade)>0],
				*[Write(self.formulas[n_paso][w])for w in write if len(write)>0],
				*[ReplacementTransform(formula_copia[j],self.formulas[n_paso][f])
				for j,f in zip(range(len(pos_copias)),pos_copias) if len(pre_copias)>0
				],
				run_time=run_time
			)

		self.wait(tiempo_cambios_final)

		for ani_ in pos_orden:
			if len(pos_write)>0 and ani_=="w":
				self.play(*[Write(self.formulas[n_paso][w])for w in pos_write])
			if len(pos_fade)>0 and ani_=="f":
				self.play(*[FadeOut(self.formulas[n_paso][w])for w in pos_fade])

		self.wait(tiempo_final)
