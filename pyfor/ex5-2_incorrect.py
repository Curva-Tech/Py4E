largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == 'done':
        break
    try:
            fv = float(num)
    except:
        print('Invalid input')
        continue
    
        print(num)
    
    print("maximum",num, largest)
    print("minimum",num, smallest)