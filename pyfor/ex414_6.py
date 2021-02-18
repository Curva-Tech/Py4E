def computepay(hours,rate):
    if hours > 40:
        pay = ((rate * 1.5) * (hours - 40)) + 40 * rate
    else:
        pay = rate * hours
        
    return pay
    
hours = float(input("How many hours?"))
rate = float(input("What rate?"))

workout = computepay(hours, rate)

print("pay:", workout)


        