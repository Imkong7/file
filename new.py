num = 101

sum = 100

def generateTable(num):
    for i in range(1, 11):
        print(f'{num} x {i} = {num*i}')
        
generateTable(5)