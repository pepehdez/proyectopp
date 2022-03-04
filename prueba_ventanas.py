from tkinter  import Tk, Label, Button, Entry
#from tkinter import *
vent = Tk()
vent.title("CALCULAR INDECE DE MASA CORPORAL")
vent.geometry("400x200")

def divmod(): 
    n1 = txt1.get()
    n2 = txt2.get()
    n1 = float(n1)
    n2 = float(n2)
    r  = (n1 / (n2 ** 2))
    r = round(r,2)
    #imc = r
    #imc = float(imc)
    txt3.delete(0,"end")
    txt3.insert(0,r)
    if r < 18.5:
      men1 = Label(vent, text="Malnutricion", bg = "red")
      men1.place(x=230, y= 130, width = 80, height =30)
      lbl4 = Label(vent, text = "Su rango de pesos saludable sugerido es de 55 a 62kg")
      lbl4.place(x=10, y=170) 
    elif r >= 18.5 and r <= 24.9:
      men3 = Label(vent, text= "Normal", bg = "green") 
      men3.place(x=230, y= 130, width = 80, height = 30)
      lbl4 = Label(vent, text = "Su rango de pesos saludable sugerido es de 62 a 83kg")
      lbl4.pack()    
    elif r >= 25 and r <= 29.9:
      men3 = Label(vent, text= "Sobrepeso", bg = "red") 
      men3.place(x=230, y= 130, width = 80, height = 30)
      lbl4 = Label(vent, text = "Su rango de pesos saludable sugerido es de 62 a 83kg")
      lbl4.pack(x=10, y=170)    
    elif r >= 30:
      men2 = Label(vent, text= "Obeso", bg = "red") 
      men2.place(x=230, y= 130, width = 80, height = 30) 
      lbl4 = Label(vent, text = "Su rango de pesos saludable sugerido es de 62 a 83kg")
      lbl4.pack(X=10, y=170)  
    else:
      men4 = Label(vent, text= "Paramentos no cumple", bg = "blue") 
      men4.place(x=10, y= 170)    
    
lbl0 = Label(vent, text= "Nombre: ", bg = "#bfdaff") 
lbl0.place(x = 10, y = 10, width = 100, height = 30)   

txt0 = Entry(vent, bg = "beige")
txt0.place( x = 120, y= 10, width = 100, height = 30)

lbl1 = Label(vent, text="Peso: ", bg = "#bfdaff")
lbl1.place(x = 10, y= 50, width = 100, height = 30)

txt1 = Entry(vent, bg = "beige")
txt1.place( x = 120, y= 50, width = 100, height = 30)

lbl2 = Label(vent, text = "Talla: ", bg = "#bfdaff")
lbl2.place(x =10, y= 90, width = 100, height = 30)

txt2 = Entry(vent, bg = "beige")
txt2.place(x = 120, y= 90, width = 100, height = 30)

btn1 = Button(vent, text = "Calcular", command = divmod)
btn1.place(x = 230, y = 50, width = 80, height = 30)

lbl3 = Label(vent, text = "IMC: ", bg = "#bfdaff")
lbl3.place(x =10, y=130, width = 100, height = 30)

txt3 = Entry(vent, bg = "beige")
txt3.place(x = 120, y = 130, width = 100, height = 30)



vent.mainloop()







   





