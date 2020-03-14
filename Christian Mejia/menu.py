# -*- coding = utf8 -*-
# Repositorio: https://github.com/Chriss-1/Examen-IIParcial.git
# Autor: Christian Mejia
# Fecha: 13/03/20

from almacen import Parqueo
import platform
import sys
import os

class Menu:
    def __init__(self):
        """ Inicialisa los parametros """
        self.almacen = Parqueo()
        self.Opcion ={"1": self.nuevo_vehiculo,
                        "2": self.egreso_vehiculo,
                        "3": self.reporte_vehiculo,
                        #"4": self.reporte_ganacias,
                        "5": self.salir}

    def Opciones(self):
        """ Muestra el menu de opciones """ 
        self.Limpiar_pantalla()
        print("""***********Genisys Inc***********
        1: nuevo ingreso
        2: Egreso de vehiculo
        3: Reporte de vehiculos
        4: Reporte de ganancias
        5: Salir""")

    def nuevo_vehiculo(self):
        """ Ingresa nuevo vehiculo """
        self.almacen.nuevo_ingreso()
        self.enter()

    def egreso_vehiculo(self):
        """ Opcion para dar ticket alos vehiculos que salgan """
        self.almacen.Imprimir_ticket()
        self.enter()
    
    def reporte_vehiculo(self):
        """ Imprime el reporte de vehiculos """
        self.almacen.reporte_vehiculos()
        self.enter()

    def salir(self):
        """ Sale del programa """
        print("Gracias por usar nuestro programa")
        sys.exit()

    def enter(self):
        """ Hace una pausa """
        input("Precione enter para continuar")
    
    def Limpiar_pantalla(self):
        """ Limpia lapantalla segun el sistema"""
        if platform.system() == "Windows":
            os.system("cls")
        elif platform.system() == "Darwin" or platform.system() == "Linux":
            os.system("clear")

    def inicio(self):
        """ Muestra el menu y rectifica la opcion """
        self.Opciones()
        opcion = input("Ingrese su opcion: ")
        accion = self.Opcion.get(opcion)
        if accion:
            accion()
        else:
            print("Opcion invalida")
            self.enter()

if  __name__ == "__main__":
    menu = Menu()
    menu.inicio()

