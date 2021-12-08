"""
EN este ejemplo se muestra la creacion de una clase con atricutos 
un metodo que utiliza la libreria matplotlib para dibujar
un circulo.

Este archivo fue creado con VSCode usando plugin Python de microsoft.
Formato realizado con black.
VSCode iniciado desde anaconda:
    conda activate env_practica
    code
"""
import matplotlib.pyplot as plt

# la linea anterior es el metodo usual para importar
# la libreria usada para crear graficos


class circulo(object):
    def __init__(self, radio=1, color="m"):
        self.color = color
        self.radio = radio

    def plot_circulo(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radio, fc=self.color))
        plt.axis("scaled")
        plt.show()


circulo_azul = circulo(10, "b")
circulo_azul.plot_circulo()

