
file = open('romeo.txt')
#print(file)
word_list = []
for line in file: #checks each line in file
    for words in line.split(): #checks each word in line
        #print("-----")
        if words in word_list: continue # checks if word in list
        else:
            word_list.append(words) # puts word in list
            #print(word_list)
#print("------------")
word_list.sort() # sorts list alphabetically
print (word_list)
