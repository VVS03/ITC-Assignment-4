#Q2
year = int (input("Enter the year you want to check : "))

if year%100==0:                                  
    if year%400==0:
        print(f"{year} is a leap Year.")
    else:
        print(f"{year} is not a leap Year.")


else:
    if year % 4 == 0:
       print(f"{year} is a leap Year.")
    else: 
        print(f"{year} is not a leap Year.")