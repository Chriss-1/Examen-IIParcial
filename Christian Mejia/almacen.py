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

    def contador(self,placa = ""):
        """ retorna el indice del vehiculo segun la placa """ 
        while placa == "":
            placa = input("Ingrese el numero de placa del vehiculo: ")
        for x in range(len(self.vehiculos_ingresados)):
            if placa == self.vehiculos_ingresados[x].placa:
                print("\nVehiculo encontrado")
                return x


    def buscar_vehiculo(self,placa = ""):
        """ Verifica que la existencia del vehiculo """ 
        while placa == "":
            placa = input("Ingrese el numero de placa del vehiculo: ")
        if len(self.vehiculos_ingresados) != 0:
            for x in range(len(self.vehiculos_ingresados)):
                if placa == self.vehiculos_ingresados[x].placa and self.vehiculos_ingresados[x].estado == True:
                    print("\nVehiculo encontrado")
                    return True
                else:
                    print("Vehiculo no encontrado")
                    return False
            else:
                print("No se an ingresado vehiculos")
                return False

        
    def imprimir_vehiculos(self):
        for x in range(len(self.vehiculos_ingresados)):
            print(self.vehiculos_ingresados[x].placa, "  ",self.vehiculos_ingresados[x].marca)

    def tarifa(self,contador):
        """ Calcula la tarifa a cobrar """
        if self.vehiculos_ingresados[contador].tipo == 1:
            subtotal_sin_descuento = ((int(self.vehiculos_ingresados[contador].total_horas) - 1) * 10)
            subtotal_con_descuento = (subtotal_sin_descuento) * 0.10
            _tarifa_ = 10 + (subtotal_sin_descuento - subtotal_con_descuento)
            return _tarifa_
        else: 
            subtotal_sin_descuento = ((int(self.vehiculos_ingresados[contador].total_horas) - 1) * 20)
            subtotal_con_descuento = (subtotal_sin_descuento) * 0.10
            _tarifa_ = 20 + (subtotal_sin_descuento - subtotal_con_descuento)
            return _tarifa_

    def Imprimir_ticket(self):
        """ Imprime el ticket del vehiculo que sale """
        self.imprimir_vehiculos()
        placa = input("Ingrese la placa del vehiculo que saldra: ")
        if self.buscar_vehiculo(placa):
            contador = self.contador(placa)
            self.vehiculos_ingresados[contador].estado = False
            print("***********Genisys Inc***********")
            print("Hora de entrada: ",self.vehiculos_ingresados[contador].hora_entrada)
            print("Horas utilizadas: ",self.vehiculos_ingresados[contador].total_horas)
            print("Total a pagar: ",tarifa = self.tarifa(contador))
            print("**********Vuelva Pronto**********")

    def reporte_vehiculos(self):
        """ Imprime el reporte de los vehiculos ingresados y egresados """
        print("****Vehiculos Ingresados****")
        for x in range(len(self.vehiculos_ingresados)):
            print("\n")
            print("Placa del vehiculo: ",self.vehiculos_ingresados[x].placa)
            print("Marca del vehiculo: ",self.vehiculos_ingresados[x].marca)
            print("Hora de ingreso: ",self.vehiculos_ingresados[x].hora_entrada)

        print("****Vehiculos que salieron****")
        for x in range(len(self.vehiculos_ingresados)):
            if self.vehiculos_ingresados[x].estado == False:
                print("\n")
                print("Placa del vehiculo: ",self.vehiculos_ingresados[x].placa)
                print("Marca del vehiculo: ",self.vehiculos_ingresados[x].marca)
                print("Hora de ingreso: ",self.vehiculos_ingresados[x].hora_entrada)
                print("Hora de salida: ",self.vehiculos_ingresados[x].hora_salida)
            