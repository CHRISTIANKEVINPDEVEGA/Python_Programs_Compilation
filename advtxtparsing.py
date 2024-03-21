import string

fname = input('Enter the filename: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened: ', fname)
    exit()

counts = dict()
for line in fhand:
    line = line.strip()
    line = line.translate(line.maketrans("","",string.punctuation))
    line = line.lower()
    words = line.split()
    
