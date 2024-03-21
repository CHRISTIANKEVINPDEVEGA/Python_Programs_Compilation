def parserline(linesofword):
    words = linesofword.split()
    print(words[1])

    
txtfile = input('Enter Filename: ')
try:
 linesOffile = open(txtfile)
 for lineOffile in linesOffile:
    linenospace = str(lineOffile.rstrip())
    if not linenospace.startswith('From '):
        continue
    parserline(linenospace)
except:
 print('File Not found')