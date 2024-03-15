fout = open('output.txt', 'w')
print(fout)

line1 = 'this is the'
print(fout.write(line1))

line2 = 'this is rain rain'
print(fout.write(line2))

fout.close()

# Exercise one
input = input('Enter a filename: ')

try:
    uphand = open(input)
except:
    print('Invalid name')
    exit()

for line in uphand:
    print(line.upper())

