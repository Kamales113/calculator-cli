def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def calculate():
     operation = input("The operation are +,-,*,/: ")
     print("Welcom to the calculator")
     print("the operation are +,-,*,/")
     print("If you wan to exit type exit")
     while True:
        if operation =="exit":
            break
        num1 = float(input("Enter the first Number:"))
        num2 = float(input("Enter the second Number:"))
        if operation =="+":
            print(add(num1,  num2))
        elif operation == "-":
            print(sub(num1,num2))
        elif operation == "*":
            print(mul(num1,num2))
        elif operation == "/":
            print(div(num1,num2))
        else:
            print("Invalid number")

if __name__ == "__main__":
    calculate()
