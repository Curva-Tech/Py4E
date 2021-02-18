numlist = []

#def min(numlist):
    #smallest = None
    #for fv in numlist:
        #if smallest is None or fv < smallest:
            #smallest = fv
        #return smallest
    
#def min(numlist):
    #smallest = None
    #for fv in numlist:
        #if smallest is None or fv < smallest:
            #smallest = fv
        #return smallest

while True:
    num = input("Enter a number: ")
    
    if num == 'done':
        break
        
    try:
        fv = int(num)
    
    except:
        print('Invalid input')
        continue
    numlist.append(num)
    #print(numlist)    
    
print("maximum: ",max(numlist))
print("minimum: ",min(numlist))