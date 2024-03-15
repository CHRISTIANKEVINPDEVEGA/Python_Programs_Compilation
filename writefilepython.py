fout = open('output.txt', 'w')
print(fout)

line1 = 'this is the'
print(fout.write(line1))

line2 = 'this is rain rain'
print(fout.write(line2))

fout.close()

# Exercise 1
input = input('Enter a filename: ')

try:
    uphand = open(input)
except:
    print('Invalid name')
    exit()

for line in uphand:
    print(line.upper().rstrip())


# Exercise 2

input2 = input('Enter a filename: ')

try:
    uphand2 = open(input2)
except:
    print('Invalid name')
    exit()

count = 0
floatcount = 0

for line in uphand2:
    if line.startswith('X-DSPAM-Confidence:'):
        count += 1
        icolon = line.find(':')
        floatval = float(line[(icolon+1):])
        floatcount += floatval

floatavg = floatcount/count
print('Average spam confidence: ', floatavg)