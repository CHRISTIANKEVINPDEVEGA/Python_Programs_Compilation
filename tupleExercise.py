t = ('a','b','c','d','e')
t1 = ('a',)
print(type(t))
t=tuple('ldwacawd')
print(t[1:3])
t = ('A',)+t[1:]
print(t)
print((0,1,2)<(0,3,4))
print((0,1,500)<(0,3,4))

txt = 'but soft what light in yonder window breaks'
words = txt.split()
t = list()
for word in words:
    t.append((len(word),word))
print(t)
t.sort(reverse=True)
print(t)
res = list()
for length, word in t:
    res.append(word)

print(res)

m = ('have','Fun')
x,y = m
print(x)
print(y)
x,y=y,x
print(x)
print(y)
a, b = (1, 2), 3
print(a)
print(b)

addr = 'monty@python.org'
uname, domain = addr.split("@")
print(uname)
print(domain)

d = {'b':1,'a':10,'c':22}
t = list(d.items())
print(t)
t.sort()
print(t)

d = {'a':10, 'b':1, 'c':22}
for key, val in d.items():
    print(key,val)

d = {'a':10, 'b':1, 'c':22}
l = list()
for key, val in d.items():
    l.append((val,key))

l.sort(reverse=True)

print(l)


import string
wordsCount = {}
punc = string.punctuation
fhand = open('romeo.txt')
for line in fhand:
    line = line.translate(str.maketrans("","",punc))
    line = line.lower()
    linelst = line.split()
    for word in linelst:
        if word not in wordsCount:
            wordsCount[word] = 1
        if word in wordsCount:
            wordsCount[word] += 1 
lsts = list()
for key, val in wordsCount.items():
    lsts.append((val,key))

lsts.sort(reverse=True)

for key, val in lsts[:10]:
    print(key,val)