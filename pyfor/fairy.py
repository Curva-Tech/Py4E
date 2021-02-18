def computegrade(score):
    if float(score) >= 0.9:
        grade = "A"
    elif float(score) >= 0.8:
        grade = "B"
    elif float(score) >= 0.7:
        grade = "C"
    elif float(score) >= 0.6:
        grade = "D"
    elif float(score) < 0.6:
        grade = "F"    
    return grade

score = float(input("What score did you get?"))

print("your result is:", computegrade(score))