file = open('romeo.txt')

for line in file:
    line = line.rstrip()
    wds = line.split()
    wds.sort()
    print(wds)

