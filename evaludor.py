from tkinter import ttk
from tkinter import *

import sqlite3

class Product:


  def __init__(self, window):
       self.wind = window
       self.wind.title("Evaludor de Atletas")

    # creando a frame
       #frame.config(width = 480, heith = 320, bg = )
       frame = LabelFrame(self.wind, text = "Registra un deportista: ")
       frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)
    
      # input del name
       Label(frame, text = "Nombre : ").grid(row = 2, column = 0)
       self.name = Entry(frame)
       self.name.focus()
       self.name.grid(row = 2, column = 1)

       Label(frame, text = "Edad : ").grid(row = 3, column = 0)
       self.name = Entry(frame)
      # self.name.focus()
       self.name.grid(row = 3, column = 1)

    # input del peso
       Label(frame, text = "Peso?: ").grid(row = 4, column = 0)
       self.peso = Entry(frame)
       self.peso.grid(row = 4, column = 1)

    # Input de la talla
       Label(frame, text = "Talla?: ").grid(row = 5, column = 0)
       self.talla = Entry(frame)
       self.talla.grid(row = 5, column = 1)
   

    # Button add deportista
       ttk.Button(frame, text = "Guardar").grid(row = 6, columnspan =2, sticky = W + E)   


if __name__ == "__main__":
  window = Tk()
  application = Product(window)
  window.mainloop()


