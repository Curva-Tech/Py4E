def computegrade(score):
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
    return grade

result = float(input("What score did you get?"))

final_result = computegrade(result)
print("your result is:", final_result)