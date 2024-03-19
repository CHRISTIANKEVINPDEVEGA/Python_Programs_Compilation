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

a = [1,2,3]
b = [4,5,6]
c = a + b 
print(c)

print([0] * 4)
print([1,2,3,4] * 4)
t = ['a', 'b', 'c', 'd', 'f', 'g']
print(t[:1])
t[1:4] = ['j', 'k']
print(t)

t = ['a','b','c']
t.append('d')
print(t)

t1 =['a','b','c']
t2 = ['d', 'e', 'f']
t1.extend(t2)
print(t1)

t = ['a','c','d','b']
t.sort()
print(t)

t = ['a', 'b', 'c']
x = t.pop(2)
print(t)
print(x)
del t[1]
print(t)
t.remove('a')
print(t)

t =  ['a', 'b', 'c', 'd', 'e', 'f']
del t[1:3]
print(t)

nums = [3, 41, 12, 9, 74, 15]
print(max(nums))

nums = []

# while(True):
#     inp = input('Enter a value: ')
#     if inp == 'done': break
#     value = float(inp)
#     nums.append(value)

# average = sum(nums) / len(nums)
# print('Average: ', average)

# s = 'spam'
# lists= list(s)
# print(lists)

# liststr = 'i want to go home'
# newlist=liststr.split()
# print(newlist)

# listspam = 'spam-spam-spam'
# delimiter = '-'
# newspamlist = listspam.split(delimiter)
# print(newspamlist)
# newspamstr = delimiter.join(newspamlist)
# print(newspamstr)

# fhand = open('word.txt')

# for line in fhand:
#     line = line.rstrip()
#     if not line.startswith('From '):
#         continue
#     linesplitted = line.split()
#     print(linesplitted)

def delete_head(t):
    del t[0]

letters = ['a','b','c']
delete_head(letters)
print(letters)

t1 = [1,2]
t2 = t1.append(3)
print(t1)
print(t2)


t1 = [1,2]
t2 = t1 + [3]
print(t1 is t2)

def tail(t):
    return t[1:]

print(tail(t2))