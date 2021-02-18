#Exercise 1:
#Write a function called chop that takes a list and modifies it, removing the first
#and last elements, and returns None.

#Then write a function called middle that takes a list and returns a new list that
#contains all but the first and last elements.



list = [1,2,3,4,5]

def chop_list(t):
    list.pop(0)
    list.pop(3)
    
rest = chop_list(list)
print(rest)

print("----------")

list1 = [1,2,3,4,5]

def middle_list(t):
    del t[0]
    del t[3]
    print(t)
    
middle_list(list1)