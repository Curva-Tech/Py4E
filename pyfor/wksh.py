han = open('mbox-short.txt')

for line in han:
    line = line.rstrip()
    #print('Line:', line)
    wds = line.split()
    #print('Words:', wds)
    if len(wds) < 3 or wds[0] != 'From' :
        #print("Skip blank")
        continue
    print(wds[2])