import tkinter as tk
import numpy as np
from PIL import Image, ImageTk

class Mapa:
    def __init__(self, canvas):
        super().__init__()
        self.canvas = canvas
        self.matriz = self.cargar_matriz("resources/maps/prueba.txt")
        self.libre = 0
        self.muro = 1
        self.partidaVehiculo = 2
        self.traficoMedio = 3
        self.traficoPesado = 4
        self.pasajero = 5
        self.destino = 6
        self.imgVehiculo = ImageTk.PhotoImage(
        Image.open("resources/images/vehiculo.jpg").resize((90,60)))
        self.imgPasajero = ImageTk.PhotoImage(
        Image.open("resources/images/pasajero.jpg").resize((70,55)))

        self.dibujar_matriz()

    def cargar_matriz(self, ruta):
        global matriz
        # Cargar la matriz desde un archivo
        with open(ruta, "r") as archivo:
            lineas = archivo.readlines()
            return np.array([list(map(int, linea.strip().split())) for linea in lineas])
    

    def dibujar_matriz(self):
        #Dibujar la matriz en el canvas
        for i in range(self.matriz.shape[0]):
            for j in range(self.matriz.shape[1]):
                x = j * 90
                y = i * 60
            
                if self.matriz[i][j] == self.libre:
                    self.canvas.create_rectangle(x, y, x+90, y+60, fill="white")
                elif self.matriz[i][j] == self.muro:
                    self.canvas.create_rectangle(x, y, x+90, y+60, fill="gray")
                elif self.matriz[i][j] == self.partidaVehiculo:
                    self.canvas.create_image(x, y, image=self.imgVehiculo, anchor="nw")
                elif self.matriz[i][j] == self.traficoMedio:
                    self.canvas.create_rectangle(x, y, x+90, y+60, fill="green")
                elif self.matriz[i][j] == self.traficoPesado:
                    self.canvas.create_rectangle(x, y, x+90, y+60, fill="red")
                elif self.matriz[i][j] == self.pasajero:
                    self.canvas.create_image(x, y, image=self.imgPasajero, anchor="nw")
                elif self.matriz[i][j] == self.destino:
                    self.canvas.create_rectangle(x, y, x+90, y+60, fill="orange")


    
    """
    x, y = ruta[0]
    x_pixeles = y*60
    y_pixeles = x*60
    """



        


