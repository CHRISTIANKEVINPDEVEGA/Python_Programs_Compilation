eng2sp = dict()
print(eng2sp)
eng2sp['one'] = 'uno'
print(eng2sp)

eng2sp = {'one':'uno', 'two':'dos', 'three':'tres'}
print(eng2sp['two'])
print(len(eng2sp))
print('one' in eng2sp)
print('uno' in eng2sp.values())
print(type(list(eng2sp.values())))


dict_wordtxt = {}
linestxt = open('words.txt')
for line in linestxt:
    line = line.rstrip()
    words_line = line.split()
    for word in words_line:
        if len(dict_wordtxt) == 0:
            dict_wordtxt[word] = len(word)
        if word in dict_wordtxt:
            continue
        else:
            dict_wordtxt[word] = len(word)

print(dict_wordtxt)

word = 'brontosaurus'
dic = dict()
for letter in word:
    if len(dic) == 0 or letter not in dic:
        dic[letter] = 1
        continue
    elif letter in dic:
        dic[letter] += 1

print(dic)
print(dic.get('b',0))
print(dic.get('z',0))

word = 'brontosaurus'
dic = dict()
for letter in word:
    dic[letter]=dic.get(letter,0) + 1

print(dic)
print(dic.get('z',6))

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened: ', fname)
    exit()

counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
print(counts)