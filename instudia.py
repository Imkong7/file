def getMultiply(a,b):
    return a *b

def getTable(num):
    for i in range(0,11):
        result = getMultiply(num, i)
    print(f'{num} x {i} = {result}')
    
getTable(5)

lists = ['apple', 'mango', 'banana']