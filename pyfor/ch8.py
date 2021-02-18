total = 0
count = 0
while True:
    inp = input("Input a number: ")
    if inp == 'done': break
    value = float(inp)
    total = total + value
    count = count + 1
average = total / count
print('Average:', average)

print("----1-----")

numlist = list()
while True:
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(inp)
    numlist.append(value)
    print(numlist)
average = sum(numlist)/len(numlist)
print('Average', average)

print("----2-----")

fhand = open ('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    print(words[2])
    
print("----3-----")
