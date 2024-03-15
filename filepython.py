fhand = open('word.txt')
print(fhand)

stuff = 'Hello\nWorld'
print(stuff)
print(len(stuff))

fhand = open('word.txt')
count = 0
for line in fhand:
    count = count + 1

print(count) 

fhand = open('word.txt')

count = 0

for line in fhand:
    print(line.strip())
    count += 1 
    if count == 2:
        break    

fhand = open('word.txt')
inp = fhand.read()
print(len(inp))
print(inp[:20])

fhand = open('word.txt')
for line in fhand:
    if line.startswith("From"):
        print(line.rstrip())

fhand = open("word.txt")
for line in fhand:
    line = line.rstrip()
    if not line.startswith("From:"):
        continue
    print(line)

fhand = open('word.txt')
for line in fhand:
    line = line.rstrip()
    if line.find('@uct.ac.za') == -1:
        continue
    print(line)

fname = input("Enter a  filename: ")
try:
    fhands = open(fname)

except:
    print('Filename', fname,  'cannot be found')
    exit()

count = 0
for line in fhands:
    if line.startswith('Subject: '):
        count += 1
print('There were', count, 'Subject lines in ', fname)

