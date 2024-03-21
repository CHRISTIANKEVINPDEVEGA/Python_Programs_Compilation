def parserline(linesofword):
    linenospace = linesofword.rstrip()
    words = linenospace.split()
    print(words[2])

    
txtfile = input('Enter Filename: ')
try:
 lineOffile = txtfile.open()
except:
 print('File Not found')