def parserline(linesofword):
    words = linesofword.split()
    print(words[1])

    
txtfile = input('Enter Filename: ')
count = 0
try:
    linesOffile = open(txtfile)
    for lineOffile in linesOffile:
        linenospace = str(lineOffile.rstrip())
        if not linenospace.startswith('From '):
            continue
        parserline(linenospace)
        count += 1
    print('There were',count,'lines in the file with From as the first word')
except:
 print('File Not found')