

import random                   #importing inbuilt "Random" function 

Q_no = 1
while Q_no<=10:
    n1 = random.randint(0,9)   #Using "randint" function to generate only random integers     
    n2 = random.randint(0,9)      
    product = int(input(f"\nfind the product of:\nQuestion{Q_no}: {n1} X {n2} = "))
    if product == (n1*n2):      #using f'strings' in above line to easily concatenate the values of variables into strings.
        print ("Right Answer")
    else:
        print ("Wrong! The answeer is ",n1*n2)
    Q_no+=1                     #to send next value to the loop to print next Question