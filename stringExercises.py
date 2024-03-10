fruit = "banana"
print(fruit[1])

letter = fruit[0]
print(letter)

print(len(fruit))

length = len(fruit)
last = fruit[length-1]
print(last)

index = 0
while index < len(fruit):
    print(fruit[index])
    index += 1

index = len(fruit)
while index > 0:
    print(fruit[index-1])
    index -= 1

s = 'monthy python'
print(s[0:5])
print(s[7:13])

fruit = "banana"
fthree = fruit[:3]
print(fthree)
lthree = fruit[3:]
print(lthree)
mthree = fruit[3:3]
print(mthree)

print(fruit[:])

greeting = 'Hello, world!'
new_greeting = 'J' + greeting[1:]
print(new_greeting)