import tkinter as tk
import numpy as np
from .mapa import Mapa

class Interfaz(tk.Tk):
    with open ("resources/maps/prueba.txt", "r") as file:
        lineas = file.readlines()
        matriz = np.array([list(map(int, linea.strip().split()))for linea in lineas])

    def __init__(self):
        super().__init__()
        self.title("El taxista")
        self.geometry("900x600")
        self.config(bg="white")

        self.canvas = tk.Canvas(self, width=900, height=600, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.mapa = Mapa(self.canvas)

        
