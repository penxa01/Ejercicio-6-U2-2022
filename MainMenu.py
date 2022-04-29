import os
from Manejador import Manejador
from ViajeroFrecuente import ViajeroFrecuente


if __name__== "__main__":

    Lista = Manejador()
    Lista.GenerarLista()
    Lista.Listar()
    NroViaj= int(input("Ingrese nro de viajero del cual desea consultar\n"))
    Viajero= Lista.Buscar(NroViaj)
    
    continuar = True

    while continuar:
        print("MENU".center(20,"-"))
        print("[1] Para consultar cantidad de millas")
        print("[2] Para acumular millas")
        print("[3] Para canjear millas")
        print("[4] Mostrar viajero con mas millas acumuladas")
        print("[5] Acumular millas usando SOBRECARGA DE OPERADORES")
        print("[6] Canjear millas usando SOBRECARGA DE OPERADORES")
        print("[7] Viajero con mas millas acumuladas SOBRECARGA DE OPERADORES")
        print("[8] Listar Viajeros")
        print("[0] Para SALIR del menu")

        op = int( input("INGRESE OPCION POR TECLADO\n"))
        os.system("cls")
        if ( op == 1):
            print("".center(20,"-"))
            print("Consultar cantidad de millas\n")
            print(Viajero.cantidadTotalMillas())
        elif(op == 2):
            Acum = int(input("Ingrese cantidad de millas que desea acumular\n"))
            Viajero.acumularMillas(Acum)
        elif(op == 3):
            Canj = int(input("Ingrese millas que desea canjear\n"))
            Viajero.canjearMillas(Canj)
        elif(op == 4):
            Lista.MaximoMillas()
        elif(op == 5):
            Acum = int(input("Ingrese cantidad de millas que desea acumular\n"))
            Viajero = Viajero + Acum
            print("".center(20,"-"))
            print(Viajero)
            print("".center(20,"-"))
            input("ENTER PARA CONTINUAR")
        elif(op == 6):
            Canj = int(input("Ingrese millas que desea canjear\n"))
            Viajero = Viajero - Canj
            print("".center(20,"-"))
            print(Viajero)
            print("".center(20,"-"))
            input("ENTER PARA CONTINUAR")
        elif( op == 7):
            v = Lista.MillasMaximas()
            print("El viajero con mas millas es:")
            print("".center(20,"-"))
            print(v)
            print("".center(20,"-"))
            input("ENTER PARA CONTINUAR")
        elif(op == 8):
            Lista.Listar()
        elif(op == 0):
            continuar = not continuar
            print("MUCHAS GRACIAS")
    
