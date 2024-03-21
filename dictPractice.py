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