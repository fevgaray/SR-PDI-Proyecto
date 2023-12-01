# SR-PDI-Proyecto: Copboy Bepop

## Instrucciones de Uso:
Elegir el ambiente preferido donde se trabaja con python y multiples libraries.
Pasos a seguir para instalacion de paquetes necesarios:
- create anaconda env with python 3.9
- install tensorflow with pip
- install scipy, numpy, pillow, imageio, and scikit-image with pip
- if it throws error it might get solved by uninstalling numpy and installing again with pip

Una vez listo el environment, se puede ejecutar super resolution a traves del notebook "SR.ipynb".

## Carpetas de Interes:
- "ImagesHR": Carpeta donde se colocan las imágenes que se les realiza downsampling para despues validar las imagenes procesadas.
- "ImagesLR": Carpeta donde se ubican las imágenes input que se le dan al modelo, también es la carpeta donde salen los resultados del downsampling.
- "dcscn-super-resolution-master/outpu": Carpeta donde se ubican los resultados del super resolution para cada escala.

## Extra:
- "downsampling.ipynb": Notebook utilizado para aplicar multiples metodos de downsampling a nuestros datasets para despues validar nuestros resultados.
