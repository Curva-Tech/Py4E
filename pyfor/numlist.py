numlist = []


while True:
    num = input("Enter a number: ")
    numlist.append(num)
    print(numlist)
    
    if num == 'done':
        break
    
numlist.remove("done")

def min(numlist):
    smallest = None
    for num in numlist:
        if smallest is None or num < smallest:
            smallest = num
        return smallest

def max(numlist):
    largest = None
    for num in numlist:
        if largest is None or num > largest:
            largest = num
        return largest
    
    
print("Smallest:", min(numlist))
print("Largest:", max(numlist))


    
    
