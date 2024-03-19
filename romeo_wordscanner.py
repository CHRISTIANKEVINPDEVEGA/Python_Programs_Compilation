title_name = input('Enter file: ')
fhand = open(title_name)

unique_words = []

for line in fhand:
    line = line.rstrip()
    word_list = line.split()
    for word in word_list:
        if len(unique_words) == 0:
            unique_words.append(word)
        else:
            if word not in unique_words :
                unique_words.append(word)
            else:
                continue

unique_words.sort()

print(unique_words)