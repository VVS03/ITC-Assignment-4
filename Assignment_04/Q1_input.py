marks = int(input("Enter your Total Marks : "))

if marks<=100:
    print("Your grade is A")
elif marks<80:
    print("Your grade is B")
elif marks<60:
    print("Your grade is C")
elif marks<50:
    print("Your grade is D")
elif marks<45:
    print("Your grade is E")
elif marks<25:
    print("Your grade is F")
else :
    print("You are entering incorrect marks.")