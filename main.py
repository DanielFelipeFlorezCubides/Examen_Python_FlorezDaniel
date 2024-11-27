from Menu.mainMenu import mainMenu
from Menu.calcularImpuesto import taxesCalculator

while True:
    match mainMenu():
        case 1:
            taxesCalculator()
        case 2: pass
        case _: exit()