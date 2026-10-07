def add(a:float, b:float)->float:
    """Add two numbers and return the result"""
    return a+b

def subtract(a:float, b:float)->float:
    """Subtracts two numbers and return the result"""
    return a-b

def multiply(a:float, b:float)->float:
    """Multiplies two numbers and return the result"""
    return a*b

def divide (a:float, b:float)->float:
    """Divides two numbers and return the result"""
    if b==0:
        raise ValueError("Cannot divide by zero")
    return a/b
while True:
    first_number=float(input("Enter first number"))
    operation=input("Choose operation(+,-,*,/")
    second_number=float(input("Enter second number"))


    if operation=="+":
        result=add(first_number, second_number)

    elif operation=="-":
        result=subtract(first_number, second_number)

    elif operation=="*":
        result=multiply(first_number, second_number)

    elif operation=="/":
        result=divide(first_number, second_number)

    else:
        result=None
        print("Invalid operation")

    if result is not None:
        print(result)
    again=input("Calculate again? (y/n)")
    if again=="n":
        break
    

assert add(2,3)==5
assert subtract(2,3)==-1
assert multiply(2,3)==6
assert divide(6,2)==3
assert add(2.5,3.5)==6
assert multiply(10,0)==0
