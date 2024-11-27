import json

def read_file(path):
        with open(f'Server/{path}', 'r') as file:
            data = file.read()
            convertList = json.loads(data)
            return convertList
    
def write_file(data, path):
    with open(f'Server/{path}', 'w') as file:
        convertJson = json.dumps(data, indent=4)
        file.write(convertJson)
        file.close()

def ivaTax(expense):
    operation = (expense * 0.1)
    return operation

def specialTax(expense):
    operationS = (expense * 0.05)
    return operationS

def localTax(expense):
    operationL = (expense * 0.08)
    return operationL

def otherTax(expense, other):
    otherConverted = (other / 100)
    operationO = (expense * otherConverted)
    return operationO

def storage(expense, tax):
    data = read_file('storagedData.json')
    formato = {
        "Expense": expense,
        "Tax": tax
    }
    data.append(formato)
    write_file(data, 'storagedData.json')
    return data