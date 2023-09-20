#IMPORTS
import time



#FUNCIONES

#Ingresar opcion al menú
def ingresar_opcion():
   opcion=0
   
   while opcion!=1 or opcion!=2 or opcion!=3:
        opcion=int(input("Ingrese una opcion: "))
        print("===============================================================")

        if opcion==1:
            ingresar_pedido()
            confirmar_pedido()
            break

        elif opcion==2:
            nombre = ingresar()
            saludar(nombre)
            ver_menu()
            break

        elif opcion==3:
            print("Sistema finalizado")
            opcion=0
            break


#Opcion 1: Ingresar el pedido (1/4)
def ingresar_pedido():

    nombre_cliente = input("Ingrese nombre del cliente: ")
    combo_s = int(input("Ingrese cantidad Combo S : "))
    combo_d = int(input("Ingrese cantidad Combo D: "))
    combo_t = int(input("Ingrese cantidad Combo T: "))
    flurby = int(input("Ingrese cantidad Flurby: "))
    total = calcular_monto(combo_s, combo_d, combo_t, flurby)
    confirmar_pedido(nombre_cliente, combo_s, combo_d, combo_t, flurby, total)

    
# Opcion 1: Calcular el monto (2/4)
def calcular_monto(combo_s,combo_d,combo_t,flurby):
    total = (combo_s * 5) + (combo_d * 6) + (combo_t * 7) + (flurby * 2)
    print("Total $", total)
    abona=int(input("Ingrese monto con el que abona: $"))
    print("Abona con $", abona)
    vuelto = abona - total
    print("Vuelto $", vuelto)
    return total


#Opcion 1: Confirmar pedido (3/4)
def confirmar_pedido(nombre_cliente, combo_s, combo_d, combo_t, flurby, total):
    pedido_confirmado=False

    while pedido_confirmado != True:
        confirma=input("¿Confirma pedido? Y/N : ")

        if(confirma=="Y"):
            pedido_confirmado:True
            pedido = [nombre_cliente, combo_s, combo_d, combo_t, flurby, total]
            ventas = open("ventas.txt", "w")
            for dato in pedido:
                ventas.write(dato + " , ")
            ventas.write("\n")
            ventas.close()
            print("Pedido confirmado exitosamente")

        elif(confirma=="N"):
            print("Pedido cancelado")
        else:
            print("Opcion incorrecta ingrese nuevamente")
            confirmar_pedido()


#Ingreso del encrgado
def ingresar():  
    print("\nBienvenido a Hamburguesas IT")
    nombre = input("Ingrese su nombre encargad@: ")
    return nombre


#Mensaje de bienvenida al encargado
def saludar(nombre):
    print("Bienvenido a Hamburguesas IT")
    print("Encargad@ ->", nombre)
    print("Recuerda, siempre hay que recibir al cliente con una sonrisa :)")


#Menú
def ver_menu():
    print("===========================MENU================================")
    print("1 – Ingreso nuevo pedido")
    print("2 – Cambio de turno")
    print("3 – Apagar sistema")
    print("===============================================================")
    ingresar_opcion()
    print("===============================================================")




#MAIN

nombre = ingresar()
saludar(nombre)
ver_menu()