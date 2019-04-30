from big_ol_pile_of_manim_imports import *

#El simple cambio de Scene por ThreeDScene no parece tener ningun cambio
class PosicionCamara1(ThreeDScene):
    def construct(self):
        circulo=Circle()
        self.play(ShowCreation(circulo))
        self.wait()

'''
Hay que agregar:

    def get_axis(self, min_val, max_val, axis_config):
        new_config = merge_config([
            axis_config,
            {"x_min": min_val, "x_max": max_val},
            self.number_line_config,
        ])
        return NumberLine(**new_config)

en manimlib/mobject/coordinate_systems.py

Pero si se usa self.set_camera_orientation(phi,theta,distance,gamma) se nota la diferencia
Ademas de que se pueden usar los ejes en tres de con ThreeDAxes() donde se puede configurar:
ThreeDAxes(
    x_min.
    x_max,
    y_min,
    y_max,
    z_min,
    z_max
)
'''

class PosicionCamara2(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        circulo=Circle()
        self.set_camera_orientation(phi=0 * DEGREES)
        self.play(ShowCreation(circulo),ShowCreation(axes))
        self.wait()

class PosicionCamara3(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        circulo=Circle()
        self.set_camera_orientation(phi=80 * DEGREES,theta=45*DEGREES)
        self.play(ShowCreation(circulo),ShowCreation(axes))
        self.wait()

class PosicionCamara4(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        circulo=Circle()
        self.set_camera_orientation(phi=80 * DEGREES,theta=45*DEGREES,distance=6)
        self.play(ShowCreation(circulo),ShowCreation(axes))
        self.wait()

class PosicionCamara5(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        circulo=Circle()
        self.set_camera_orientation(phi=80 * DEGREES,theta=45*DEGREES,distance=6,gamma=30*DEGREES)
        self.play(ShowCreation(circulo),ShowCreation(axes))
        self.wait()

#------ Movimiento de camara

class MovimientoCamara1(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        circulo=Circle()
        self.play(ShowCreation(circulo),ShowCreation(axes))
        self.move_camera(phi=30*DEGREES,theta=-45*DEGREES,run_time=3)
        self.wait()

class MovimientoCamara2(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        circulo=Circle()
        self.set_camera_orientation(phi=80 * DEGREES)           #Configuras la camara a 80 grados
        self.play(ShowCreation(circulo),ShowCreation(axes))
        self.begin_ambient_camera_rotation(rate=0.1)            #Empizas a girar la camara de manera automatica
        self.wait(5)
        self.stop_ambient_camera_rotation()                     #Detienes el giro autimatico
        self.move_camera(phi=80*DEGREES,theta=-PI/2)            #Regresas a la posicion original
        self.wait()

#----------- Funciones parametricas


class CurvaParametrica1(ThreeDScene):
    def construct(self):
        curva1=ParametricFunction(
                lambda u : np.array([
                1.2*np.cos(u),
                1.2*np.sin(u),
                u/2
            ]),color=RED,t_min=-TAU,t_max=TAU,
            )
        curva2=ParametricFunction(
                lambda u : np.array([
                1.2*np.cos(u),
                1.2*np.sin(u),
                u
            ]),color=RED,t_min=-TAU,t_max=TAU,
            )
        axes = ThreeDAxes()

        self.add(axes)

        self.set_camera_orientation(phi=80 * DEGREES,theta=-60*DEGREES)
        self.begin_ambient_camera_rotation(rate=0.1) 
        self.play(ShowCreation(curva1))
        self.wait()
        self.play(Transform(curva1,curva2),rate_func=there_and_back,run_time=3)
        self.wait()

# La escena anterior da la sensacion de que la curva siempre se muestra sobre los ejes
# Para que la curva este por debajo se debe usar .set_shade_in_3d(True)

class CurvaParametrica2(ThreeDScene):
    def construct(self):
        curva1=ParametricFunction(
                lambda u : np.array([
                1.2*np.cos(u),
                1.2*np.sin(u),
                u/2
            ]),color=RED,t_min=-TAU,t_max=TAU,
            )
        curva2=ParametricFunction(
                lambda u : np.array([
                1.2*np.cos(u),
                1.2*np.sin(u),
                u
            ]),color=RED,t_min=-TAU,t_max=TAU,
            )

        curva1.set_shade_in_3d(True)
        curva2.set_shade_in_3d(True)

        axes = ThreeDAxes()

        self.add(axes)

        self.set_camera_orientation(phi=80 * DEGREES,theta=-60*DEGREES)
        self.begin_ambient_camera_rotation(rate=0.1) 
        self.play(ShowCreation(curva1))
        self.wait()
        self.play(Transform(curva1,curva2),rate_func=there_and_back,run_time=3)
        self.wait()


class CurvaParametrica2(ThreeDScene):
    def construct(self):
        curva1=ParametricFunction(
                lambda u : np.array([
                1.2*np.cos(u),
                1.2*np.sin(u),
                u/2
            ]),color=RED,t_min=-TAU,t_max=TAU,
            )
        curva2=ParametricFunction(
                lambda u : np.array([
                1.2*np.cos(u),
                1.2*np.sin(u),
                u
            ]),color=RED,t_min=-TAU,t_max=TAU,
            )

        curva1.set_shade_in_3d(True)
        curva2.set_shade_in_3d(True)

        axes = ThreeDAxes()

        self.add(axes)

        self.set_camera_orientation(phi=80 * DEGREES,theta=-60*DEGREES)
        self.begin_ambient_camera_rotation(rate=0.1) 
        self.play(ShowCreation(curva1))
        self.wait()
        self.play(Transform(curva1,curva2),rate_func=there_and_back,run_time=3)
        self.wait()

#----- Superficies
class Superficies(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        cilindro = ParametricSurface(
            lambda u, v: np.array([
                np.cos(TAU * v),
                np.sin(TAU * v),
                2 * (1 - u)
            ]),
            resolution=(6, 32)).fade(0.5) #Numero de cuadros de la superficie

        paraboloide = ParametricSurface(
            lambda u, v: np.array([
                np.cos(v)*u,
                np.sin(v)*u,
                u**2
            ]),v_max=TAU,
            checkerboard_colors=[PURPLE_D, PURPLE_E],
            resolution=(10, 32)).scale(2)

        hiper_para = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                u**2-v**2
            ]),v_min=-2,v_max=2,u_min=-2,u_max=2,checkerboard_colors=[BLUE_D, BLUE_E],
            resolution=(15, 32)).scale(1)

        cono = ParametricSurface(
            lambda u, v: np.array([
                u*np.cos(v),
                u*np.sin(v),
                u
            ]),v_min=0,v_max=TAU,u_min=-2,u_max=2,checkerboard_colors=[GREEN_D, GREEN_E],
            resolution=(15, 32)).scale(1)

        hip_una_hoja = ParametricSurface(
            lambda u, v: np.array([
                np.cosh(u)*np.cos(v),
                np.cosh(u)*np.sin(v),
                np.sinh(u)
            ]),v_min=0,v_max=TAU,u_min=-2,u_max=2,checkerboard_colors=[YELLOW_D, YELLOW_E],
            resolution=(15, 32))

        elipsoide=ParametricSurface(
            lambda u, v: np.array([
                1*np.cos(u)*np.cos(v),
                2*np.cos(u)*np.sin(v),
                0.5*np.sin(u)
            ]),v_min=0,v_max=TAU,u_min=-PI/2,u_max=PI/2,checkerboard_colors=[TEAL_D, TEAL_E],
            resolution=(15, 32)).scale(2)

        esfera = ParametricSurface(
            lambda u, v: np.array([
                1.5*np.cos(u)*np.cos(v),
                1.5*np.cos(u)*np.sin(v),
                1.5*np.sin(u)
            ]),v_min=0,v_max=TAU,u_min=-PI/2,u_max=PI/2,checkerboard_colors=[RED_D, RED_E],
            resolution=(15, 32)).scale(2)


        self.set_camera_orientation(phi=75 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.2)


        self.add(axes)
        self.play(Write(esfera))
        self.wait()
        self.play(ReplacementTransform(esfera,elipsoide))
        self.wait()
        self.play(ReplacementTransform(elipsoide,cono))
        self.wait()
        self.play(ReplacementTransform(cono,hip_una_hoja))
        self.wait()
        self.play(ReplacementTransform(hip_una_hoja,hiper_para))
        self.wait()
        self.play(ReplacementTransform(hiper_para,paraboloide))
        self.wait()
        self.play(ReplacementTransform(paraboloide,cilindro))
        self.wait()
        self.play(FadeOut(cilindro))

#---- Texto en 3D
class Texto3D1(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES,theta=-45*DEGREES)
        texto3d=TextMobject("Este es texto en 3D").scale(2)
        self.add(axes,texto3d)

# El texto por defecto siempre se escribe en el plano XY, se puede
# rotar si se quiere

class Texto3D2(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES,theta=-45*DEGREES)
        texto3d=TextMobject("Este es texto en 3D").scale(2).set_shade_in_3d(True) #quitar si se quiere .set_shade_in_3d(True)
        texto3d.rotate(PI/2,axis=RIGHT)
        self.add(axes,texto3d)

# Si queremos que el texto se muestre de forma tradicional con el fondo 3D entonces se usa:
class Texto3D3(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES,theta=-45*DEGREES)
        texto3d=TextMobject("Este es texto en 3D")

        self.add_fixed_in_frame_mobjects(texto3d) #Este es el metodo que hay que emplear
        texto3d.to_corner(UL)

        self.add(axes)
        self.begin_ambient_camera_rotation()
        self.play(Write(texto3d))

        esfera = ParametricSurface(
            lambda u, v: np.array([
                1.5*np.cos(u)*np.cos(v),
                1.5*np.cos(u)*np.sin(v),
                1.5*np.sin(u)
            ]),v_min=0,v_max=TAU,u_min=-PI/2,u_max=PI/2,checkerboard_colors=[RED_D, RED_E],
            resolution=(15, 32)).scale(2)

        self.play(LaggedStart(ShowCreation,esfera))
        self.wait(2)

# Jugar con shift, move_to, next_to, Line, Arrow, CurvedArrow, etc. Pero ahora en 3D


