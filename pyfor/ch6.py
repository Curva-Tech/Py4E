while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('done!')

print("---------------")

while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')

print("---------------")

count = 0
for itervar in [3, 41, 29, 36, 51]:
    count = count + 1
print('Count: ', count)

total = 0
for itevar in [3, 41, 29, 36, 51]:
    total = total + itevar
print('Total: ', total)

print("---------------")

largest = None
print('Before:', largest)
for itervar in [3 , 41, 12, 9, 74, 15]:
    if largest is None or itervar > largest:
        largest = itervar
    print('Loop:', itervar, largest)
print('Largest:', largest)

smallest = None
print('Before:', smallest)
for itervar in [3 , 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
    print('Loop:', itervar, smallest)
print('Smallest', smallest)
        
print("---------------")

def min(values):
    smallest = None
    for value in values:
        if smallest is None or value < smallest:
            smallest = value
    return smallest

min(3)
