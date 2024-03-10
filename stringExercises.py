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