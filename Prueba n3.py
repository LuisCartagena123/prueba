import json

def menu():
    print("1. Registrar pedido")
    print("2. Listar los todos los pedidos")
    print("3. Imprimir hoja de ruta")
    print("4. Salir del programa")


def registrar():
    datos = ["Nombre", "Comuna", "cil.5kg","cil.15kg","cil.45kg"]
    
    nom = input("Ingrese su nombre y apellido: ")
    com = input("Ingrese su comuna: ")

    opcCI = 0
    cont5 = 0
    cont15 = 0
    cont45 = 0
    while opcCI != 4:
        
        try:    
            print("1. Cilindro de 5 kg")
            print("2. Cilindro de 15 kg")
            print("3. Cilindro de 45 kg")
            print("4. Salir")
            
            opcCI = int(input("Que opcion desea?: "))
        except:
            print("Opcion invalida, porfavor ingrese una opcion")
        try:
            if opcCI == 1:
                cantC5= int(input("Cuantos cilindros quiere comprar?: "))
                cont5 = cont5 + cantC5
            elif opcCI == 2:
                cantC15= int(input("Cuantos cilindros quiere comprar?: "))
                cont15 = cont15 + cantC15
            elif opcCI == 3:
                cantC45= int(input("Cuantos cilindros quiere comprar?: "))
                cont45 = cont45 + cantC45
        except:
            print("Debe ingrear la cantidad de cilindros que desea")

        print(cont5)
        print(cont15)
        print(cont45)    


    datos = [nom,com,cont5,cont15,cont45]

    print(datos)
print(registrar)


def listar():
    print(datos)
print(listar)

def imprimir():
    with open ("datos.csv", "r") as archivo:
        for fila in archivo:
            for col in fila:
                print(col)
print(imprimir)
    







opc = 0
while opc != 4:
    menu()
    try:
        opc = int(input("Que desea hacer?: " ))
    except:
        print("Debe ingresar el numero de la opcion")
    
    
    if opc == 1:
      registrar()
    elif opc == 2:
        listar()
    elif opc == 3:
        imprimir()



