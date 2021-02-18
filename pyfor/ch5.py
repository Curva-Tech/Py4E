n = 5
while n > 0:
    print(n)
    n = n - 1
print("Blastoff")

while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')

while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')

friends = ['joe', 'glenn', 'sally']
for friend in friends:
    print('Happy new year:', friend)
print('Done!')