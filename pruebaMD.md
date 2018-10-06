```python3
class GraficaSenoCoseno2(GraphScene):
    CONFIG = {
        "y_max" : 1.5,
        "y_min" : -1.5,
        "x_max" : 3*PI/2,
        "x_min" : -3*PI/2,
        "y_tick_frequency" : 0.5,
        "x_tick_frequency" : PI/2,
        "graph_origin" : ORIGIN,
        "y_axis_label": None, #No escribe etiqueta de y
        "x_axis_label": None, #No escribe etiqueta de x
    }
    def construct(self):
        self.setup_axes()
        graficaSeno = self.get_graph(lambda x : np.sin(x), 
                                    color = GREEN,
                                    x_min=-4,
                                    x_max=4,
                                )
        graficaCoseno = self.get_graph(lambda x : np.cos(x), 
                                    color = GRAY,
                                    x_min=-PI,
                                    x_max=0,
                                )
        graficaSeno.set_stroke(width=3) # Grosor de linea
        graficaCoseno.set_stroke(width=2)
        # Anima las dos juntas
        self.play(*[
                ShowCreation(grafica)
                for grafica in (
                        graficaSeno,
                        graficaCoseno,
                        )
            ],
            run_time = 2)

    def setup_axes(self):
        GraphScene.setup_axes(self)
        #Grosor de ejes
        self.x_axis.set_stroke(width=2)
        self.y_axis.set_stroke(width=2)
        #Color de ejes
        self.x_axis.set_color(RED)
        self.y_axis.set_color(YELLOW)
        #Modificar posición de etiquetas x,y
        func = TexMobject("\\mbox{sen}\\theta")
        var = TexMobject("\\theta")
        func.set_color(BLUE)
        var.set_color(PURPLE)
        func.next_to(self.y_axis,UP)
        var.next_to(self.x_axis,RIGHT+UP)
        #Etiquetas del eje y
        self.y_axis.label_direction = LEFT*1.5
        self.y_axis.add_numbers(*[-1,1])
        #Parámetros de valores de posiciones en x
        valor_en_x = -3*PI/2
        pasos_x = PI/2
        valor_fin_x = 3*PI/2
        #Lista de valores de posiciones de x
        valor_decimal_x=list(np.arange(valor_en_x,valor_fin_x+pasos_x,pasos_x))
        #Lista de valores TexMobject de etiquetas en x
        lista_x=TexMobject("-\\frac{3\\pi}{2}", #   -3pi/2
                            "-\\pi", #              -pi 
                            "-\\frac{\\pi}{2}", #   -pi/2
                            "\\,", #                 0 (espacio)
                            "\\frac{\\pi}{2}", #     pi/2
                            "\\pi",#                 pi
                            "\\frac{3\\pi}{2}" #     3pi/2
                          )
        #Lista de (posición,etiqueta)
        valores_x = [(i,j)
            for i,j in zip(valor_decimal_x,lista_x)
        ]
        self.x_axis_labels = VGroup()
        for x_val, x_tex in valores_x:
            x_tex.scale(0.7) #No es necesario usar variable tex
            if x_val == -PI or x_val == PI: #si x es igual a -pi o pi
                x_tex.next_to(self.coords_to_point(x_val, 0), 2*DOWN) #coloca más abajo
            else: # Si eso no ocurre...
                x_tex.next_to(self.coords_to_point(x_val, 0), DOWN)
            self.x_axis_labels.add(x_tex)
        #Anima la aparición del conjunto
        self.play(*[Write(objeto)
            for objeto in [
                    self.y_axis,
                    self.x_axis,
                    self.x_axis_labels,
                    func,var
                ]
            ],
            run_time=2
        )
```
