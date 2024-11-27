from Menu.mainMenu import mainMenu
from Menu.calcularImpuesto import taxesCalculator
from Menu.listaImpuestoMenu import listaImpuestos

while True:
    match mainMenu():
        case 1: taxesCalculator()
        case 2: listaImpuestos()
        case _: exit()