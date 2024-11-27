from Formula.logic import ivaTax, specialTax, localTax, otherTax, storage
import os
def taxesCalculator():
    while True:
        try:
            print("""
    ---------------------------------------------------
                    TAXES CALCULATOR
    ---------------------------------------------------
    """)
            expense = float(input("Please type the product or service's ammount: "))
            totalTax = 0
            while True:
                print("""
    ---------------------------------------------------
    Select the tax kind:
    1. IVA (10%)
    2. Special tax (5%)
    3. Local tax (8%)
    4. Other tax
    ---------------------------------------------------""")
                        
                taxOptions2 = int(input("Please choose an option: "))
                    
                if taxOptions2 == 1:
                    iva = ivaTax(expense)
                    totalTax += iva
                    total = expense + totalTax
                    print(f"""
        ---------------------------------------------------
                    RESULTADO DEL CÁLCULO
        ---------------------------------------------------
        Base ammount: $[{expense}]
        Tax: $[{iva}]
        Total with taxes: $[{total}]""")
                elif taxOptions2 == 2:
                    special = specialTax(expense)
                    totalTax += special
                    total = expense + totalTax
                    print(f"""
        ---------------------------------------------------
                    RESULTADO DEL CÁLCULO
        ---------------------------------------------------
        Base ammount: $[{expense}]
        Tax: $[{special}]
        Total with taxes: $[{total}]""")
                elif taxOptions2 == 3:
                    local = localTax(expense)
                    totalTax += local
                    total = expense + totalTax
                    print(f"""
        ---------------------------------------------------
                    RESULTADO DEL CÁLCULO
        ---------------------------------------------------
        Base ammount: $[{expense}]
        Tax: $[{local}]
        Total with taxes: $[{total}]""")
                elif taxOptions2 == 4:
                    other = float(input("Please type the other tax percentage: "))
                    otherResult = otherTax(expense, other)
                    totalTax += otherResult
                    total = expense + totalTax
                    print(f"""
        ---------------------------------------------------
                    RESULTADO DEL CÁLCULO
        ---------------------------------------------------
        Base ammount: $[{expense}]
        Tax: $[{otherResult}]
        Total with taxes: $[{total}]""")
                else: raise ValueError()
                
                addMore = int(input('''\n
    ==============================================
    Do you want to sum another tax?
    1. Yes
    2. No
    ==============================================:\n'''))
                if addMore == 1:
                    pass
                elif addMore == 2:
                    break
                else: raise ValueError()
                
                
            option = int(input("\nType '1' to save or '2' to cancel: "))
            if (option == 1):
                storage(expense, totalTax, total)
                print('Expense successfully saved!')
            elif (option == 2):
                print('Operation cancelled.')
            else: raise ValueError()
                        
            print("""
    ===============================
    Do you wish to do it again?
    1. Yes
    2. No
    ===============================""")
            decission = int(input("Please select an option: "))
            if decission == 2:
                os.system('clear')
                break
            if decission == 1:
                pass
                
        except ValueError as e:
            print("\nInvalid option. Please enter a number between 1 and 4. Or 1 and 2.")