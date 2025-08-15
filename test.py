num1=float(input("enter first number:"))
num2=float(input("enter second number:"))
ptint("1.addition")
print("2.subtraction")
choice=input("enter choice (1/2):")
if choice=="1":
    print("result:",num1 + num2)
    elif choice=="2":
        print("result:",num1 - num2)
        else:
            print ("invalid character")