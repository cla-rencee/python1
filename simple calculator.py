def add(x,y):
    print(x+y)

def subtract(x,y):
    print(x-y)

def multiply(x,y):
    print(x*y)

def divide(x,y):
    if y==0:
        return "Error cannot divide by zero"
    print(x/y)

def calculator():
    print("Simple calculator")
    print("Select operation")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Off")

    while True:
        choice=input("Enter choice(1/2/3/4/5)")

        if choice in['1','2','3','4','5']:
            num1=float(input("Enter first number:"))
            num2=float(input("Enter second number:"))

            if choice=='1':
                print(f"The answer is:", {add(num1,num2)})
                add(num1,num2)
            elif choice=='2':
                print(f"The answer is:", {subtract(num1,num2)})
                subtract(num1,num2)
            elif choice=='3':
                print(f"The answer is:", {multiply(num1,num2)})
                multiply(num1,num2)
            elif choice=='4':
                print(f"The answer is:", {divide(num1,num2)})
                divide(num1,num2)
            elif choice=='5':
                print(f"Off")
            else:
                print(f"Invalid input")


add(999,888)




