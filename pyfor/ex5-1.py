#sv = string value
#fv = float value
# on line 10 convert float to string!

num = 0
tot = 0.0
while True:
    sv = input("Enter a number> ")
    if sv == 'done':
        break
    try:
        fv = float(sv)
    except:
        print('Invalid input')
        continue
    print(fv)
    num = num +1
    tot = tot + fv
print("done")
print(tot,num,tot/num)
        