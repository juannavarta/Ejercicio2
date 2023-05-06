import csv
from classViajero import ViajeroFrecuente
if __name__ == "__main__":
    viajeros = []
    archivo = open('C://Users//csv//Viajeros.csv', 'r')
    reader = csv.reader(archivo, delimiter=";")
    for fila in reader:
        num = int(fila[0])
        dni = fila[1]
        nom = fila[2]
        ape = fila[3]
        millas = int(fila[4])
        viaje = ViajeroFrecuente(num, dni, nom, ape, millas)
        viajeros.append(viaje)
    i=0
    while i==0:
        print("Menu")
        print("1. Consultar Millas")
        print("2. Acumular Millas")
        print("3. Canjear Millas")
        print("0. Cerrar")
        opcion = int(input())
        if opcion==0:
            exit()
        elif opcion==1:
            j=0
            numV = int(input("Ingrese numero de viajero a consultar: "))
            while j<=len(viajeros) and numV != viajeros[j].getNumero():
                j+=1
            if j > len(viajeros):
                print("Numero incorrecto")
            else:
                print("El viajero con numero {} tiene {} millas".format(viajeros[j].getNumero(), viajeros[j].cantidadTotalMillas()))
        elif opcion==2:
            j=0
            numV = int(input("Ingrese numero de viajero a acumular millas: "))
            while j<=len(viajeros) and numV != viajeros[j].getNumero():
                j+=1
            if j > len(viajeros):
                print("Numero incorrecto")
            else:
                mil = int(input("Ingrese la cantidad de millas a acumular: "))
                print("El viajero con numero {} ahora tiene {} millas".format(viajeros[j].getNumero(), viajeros[j].acumularMillas(mil)))
        elif opcion==3:
            j=0
            numV = int(input("Ingrese numero de viajero a canjear millas: "))
            while j<=len(viajeros) and numV != viajeros[j].getNumero():
                j+=1
            if j > len(viajeros):
                print("Numero incorrecto")
            else:
                mil = int(input("Ingrese la cantidad de millas a canjear: "))
                if mil <= viajeros[j].cantidadTotalMillas():
                    print("El viajero con numero {} ahora tiene {} millas".format(viajeros[j].getNumero(), viajeros[j].canjearMillas(mil)))
                else:
                    print("La cantidad de millas seleccionadas no alcanzan para realizar el canje")
        else:
            print("Opción Inválida")