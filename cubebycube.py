def cube(number):
    return number*number*number
def by_three(number):
    if number %3 == 0:
        return cube(number)
    else:
        print("false")

print(by_three(902))
print(by_three(688))