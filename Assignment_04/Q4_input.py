#Question_4

for n in range (0,200):                                    #since the candy is less than 200
    if (n-2)%5==0 and (n-3)%6==0 and (n-2)%7==0 :          #conditions given in Question
        print (f"There are {n} candy pieces in the bowl.") #using f'strings to substitute the value of "n"
    else:
        pass                                               #to check for further number
