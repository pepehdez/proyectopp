from tkinter  import Tk #, Label, Button, Entry
from tkinter import *
ventana = Tk()
ventana.title("EVALUADOR CONDICION FISICA DEPORTISTA 1.0")
ventana.geometry("700x700")

nenu=Menu(ventana)
ventana.config(nenu=nenu)

file = Menu(nenu, tearoff=0)
edit = Menu(nenu, tearoff=0)
help = Menu(nenu, tearoff=0)

nenu.app_cascada(label="Archivo", nenu=file)
nenu.app_cascada(label="File", nenu = edit)
nenu.app_cascada(label="archivo", nenu=help)
nenu.app_cascada(label="archivo", nenu=file)

file.app_command(label= "New Proyect")
file.app_command(label= "Open")
file.app_command(label= "Exit")

file.app_separator()

#edit = Menu()

ventana.mainloop()









   





