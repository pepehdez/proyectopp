from logging.handlers import TimedRotatingFileHandler
from mailbox import NoSuchMailboxError
import os
import sys
import sqlite3

deportista = 0

def agregar_dep():
    os.system("cls")
    print("-------Agrega un Deportista--------")
    print("")

    nombre = input(" Digite el nombre del deportista.. ")
    
    edad = input(" Digite la edad: ")
    edad = float(edad)
    peso = input(" Digite su peso de deportista: ")
    peso = float(peso)  
    
    talla = input(" Digite su talla: ")
    talla = float(talla)
    imc = (peso)/(talla **2)
    imc = round(imc , 2)
    imc = str(imc)
    edad = str(edad)
    peso = str(peso)
    talla = str(talla)
    
    con = sqlite3.connect("deportistau.db")
    cursor = con.cursor()
    cursor.execute("insert into deportistau (nombre,edad,peso,talla,imc) values ('"+nombre+"', '"+edad+"', '"+peso+"', '"+talla+"','"+imc+"')")
     
    con.commit()
    con.close()

    print("Deportista agregado")
    print(" ")
    print("[m] Volver al MENU.")
    print()
    print("[s] Salir.")
    print(" ")

    opcion = input("Digite una opcion:  ")

    if opcion == "m":
       menu()
    elif opcion == "s":
       sys.exit()

def consulta_dep():
    os.system("cls")
    print("----------------Listado de Deportistas-------------")
    print("")

    con = sqlite3.connect("deportistau.db")
    cursor = con.cursor()
    cursor.execute("select * from deportistau")

    print("------\t\t------\t\t------\t\t------\t\t-----\t\t-----")
    print("codigo\t\tnombre\t\tedad\t\tpeso\t\ttalla\t\timc")
    print("------\t\t------\t\t------\t\t------\t\t-----\t\t-----")
    
    
    for deportista in cursor:
                
            #print(deportistau[5])
            #print("texto[]") 
        if deportista[5] < 18.5:
                
                texto =("Bajo peso")
            #    print("Bajo peso")
        elif deportista[5] >= 30:
            #  print("Obeso")
              texto = ("Obeso")
            
        elif deportista[5] >= 18.5 or deportista[5] <= 24.9:
              
              texto = ("Normal")
            #  print("Normal")
            
        elif deportista[5] >= 25 or deportista[5] <= 29.9:
              texto = ("Sobrepeso")
            #  print("sobrepeso")

              print(str(deportista[0]+"\t\t"+deportista[1]+"\t\t"+deportista[2]+"\t\t"+deportista[3]+"\t\t"+deportista[4]+"\t\t"+deportista[5]))
        else:
              
             print(str(deportista[1]+"\t\t"+deportista[2]+"\t\t"+deportista[3]+"\t\t"+deportista[4]+"\t\t"+deportista[5]))
             print("Parametro no cumple ..")
           
                
            #print(deportista[1]+"\t\t"deportista[2]+"\t\t"deportista[3]+"\t\t"deportista[4])
                
            
    con.close()  

    print(" ")
    print("[m] Volver al MENU.")
    print("[s] Salir.")
    print(" ")  

    opcion = input("Digite una opcion: ")

    if opcion == "m":
       menu()
    elif opcion == "s":
        sys.exit()


    def modificar_dep():
     os.system("cls")
    con = sqlite3.connect("deportistau.db")
    cursor = con.cursor()
    cursor.execute("select * from deportistau")
    
    print("---Modificar---")
    print("")
    print("-----\t\t-----\t\t-----\t\t------\t\t------")
    print("codigo\t\tnombre\t\tedad\t\tpeso\t\ttalla\t\t")
    print("-----\t\t-----\t\t------\t\t-----\t\t------")
    print("")

    for deportista in cursor:
        print(str(deportista[0])+"\t\t"+deportista[1]+"\t\t"+deportista[3]+"\t\t"+deportista[4]+"\t\t"+deportista[5])
        print("")

    print("")
    codigo = input("Digite el codigo del deportista que desea modificar?..")
    
    print("")
    nombre = input("Digite el nuevo deportista: ")
    edad = input("Digite su edad: ")
    peso = input("Digite el nuevo peso: ")
    talla = input("Digite su talla: " )

    sql = "update deportista set nombre='"+nombre+"',edad ='"+edad+"', peso='"+peso+"' ,talla ='"+talla+"' where codigo="+codigo

    cursor.execute(sql)
    con.commit()
    con.close()

    print("")
    print("Deportista modificado")
    print(" ")
    print("[m] Volver al MENU.")
    print("[s] Salir.")
    print(" ")

    opcion = input("Digite una opcion: ")

    if opcion == "m":
        menu()
    elif opcion == "s":
        sys.exit()

def eliminar_dep():
    os.system("cls")
    con = sqlite3.connect("deportistau.db")
    cursor = con.cursor()
    cursor.execute("select * from deportistau")
    
    print("---Eliminar deportista---")
    print("")
    print("-----\t\t-----\t\t-----")
    print("codigo\t\tnombre\t\tedad\t\tpeso\t\ttalla\t\timc")
    print("-----\t\t---\t\t--------")
    print("")

    for deportista in cursor:
        print(str(codigo[0])+"\t\t"+ 'nombre[1]'+ "\t\t" +'edad[2]'+ "\t\t" +'peso[3]'+ "\t\t" +'talla'[4])
       #print(str(articulo[0])+"\t\t"+articulo[1]+"\t\t"+articulo[2])
        print("")

    print("")
    codigo = input("Digite el codigo del deportista que desea Eliminar?..")
          
    sql = "delete from deportistas where codigo="+codigo

    cursor.execute(sql)
    con.commit()

    print("")
    print("Deportista Eliminado")
    print(" ")
    print("[m] Volver al MENU.")
    print("[s] Salir.")
    print(" ")

    opcion = input("Digite una opcion")

    if opcion == "m":
        menu()
    elif opcion == "s":
        sys.exit()

def menu():
    os.system("cls")
    print("--Informacion del Deportista--")
    print("")
    print("[1] Agregar un Deportista ")
    print("[2] Consultar  Deportista ")
    print("[3] Modificar ")
    print("[e] Eliminar ")
    print("[s] Salir ")
    print("")

    opcion = input("Digite una Opcion: ")

    if opcion == "1":
        agregar_dep()
    elif opcion == "2":
        consulta_dep()
    elif opcion == "3":
        modificar_dep()
    elif opcion == "e":
        eliminar_dep()
    elif opcion == "s":
        sys.exit()
    else:
        opcion == input("Digite una opcion valida: ") 
        menu(opcion) 
menu()                             
