from Menu.mainMenu import mainMenu
from Menu.calcularImpuesto import taxesCalculator
from Menu.listaImpuestoMenu import listaImpuestos
import os

while True:
    match mainMenu():
        case 1: 
            os.system('clear')
            taxesCalculator()
        case 2: listaImpuestos()
        case _: exit()