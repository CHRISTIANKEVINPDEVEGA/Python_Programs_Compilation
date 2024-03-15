fout = open('output.txt', 'w')
print(fout)

line1 = 'this is the'
print(fout.write(line1))

line2 = 'this is rain rain'
print(fout.write(line2))

fout.close()

# Exercise 1
# input = input('Enter a filename: ')

# try:
#     uphand = open(input)
# except:
#     print('Invalid name')
#     exit()

# for line in uphand:
#     print(line.upper().rstrip())


# Exercise 2

# input2 = input('Enter a filename: ')

# try:
#     uphand2 = open(input2)
# except:
#     print('Invalid name')
#     exit()

# count = 0
# floatcount = 0

# for line in uphand2:
#     if line.startswith('X-DSPAM-Confidence:'):
#         count += 1
#         icolon = line.find(':')
#         floatval = float(line[(icolon+1):])
#         floatcount += floatval

# floatavg = floatcount/count
# print('Average spam confidence: ', floatavg)

# Exercise 3

fname = input("Enter a  filename: ")
try:
    fhand3 = open(fname)

except:
    if fname == 'na na boo boo':
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
    else:
        print('Filename', fname,  'cannot be found')
    exit()

count = 0
for line in fhand3:
    if line.startswith('Subject: '):
        count += 1
print('There were', count, 'Subject lines in ', fname)
