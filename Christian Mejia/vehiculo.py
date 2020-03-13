# -*- coding = utf8 -*-
# Librerias necesarias
from datetime import datetime,timedelta
import random

class Vehiculo:
    """ Clase donde se generan los vehiculos """ 
    horas = 0
    
    def __init__(self,placa,marca,modelo,tipo,):
        """ Asigna los valores al vehiculo """
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo
        self.hora_entrada = datetime.now()
        horas = random.randint(1,6)
        self.hora_salida = datetime.now() + timedelta(horas)

