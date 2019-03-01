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
<p align="center"><img src ="/Español/extras/aprender_manim_cuenta_propia_v1/capturas/coord_syst.png" width="700" /></p>

## Modificar búsqueda de imágenes:
### Descarga las siguientes imágenes
#### Imagen genérica .png a ```media/designs/raster_images```

<p align="center"><img src ="/Español/extras/aprender_manim_cuenta_propia_v1/archivos/generic.png" width="400" /></p>

#### Imagen genérica .svg a ```media/designs/svg_images```

<p align="center"><img src ="/Español/extras/aprender_manim_cuenta_propia_v1/archivos/generic.svg" width="400" /></p>

Después mueve los tres archivos .svg de ```manimlib/files``` a ```media/designs/svg_images```

#### Añade la siguiente linea en ```manimlib/mobject/svg/svg_mobject.py```

```python3
            os.path.join(SVG_IMAGE_DIR, "generic.svg")
```

<p align="center"><img src ="/Español/extras/aprender_manim_cuenta_propia_v1/capturas/capt2.png" width="700" /></p>
