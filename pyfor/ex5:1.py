while True:
    
    
    try:
        inp = float(input("Enter a number> "))
        
        
    except ValueError:
        print("incorrect entry, enter a number please") 
        quit()