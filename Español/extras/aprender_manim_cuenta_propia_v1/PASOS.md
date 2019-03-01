# Cómo aprender Manim por cuenta propia.
Este tutorial funciona con la versión de [manim del 3 de Febrero del 2019](https://github.com/3b1b/manim/tree/3b088b12843b7a4459fe71eba96b70edafb7aa78). 
## Modificar los siguientes archivos:
En ```manimlib/mobject/coordinate_systems.py``` agregar en la linea 54.

```python3
    def get_axis(self, min_val, max_val, axis_config):
        new_config = merge_config([
            axis_config,
            {"x_min": min_val, "x_max": max_val},
            self.number_line_config,
        ])
        return NumberLine(**new_config)
```
<p align="center"><img src ="/Español/extras/aprender_manim_cuenta_propia_v1/capturas/coord_syst.png" width="400" /></p>
