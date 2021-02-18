numlist = []

while True:
    num = input("Enter a number: ")
    
    if num == 'done':
        break
        
    try:
        fv = float(num)
    
    except:
        print('Invalid input')
        continue
    numlist.append(num)
    #print(numlist)    
    
print("maximum: ",max(numlist))
print("minimum: ",min(numlist))