txtfile = input('Enter Filename: ')
try:
 lineOffile = txtfile.open()
except:
 print('File Not found')