fout = open('output.txt', 'w')
print(fout)

line1 = 'this is the'
print(fout.write(line1))

line2 = 'this is rain rain'
print(fout.write(line2))

fout.close()