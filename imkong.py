lists = ['apple', 'mango', 'banana', 'grapes']
length = len(lists)

def getFruits():
    word = 'm'
    for i in range(0,length):
        if word == lists[i][0]:
            print('This is lists')
