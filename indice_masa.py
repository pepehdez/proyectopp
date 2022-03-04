from socket import IP_MULTICAST_IF


print()
print("Autor: Alberto Hernandez")
print()
peso = input("PESO ")
peso = float(peso)
talla = input("TALLA ")
talla = float(talla)
imc = (peso / (talla * 2))
imc = round(imc , 2)
imc = str(imc)
print("Tienes "+ imc +" en masa corporal")
imc = float(imc)
if imc < 18.5:
    print("Malnutricion")
elif imc >= 30:
    print("Obeso")
elif imc >= 18.5 and imc <= 24.9:
    print("Normal")
elif imc >= 25 and imc <= 29.9:
    print("Sobrepeso")
else:
    print("Parametro no cumple ..") 
                   
