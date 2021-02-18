count = 0
total = 0

filename = input('Enter filename:> ')

try:
    contents = open(filename)
    
except:
    if filename == 'na na boo boo':
            print("Fuck You!")
            quit()
    else:
        print('File not found', filename)
        quit()
    

for line in contents:
    if line.startswith('X-DSPAM-Confidence:'): 
        count = count + 1
        #print(count)
        pos = line.find(':')
        #print(pos)
        number = float(line[pos + 1:].strip())
        #print(number)
        total = total + number
        #print(total)
print('Count is:> ',count)
print('Total is:> ',total)
        
ave = total/count
print('Average Spam Confidence is:>',ave)
        



    
