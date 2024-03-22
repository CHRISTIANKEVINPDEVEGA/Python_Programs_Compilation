
weekdayCount = dict()
fhand = open('word.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    linelst = line.split()
    if linelst[2] in weekdayCount:
        weekdayCount[linelst[2]] += 1
    else:
        weekdayCount[linelst[2]] = 1

print(weekdayCount)

emailmesCount = dict()
fhand = open('word.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '):
        continue 
    linelst = line.split()
    if linelst[1] in emailmesCount:
        emailmesCount[linelst[1]] += 1
    else:
        emailmesCount[linelst[1]] = 1

lst = list()
for key,val in emailmesCount.items():
    lst.append((val,key))

lst.sort(reverse=True)
key,val = lst[0]
print(val,key)


# maxVal = None
# for keys in emailmesCount:
#     if maxVal is None or emailmesCount[maxVal] <= emailmesCount[keys]:
#         maxVal = keys

# print(maxVal,emailmesCount[maxVal])

# domainnameCount = dict()
# fhand = open('word.txt')
# for line in fhand:
#     line = line.rstrip()
#     if not line.startswith('From '):
#         continue
#     at_index = line.find('@')
#     at_space = line.find(" ",at_index)
#     domainname = line[(at_index+1):at_space]
#     if domainname in domainnameCount:
#         domainnameCount[domainname] += 1
#     else:
#         domainnameCount[domainname] = 1

# print(domainnameCount)