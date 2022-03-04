from glob import escape


print()
print("Autor: Alberto Hernandez")
print()
print("Bienvenido a la Valoracion Fisica  de Deportista de la UdC")
print()
peso = input("Que peso tienes? ")
peso = float(peso)
talla = input("Cuanto mides ")
talla = float(talla)
#imc = (peso / (talla * 2))
imc = (peso)/(talla **2)
imc = round(imc , 2)
imc = str(imc)
print()
print("TU IMC = "+ imc )
print("NIVEL DE PESO")
imc = float(imc)
if imc < 18.5:
    
    print("Bajo peso")
    print()
    print("Su rango de peso saludale sugerido es de 55k a 60k")
elif imc >= 30:
    print("Obeso")
    print()
    print("Su rango de peso saludable sugerido es de 62 a 83kg")
elif imc >= 18.5 or imc <= 24.9:
    print("Normal")
    print()
    print("Su rango de peso saludable sugerido es de55 a 74kg")
elif imc >= 25 or imc <= 29.9:
    print("Sobrepeso")
else:
    print("Parametro no cumple ..") 
