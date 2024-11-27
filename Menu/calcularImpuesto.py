from Formula.logic import ivaTax, specialTax, localTax, otherTax, storage
def taxesCalculator():
    while True:
        try:
            print("""
    ---------------------------------------------------
                    TAXES CALCULATOR
    ---------------------------------------------------
    """)
            expense = float(input("Please type the product or service's ammount: "))
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
                print(f"""
    ---------------------------------------------------
                RESULTADO DEL CÁLCULO
    ---------------------------------------------------
    Base ammount: $[{expense}]
    Tax: $[{iva}]
    Total with taxes: $[{expense + iva}]""")
                
                option = int(input("\nType '1' to save or '0' to cancel: "))
                if (option == 1):
                    storage(expense, iva)
                    print('Expense successfully saved!')
                elif (option == 0):
                    print('Operation cancelled.')
            elif taxOptions2 == 2:
                special = specialTax(expense)
                print(f"""
    ---------------------------------------------------
                RESULTADO DEL CÁLCULO
    ---------------------------------------------------
    Base ammount: $[{expense}]
    Tax: $[{special}]
    Total with taxes: $[{expense + special}]""")
                
                option = int(input("\nType '1' to save or '0' to cancel: "))
                if (option == 1):
                    storage(expense, special)
                    print('Expense successfully saved!')
                elif (option == 0):
                    print('Operation cancelled.')
            elif taxOptions2 == 3:
                local = localTax(expense)
                print(f"""
    ---------------------------------------------------
                RESULTADO DEL CÁLCULO
    ---------------------------------------------------
    Base ammount: $[{expense}]
    Tax: $[{local}]
    Total with taxes: $[{expense + local}]""")
                
                option = int(input("\nType '1' to save or '0' to cancel: "))
                if (option == 1):
                    storage(expense, local)
                    print('Expense successfully saved!')
                elif (option == 0):
                    print('Operation cancelled.')
            elif taxOptions2 == 4:
                other = float(input("Please type the other tax percentage: "))
                otherResult = otherTax(expense, other)
                print(f"""
    ---------------------------------------------------
                RESULTADO DEL CÁLCULO
    ---------------------------------------------------
    Base ammount: $[{expense}]
    Tax: $[{otherResult}]
    Total with taxes: $[{expense + otherResult}]""")
                
                option = int(input("\nType '1' to save or '0' to cancel: "))
                if (option == 1):
                    storage(expense, otherResult)
                    print('Expense successfully saved!')
                elif (option == 0):
                    print('Operation cancelled.')
            else: raise ValueError()

                    
            print("""
    ===============================
    Do you wish to do it again?
    1. Yes
    2. No
    ===============================
    """)
            decission = int(input("Please select an option: "))
            if decission == 2:
                break
            if decission == 1:
                pass
            
        except ValueError as e:
            print("\nInvalid option. Please enter a number between 1 and 4.")