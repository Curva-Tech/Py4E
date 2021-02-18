fhand = open('mbox.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line Count:', count)

print("-----1-------")

fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    if line.startswith('From'):
        print(line)
        
print('------2-------')

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip() #removes \n
    if line.startswith('From'):
        print(line)
        
print('------3--------')

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()#removes \n
    if not line.startswith('From:'): 
        continue #if the line is not a "from" line then ignore and continue
    print(line)
    
print('------4--------')

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()#removes \n
    if line.find('@uct.ac.za') == -1: continue
    print(line)

    #-1 is returned if the string is not found
    
print('-------5-------')

fname = input("Enter file name:> ")
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)

print('-------6-------')

fname = input("Enter file name:> ")
try:
    fhand= open(fname)
except:
    print("file cannot be opened:", fname)
    exit()
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were,', count, 'subject lines in', fname)
        