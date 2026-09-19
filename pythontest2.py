usernumber1 = input("Enter a number: ")
usernumber2 = input("Enter a number: ")
def addition(a,b):
    result =  a + b 
    print(result)
try:
    addition(usernumber1,usernumber2)
except ValueError:
    print("You Put Letters")
except ZeroDivisionError:
    if result %2 == 0 :
        print("Ok good")

def subtraction(a,b):
    result = a - b 
    print(result)
try:
    subtraction(usernumber1,usernumber2)
except ValueError:
    print("You Put Letters")
except ZeroDivisionError:
    if result %2 == 0 :
        print("Ok good")
