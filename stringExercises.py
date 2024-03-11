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

word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count += 1
print(count)

def count(word, letter):
    count = 0
    for wordletter in word:
        if letter == wordletter:
            count += 1
    print(f"The number of '{letter}' in {word} is {count}")

# word = input("Enter a word ")
# letter = input("Enter a letter ")
# count(word,letter)
    
print('a' in 'banana')
print('seed' in 'banana')

if word == 'banana':
    print('All right, banana.')

word = 'Pineapple'

if word < 'banana':
    print(f'Your word, {word}, comes before banana')
elif word > 'banana':
    print(f'Your word, {word}, comes after banana')
else:
    print('All right, banana.')   

stuff = 'Hello World'
print(type(stuff))
print(dir(stuff))
print(help(str.capitalize))

word = 'banana'
new_word = word.upper()
print(new_word)