result = input("Enter Score:> ")

try:
    score = float(result)
    
    if float(result) >= 0.9:
        grade = "A"
    elif float(result) >= 0.8:
        grade = "B"
    elif float(result) >= 0.7:
        grade = "C"
    elif float(result) >= 0.6:
        grade = "D"
    elif float(result) < 0.6:
        grade = "F"    
    
    print("Your grade is:", grade)
    
except:
    print("please enter a number") 
    
