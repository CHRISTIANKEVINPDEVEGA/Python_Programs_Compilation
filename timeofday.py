fhand = open('word.txt')
dicttime = dict()
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    linelst = line.split()
    if line[1] 
