from tkinter  import Tk, Menu, Label, Button, Entry
from tkinter import *
from tkinter import messagebox
#from PIL import inmageTk, image
from tkinter.filedialog import askopenfilename
vent = Tk()
vent.title("EVALUADOR CONDICION FISICA DEPORTISTA 1.0")
vent.geometry("700x400")
menu=Menu(vent)
vent.config(menu=menu)

def divmod(): 
    n1 = txt2.get()
    n2 = txt3.get()
    n1 = float(n1)
    n2 = float(n2)
    r  = (n1 / (n2 ** 2))
    r = round(r,2)
    #imc = r
    #imc = float(imc)
    txt4.delete(0,"end")
    txt4.insert(0,r)
    if r < 18.5:
      men1 = Label(vent, text="Malnutricion", bg = "red")
      men1.place(x=230, y= 130, width = 80, height =20)
      lbl5 = Label(vent, text = "Para su estatura, su peso Normal varia entre 67,5 a 90,8 kilogramos")
      lbl5.place(x=300, y= 130) 
    elif r >= 18.5 and r <= 24.9:
      men3 = Label(vent, text= "Normal", bg = "green") 
      men3.place(x=230, y= 130, width = 80, height = 20)
      lb15 = Label(vent, text= "Para su estatuta, su peso Normal varia entre 62 a 83,4 Kilogramos")
      lb15.place(x=310, y=130)
      lbl5.pack(x=10, y= 170)
         
    elif r >= 25 and r <= 29.9:
      men3 = Label(vent, text= "Sobrepeso", bg = "red") 
      men3.place(x=230, y= 130, width = 80, height = 20)
      lbl5.pack(x=10, y=170)    
    elif r >= 30:
      men2 = Label(vent, text= "Obeso", bg = "red") 
      men2.place(x=230, y= 130, width = 80, height = 20)
      lbl5.pack(X=10, y=170)  
    else:
      men4 = Label(vent, text= "Paramentos no cumple", bg = "blue") 
      men4.place(x=10, y= 170)    

#vent.mainloop()
 

File = Menu(menu, tearoff=0)
File.add_command(label  = "Crear Registro DB")
File.add_command(label = "Elimina Registro DB")
File.add_separator()
File.add_command(label = "Salir")

Edit = Menu(menu, tearoff=0)
Edit.add_command(label= "Consulta Registro BD") 
Edit.add_command(label= "Modifica Registro BD")
Edit.add_command(label= "Guardar")

Help = Menu(menu, tearoff=0)
Help.add_command(label= "Ayuda") 
Help.add_separator()
Help.add_command(label="Acerca")

menu.add_cascade(label= "Inicio", menu=File)
menu.add_cascade(label= "Consulta", menu=Edit)
menu.add_cascade(label= "Ayuda", menu=Help)

lbl0 = Label(vent, text= "Nombre: ", bg = "#bfdaff") 
lbl0.place(x = 10, y = 10, width = 100, height = 20)   

txt0 = Entry(vent, bg = "beige")
txt0.place( x = 120, y= 10, width = 100, height = 20)

lbl1 = Label(vent, text="Edad: ", bg = "#bfdaff")
lbl1.place(x = 10, y= 40, width = 100, height = 20)

txt1 = Entry(vent, bg = "beige")
txt1.place( x = 120, y= 40, width = 100, height = 20)

lbl2 = Label(vent, text="Peso: ", bg = "#bfdaff")
lbl2.place(x = 10, y= 70, width = 100, height = 20)

txt2 = Entry(vent, bg = "beige")
txt2.place( x = 120, y= 70, width = 100, height = 20)


lbl3 = Label(vent, text="Talla: ", bg = "#bfdaff")
lbl3.place(x = 10, y= 100, width = 100, height = 20)

txt3 = Entry(vent, bg = "beige")
txt3.place( x = 120, y= 100, width = 100, height = 20)


lbl4 = Label(vent, text = "IMC: ", bg = "#bfdaff")
lbl4.place(x =10, y=130, width = 100, height = 20)

txt4 = Entry(vent, bg = "beige")
txt4.place(x = 120, y = 130, width = 100, height = 20)

btn0 = Button(vent, text = "Nuevo", bg = "blue")
btn0.place(x= 10, y = 170, width =100, height = 30) 


btn1 = Button(vent, text = "Calcular", bg= "red", command = divmod)
btn1.place(x = 270, y = 170, width = 100, height = 30)

btn2 = Button(vent, text = "Cancelar", bg = "blue")
btn2.place(x= 530, y = 170, width =100, height = 30)




#
Edit = Menu()

vent.mainloop()









   





