def mainMenu():
    while True:
        try:
            print("""
    ---------------------------------------------------
                TAXES CALCULATOR MENU
    ---------------------------------------------------
    Choose an option:
    1. Calculate product or service's tax
    2. Show tax kind list
    3. Exit
    ---------------------------------------------------""")
            
            options = int(input('Please choose one of the available options: '))
            if 1 <= options <= 2:
                return options
            elif options == 3:
                print('''
    ===============================================
    Thanks for using the taxes calculator, see you!
    ===============================================''')
                break
            else:
                raise ValueError()
        except ValueError as e:
                    print('Invalid option. Please enter a number between 1 and 3.')