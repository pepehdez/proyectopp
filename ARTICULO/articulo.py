from logging.handlers import TimedRotatingFileHandler
from mailbox import NoSuchMailboxError
import os
import sys
import sqlite3

def agregar_dep():
    os.system("cls")
    print("-------Agrega un Deportista--------")
    print("")

    nombre = input(" Digite el nombre del deportista.. ")
    edad = input(" Digite la edad: ")
    peso = input(" Digite su peso de deportista: ")
    talla = input(" Digite su talla: ")

    #imc = (peso / (talla * 2))
    #imc = (peso)/(talla **2)
    #imc = round(imc , 2)
    # imc = str(imc)
    
    con = sqlite3.connect("deportista.db")
    cursor = con.cursor()
    cursor.execute("insert into deportista (nombre,edad,peso,talla) values ('"+nombre+"', '"+edad+"', '"+peso+"', '"+talla+"')")
    con.commit()
    con.close()

    print("Deportista agregado")
    print(" ")
    print("[m] Volver al MENU.")
    print("[s] Salir.")
    print(" ")

    opcion = input("Digite una opcion:  ")

    if opcion == "m":
       menu()
    elif opcion == "s":
       sys.exit()

def consulta_dep():
    os.system("cls")
    print("Deportista agregado")
    print("")

    con = sqlite3.connect("deportista.db")
    cursor = con.cursor()
    cursor.execute("select * from deportista")

    print("------\t\t------\t\t------\t\t------")
    print("nombre\t\tedad\t\tpeso\t\ttalla")
    print("------\t\t------\t\t------\t\t------")

    for deportista in cursor:
        print(deportista[1]+"\t\t"+deportista[2]+"\t\t"+deportista[3]+"\t\t"+deportista[4])
        #print(deportista[1]+"\t\t"deportista[2]+"\t\t"deportista[3]+"\t\t"deportista[4])
        print("")

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
    con = sqlite3.connect("deportista.db")
    cursor = con.cursor()
    cursor.execute("select * from deportista")
    
    print("---Modificar---")
    print("")
    print("-----\t\t-----\t\t-----\t\t------\t\t------")
    print("codigo\t\tnombre\t\tedad\t\tpeso\t\ttalla")
    print("-----\t\t-----\t\t------\t\t-----\t\t------")
    print("")

    for deportista in cursor:
        print(str(deportista[0])+"\t\t"+deportista[1]+"\t\t"+deportista[2]+"\t\t"+deportista[3]+"\t\t"+deportista[4])
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
    con = sqlite3.connect("deportista.db")
    cursor = con.cursor()
    cursor.execute("select * from deportista")
    
    print("---Eliminar deportista---")
    print("")
    print("-----\t\t-----\t\t-----")
    print("codigo\t\tnombre\t\tedad\t\tpeso\t\ttalla")
    print("-----\t\t---\t\t--------")
    print("")

    for deportista in cursor:
        print(str(deportista[0])+"\t\t"+deportista[1]+"\t\t"+deportista[2]+"\t\t"+deportista[3]+"\t\t"+deportista[4])
        print("")

    print("")
    codigo = input("Digite el codigo del deportista que desea Eliminar?  ")
          
    sql = "delete from deportista where codigo="+codigo

    cursor.execute(sql)
    con.commit()
    con.close()

    print("")
    print("Deportista Eliminado")
    print(" ")
    print("[m] Volver al MENU.")
    print("[s] Salir.")
    print(" ")
    print("prueba guit")

    opcion = input("Digite una opcion: ")

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
