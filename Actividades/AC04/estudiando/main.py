from collections import deque
from paquete import Paquete
from botella import Botella

__author__ = 'patricio_lopez'


class Maquina:

    def procesar(self, linea_produccion_entrante):
        print("----------------------")
        print("La maquina {} comienza a trabajar.".format(
            self.__class__.__name__))


class Botellizamodulador(Maquina):

    def __init__(self):
        self.botellas_a_producir = 0

    def procesar(self, linea_produccion_entrante=None):
        super().procesar(linea_produccion_entrante)
        production_line = deque()
        while len(production_line) != self.botellas_a_producir:
            if len(production_line) == 0:
                production_line.append(Botella())
            elif len(production_line) % 5 == 0:
                previous_bottle = production_line[-1]
                production_line.append(Botella(litros=previous_bottle.litros * 3))
            elif len(production_line) % 6 == 0:
                previous_bottle = production_line[-1]
                pre_previous_bottle = production_line[-2]
                production_line.append(Botella(litros=previous_bottle.litros / 2 + pre_previous_bottle.litros * 4))
            else:
                production_line.append(Botella())
        return production_line


class LowFAT32(Maquina):

    def __init__(self):
        self.botellas_desechadas = []

    def desechar_botella(self, botella):
        self.botellas_desechadas.append(botella)

    def imprimir_botellas_desechadas(self):
        print("Se desecharon {} botellas".format(
            len(self.botellas_desechadas)))

    def procesar(self, linea_produccion_entrante):
        super().procesar(linea_produccion_entrante)
        production_line = deque()
        while len(linea_produccion_entrante) != 0:
            bottle = linea_produccion_entrante.popleft()
            if len(production_line) == 0:
                production_line.append(bottle)
            elif bottle.litros >= production_line[-1].litros:
                production_line.append(bottle)
            elif bottle.litros <= production_line[0].litros:
                production_line.appendleft(bottle)
            else:
                self.desechar_botella(bottle)
        self.imprimir_botellas_desechadas()
        return production_line


class HashSoda9001(Maquina):

    def procesar(self, linea_produccion_entrante):
        super().procesar(linea_produccion_entrante)
        storage = dict()
        while len(linea_produccion_entrante) != 0:
            bottle = linea_produccion_entrante.popleft()
            if bottle.litros not in storage:
                storage[bottle.litros] = []
            liters = storage[bottle.litros]
            liters.append(bottle)
        return storage


class PackageManager(Maquina):

    def procesar(self, linea_produccion_entrante):
        paquetes = deque()
        for pila in linea_produccion_entrante.values():
            paquete = Paquete()
            paquete.agregar_botellas(pila)
            paquetes.append(paquete)
        return paquetes


class Fabrica:

    def __init__(self):
        self.botellizamodulador = Botellizamodulador()
        self.lowFAT32 = LowFAT32()
        self.hashSoda9001 = HashSoda9001()
        self.packageManager = PackageManager()

    def producir(self, numero_botellas):
        self.botellizamodulador.botellas_a_producir = numero_botellas
        producto = None
        for maquina in [self.botellizamodulador,
                        self.lowFAT32,
                        self.hashSoda9001,
                        self.packageManager]:
            producto = maquina.procesar(producto)
        return producto


if __name__ == "__main__":

    numero_botellas = 1000312

    fabrica = Fabrica()
    output = fabrica.producir(numero_botellas)
    print("----------------------")
    print("Para {} botellas, se producen {} paquetes".format(
        numero_botellas, len(output)))
    for paquete in output:
        paquete.ver_contenido()
    print("----------------------")
