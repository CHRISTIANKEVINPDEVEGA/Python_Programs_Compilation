
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