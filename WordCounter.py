
file = open("word.txt","r")
count = 0

for line in file:
    words = line.split(" ")
    for word in words:
        if word == "do":
            count += 1
file.close
print(f"Number of words: {count}")    


Counter = 0
file2 = open("word.txt","r")
file2r = file2.read()
file2.close()
schar = ",.!?“”()"

for SPchar in schar:
    if SPchar in file2r:
        file2r = file2r.replace(SPchar, " ")

words = file2r.split()

wordCount = {}

for word in words:
    if word == "to":
        Counter += 1

print(f"Word amountd: {Counter}")
