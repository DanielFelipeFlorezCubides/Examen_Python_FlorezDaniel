from Menu.calcularImpuesto import taxesCalculator
import os
def listaImpuestos():
    while True:
        try:   
            print("""
            ---------------------------------------------------
                                TAXES KINDS
            ---------------------------------------------------
            1. IVA (10%)
            2. Special tax (5%)
            3. Local tax (8%)
            4. Other (Personalizable)""")
            
            print("""\n
            '''''''''''''''''''''''''''''''''''' 
            Do you want to calculate a tax?
            1. Yes (Go to taxes calculation)
            2. No (Go back to main menu)
            ''''''''''''''''''''''''''''''''''''
                """)
            
            option = int(input('Please choose one of the available options: '))
            if option == 1:
                taxesCalculator()
            elif option == 2:
                os.system('clear')
                break
            else: raise ValueError()
        except ValueError as e:
                    print('Invalid option. Please enter a number between 1 and 2.')