from tkinter import ttk
import tkinter as tk
from tkinter import Frame, Label, Button


class Frame(tk.frame):
    def __init__(self, root =None):
        super().__init__(root,width=480, height=320)
        self.root = root
        self.pack()
        #self.config(bg = "green")
        self.id_pelicula = None

        root = Frame(root = root)
        root.mainloop()


def main():
    root= tk.Tk()
    root.title("Prueba de Ventanas")
    root.iconbitmap('balon.ico')
    root.resizable(0,0)
    #barra_menu(root)


   
    
if __name__ =='__main__':
    main()     
