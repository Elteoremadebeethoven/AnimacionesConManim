from big_ol_pile_of_manim_imports import *

class EfectoAparicionTexto4(Scene):
    def construct(self):
        texto = VGroup(*map(TextMobject, [
            "Solo texto o fórmulas.",
        ]))
        for letra in texto:
            self.play(LaggedStart(FadeIn, letra, run_time = 2))
        self.wait()

class EfectoAparicionTexto5(Scene):
    def construct(self):
        texto = VGroup(*map(TextMobject, [
            "Solo texto o fórmulas.",
        ]))
        for letra in texto:
            self.play(LaggedStart(GrowFromCenter, letra, run_time = 2))
        self.wait()

class EfectoAparicionTexto6(Scene):
    def construct(self):
        texto = VGroup(*map(TextMobject, [
            "Solo texto o fórmulas.",
        ]))
        self.wait(0.3)
        for letra in texto:
            self.play(LaggedStart(FadeIn, 
                letra, run_time = 0.1*len(letra),
                lag_ratio=0.5/len(letra)))
            self.wait(0.1)
        self.wait()

class ResaltadoV1(Scene): 
    def construct(self):
        texto = TexMobject("\\lim_{","x","\\to","\\infty}","{1","\\over","x}","=","0")
        self.play(Write(texto))
        self.wait(0.5)
        self.play(
                texto[0].set_color, YELLOW,
                texto[0].scale_in_place, 1.2,
                rate_func = there_and_back,
            )
        self.wait(3)

class ResaltadoV2(Scene): 
    def construct(self):
        texto = TexMobject("\\lim_{","x","\\to","\\infty}","{1","\\over","x}","=","0")
        self.play(Write(texto))
        self.wait(0.5)
        for i in [0,8]:
            self.play(
                    texto[i].set_color, YELLOW,
                    texto[i].scale_in_place, 1.2,
                    rate_func = there_and_back,
                )
        self.wait(3)

class ResaltadoV3(Scene): 
    def construct(self):
        texto = TexMobject("\\lim_{","x","\\to","\\infty}","{1","\\over","x}","=","0")
        self.play(Write(texto))
        self.wait(0.5)
        self.play(
                texto[0].set_color, YELLOW,
                texto[0].scale_in_place, 1.2,
                run_time =0.3
            )
        self.wait(2)
        self.play(
                texto[0].set_color, WHITE,
                texto[0].scale_in_place, 1/1.2,
                run_time =0.3
            )
        self.wait(3)

class ResaltadoV4(Scene): 
    def construct(self):
        texto = TexMobject("\\lim_{","x","\\to","\\infty}","{1","\\over","x}","=","0")
        self.play(Write(texto))
        self.wait(0.5)
        self.play(
                texto[0].set_color, YELLOW,
                texto[0].scale_in_place, 1.2,
                texto[3].set_color, YELLOW,
                texto[3].scale_in_place, 1.2,
                texto[7].set_color, YELLOW,
                texto[7].scale_in_place, 1.2,
                rate_func = there_and_back,
            )
        self.wait(3)

class ResaltadoV5(Scene): 
    def construct(self):
        texto = TexMobject("\\lim_{","x","\\to","\\infty}","{1","\\over","x}","=","0")
        self.play(Write(texto))
        self.wait(0.5)
        for i,j,k,l,m in [(0,3,4,4,4),(5,3,3,3,3),(0,2,4,6,8)]:
            self.play(
                    texto[i].set_color, YELLOW,
                    texto[i].scale_in_place, 1.2,
                    texto[j].set_color, YELLOW,
                    texto[j].scale_in_place, 1.2,
                    texto[k].set_color, YELLOW,
                    texto[k].scale_in_place, 1.2,
                    texto[l].set_color, YELLOW,
                    texto[l].scale_in_place, 1.2,
                    texto[m].set_color, YELLOW,
                    texto[m].scale_in_place, 1.2,
                    run_time =0.3
                )
            self.wait(2)
            self.play(
                    texto[i].set_color, WHITE,
                    texto[i].scale_in_place, 1/1.2,
                    texto[j].set_color, WHITE,
                    texto[j].scale_in_place, 1/1.2,
                    texto[k].set_color, WHITE,
                    texto[k].scale_in_place, 1/1.2,
                    texto[l].set_color, WHITE,
                    texto[l].scale_in_place, 1/1.2,
                    texto[m].set_color, WHITE,
                    texto[m].scale_in_place, 1/1.2,
                    run_time =0.3
                )
        self.wait(3)