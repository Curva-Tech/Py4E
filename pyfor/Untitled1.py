def count(word,letter):
    count = 0
    for thing in word:
        if thing == letter:
            count = count + 1
    print(count)
        
input_word = input("What word?>: ")
input_letter = input("What letter?>: ")
    
count(input_word, input_letter)

