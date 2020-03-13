# -*- coding = utf8 -*-

# Llamamiento de la clase vehiculo
from vehiculo import Vehiculo

class Parqueo:
    def __init__(self):
        """ Inicializa la lista donde se almacenan los vehiculos """
        self.vehiculos_ingresados = list()

    def nuevo_ingreso(self):
        """ Agrega un nuevo vehiculo """
        placa = input("Ingrese el numero de la placa del vehiculo: ") 
        marca = input("Ingrese la marca del vehiculo: ")
        modelo = input("Ingrese el modelo del vehiculo: ")
        tipo = input("Ingrese el tipo del vehiculo(1: Motocicleta. 2: Automóvil):")

        self.vehiculos_ingresados.append(Vehiculo(placa,marca,modelo,tipo))

    def buscar_vehiculo(self,placa = ""):
        while placa == "":
            placa = input("Ingrese el numero de placa del vehiculo: ")
        if len(self.vehiculos_ingresados) != 0:
            for x in range(len(self.vehiculos_ingresados)):
                if placa == self.vehiculos_ingresados[x].placa:
                    print("\nVehiculo encontrado")
                    return True
                else:
                    print("Vehiculo no encontrado")
                    return False
            else:
                print("No se an ingresado vehiculos")

