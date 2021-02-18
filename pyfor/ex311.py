h = 45
h1 = 40
r = 10

payt = h1 * 10
print("Normal time equals:", payt)

if h > 40:
    ot = ((h%h1) * 10) * 1.5
    print(ot)
    
pay = payt + ot
print("Total incl OT equals:",pay)


# exercise 3.11/2

inputH = input("Enter Hours:> ")
try:
    hours = float(inputH)
except:
    print("Please enter a number dickhead!")

inputR = input("Enter Rate:>")
try:
    rate = float(inputR)
except:    
    print("Please enter a number dickhead!")
    
    
# exercise 3.11/3

result = input("Enter Score:> ")

try:
    score = float(result)
    
    if float(result) >= 0.9:
        grade = "A"
    if float(result) >= 0.8:
        grade = "B"
    if float(result) >= 0.7:
        grade = "C"
    if float(result) >= 0.6:
        grade = "D"
    if float(result) < 0.6:
        grade = "F"    
    
    print("Your grade is:", grade)
    
except:
    print("please enter a number") 




    
   

