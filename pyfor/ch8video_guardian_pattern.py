han = open('mbox-short.txt')

for line in han:
    line = line.rstrip()
    #print('Line:', line)
    wds = line.split()
    #print('Words:', wds)
    
    #------Guardian pattern-----
    if len(wds) < 1:
        #print("Skip blank")
        continue
    if wds[0] != 'From' :
        #print("Ignore")
    #------_-------
        continue
    print(wds[2])
    
    
#Tidied up with guardian pattern on line 27.  

han = open('mbox-short.txt')

for line in han:
    line = line.rstrip()
    wds = line.split()
    if len(wds) < 3 or wds[0] != 'From' :
        continue
    print(wds[2])