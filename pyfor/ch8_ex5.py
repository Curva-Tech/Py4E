#Exercise 5: Write a program to read through the mail box #data and when you
#find line that starts with “From”, you will split the line into words using the split
#function. We are interested in who sent the message, which is the second word on
#the From line.
#From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
#You will parse the From line and print out the second word for each From line,
#then you will also count the number of From (not From:) #lines and print out a
#count at the end.

file = open("mbox-short.txt")
count = 0

for line in file:
    line = line.split()
    if len (line) < 1: continue # exclude blank lines
    if line[0] != 'From': continue # exclude lines not starting with 'From"
    if line[0] == 'From': #count lines starting with 'From'
        count = count + 1
    print(line[1]) # print second word in lines starting with 'From'
    
print("There are:", count, "lines starting with From")
    
    
    