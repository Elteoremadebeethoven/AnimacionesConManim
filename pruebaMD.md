# Gráficas en GraphScene
## Programas
### Gráfica 1
```python3
class Grafica1(GraphScene):
    CONFIG = {
        "y_max" : 50,
        "y_min" : 0,
        "x_max" : 7,
        "x_min" : 0,
        "y_tick_frequency" : 5, #Subdivisiones de y
        "x_tick_frequency" : 1, #Subdivisiones de x
        "axes_color" : BLUE, #Color de los ejes XY
    }
    def construct(self):
        self.setup_axes(animate=True) #animate=True para animar al mostrar los ejes
        #Definición de gráfica
        grafica = self.get_graph(lambda x : x**2, # Función en numpy 
                                    color = GREEN,
                                    x_min = 2, # Dominio
                                    x_max = 4
                                    )
        #Animar creación de gráfica
        self.play(
        	ShowCreation(grafica),
            run_time = 2
        )
        self.wait()
```
<p align="center"><img src ="/Grafica1.gif" /></p>

### Gráfica 1 versión 2
```python3
class Grafica1v2(GraphScene):
    CONFIG = {
        "y_max" : 50,
        "y_min" : 0,
        "x_max" : 7,
        "x_min" : 0,
        "y_tick_frequency" : 5,
        "x_tick_frequency" : 1,
        "axes_color" : BLUE, #     x y z
        "graph_origin" : np.array((0,0,0)) # Origen de la gráfica, se puede usar LEFT,...
    }
    def construct(self):
        self.setup_axes(animate=True)
        grafica = self.get_graph(lambda x : x**2, 
                                    color = GREEN,
                                    x_min = 2, 
                                    x_max = 4
                                    )
        self.play(
            ShowCreation(grafica),
            run_time = 2
        )
        self.wait()
```

<p align="center"><img src ="/Grafica2.gif" /></p>

<p align="center"><img src ="/TextoWrite.gif" /></p>
