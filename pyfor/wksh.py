list1 = [1,2,3,4,5]

def middle_list(t):
    del t[0]
    del t[3]
    print(t)
    
middle_list(list1)

#Another way of doing it:

list1 = [1,2,3,4,5]

a = list1.pop(0)
b = list1.pop(3)
#print(a)
#print(b)
print(list1)