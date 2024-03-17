[10,20,30,40]
['hard','boiled','cheese']

['spam',[1,2,3,4],5,2.6]

[]

cheese = ['cheddar','Edam','Gouda']
numbers = [0,1,2,3,4]
empty = []

print(cheese,numbers,empty)

print(cheese[0])

cheese[1] = 'Eden'

print(cheese)

print('Eden' in cheese)

for cheeses in cheese:
    print(cheeses)

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2

print(numbers)

for x in empty:
    print('this never happened')