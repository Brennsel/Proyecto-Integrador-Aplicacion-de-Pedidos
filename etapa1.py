#IMPORTS
import time


#FUNCIONES
def ingresar():  
    print("\nBienvenido a Hamburguesas IT")
    nombre = input("Ingrese su nombre encargad@: ")
    saludar(nombre)


def saludar(nombre):
    print("Bienvenido a Hamburguesas IT")
    print("Encargad@ ->", nombre)
    print("Recuerda, siempre hay que recibir al cliente con una sonrisa :)")


def ver_menu():
    print("===========================MENU================================")
    print("1 – Ingreso nuevo pedido")
    print("2 – Cambio de turno")
    print("3 – Apagar sistema")
    print("===============================================================")
    ingresar_opcion()
    print("===============================================================")


def ingresar_opcion():
   opcion=0
   
   while opcion!=1 or opcion!=2 or opcion!=3:
        opcion=input("Ingrese una opcion: ")
        print("===============================================================")

        if opcion==1:
            ingresar_pedido()
            confirmar_pedido()
            break

        elif opcion==2:
            ingresar()
            saludar()
            ver_menu()
            ingresar_opcion()
            break

        elif opcion==3:
            print("Sistema finalizado")
            opcion=0
            break


def ingresar_pedido():

    print("Ingrese nombre del cliente: ")
    nombre_cliente = input()
    print("Ingrese cantidad Combo S : ")
    combo_s = int(input())
    print("Ingrese cantidad Combo D: ")
    combo_d = int(input())
    print("Ingrese cantidad Combo T: ")
    combo_t = int(input())
    print("Ingrese cantidad Flurby: ")
    flurby = int(input())
    calcular_monto(combo_s,combo_d,combo_t,flurby)
    confirmar_pedido
    

def calcular_monto(combo_s,combo_d,combo_t,flurby):
    total = (combo_s * 5) + (combo_d * 6) + (combo_t * 7) + (flurby * 2)
    print("Total $", total)
    print("Abona con $", total)
    abona = int(input())
    vuelto = abona - total
    print("Vuelto $", vuelto)


def confirmar_pedido():
    pedido_confirmado=False
    confirma=str(input("¿Confirma pedido? Y/N : "))

    if(confirma=="Y"):
        pedido_confirmado:True
        print("Pedido confirmado exitosamente")
    elif(confirma=="N"):
        print("Pedido cancelado")
    else:
        print("Opcion incorrecta ingrese nuevamente")
        confirmar_pedido()

#MAIN

ingresar()
ver_menu()