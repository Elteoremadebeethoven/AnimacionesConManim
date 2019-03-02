from big_ol_pile_of_manim_imports import *

class CompartirVariables(Scene):
    def construct(self):
        self.paso1()
        self.paso2()
        self.paso3()
        x,y=self.get_attrs("x","y")
        x+=1
        y+=1
        print("En construct: x= %s, y= %s,z= %s"%(x,y,self.z))

    def paso1(self):
        x=9.5
        y=8.7
        self.set_variables_as_attrs(x,y)
        print("En paso 1: x= %s, y= %s"%(x,y))

    def paso2(self):
        x,y=self.get_attrs("x","y")
        x+=1
        y+=1
        self.z=3
        print("En paso 2: x= %s, y= %s"%(x,y))
        self.set_variables_as_attrs(x,y)

    def paso3(self):
        x,y=self.get_attrs("x","y")
        x+=1
        self.x=self.x*(-1)
        y+=1
        self.set_variables_as_attrs(x,y)                                # Jugar
        print("En paso 3: x= %s, y= %s, self.x= %s"%(x,y,self.x))       # con las posiciones de estas dos lineas