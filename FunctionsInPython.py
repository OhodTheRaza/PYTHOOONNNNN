def greet_customer():
    print("Hello Welcome to my Brand new lemonade stand. ")
    print("Come have a lemonade!")

price_per_cup = float(input("Enter the price of the lemonde cup in pkr: "))
cups_sold = int(input("Enter the number of cups Sold: "))

def calculate_price(price,cups):
    total = price*cups
    return total
total_cost = calculate_price(cups_sold,price_per_cup)

rounded_total = round(total_cost,2)
print("Total Cost: ", rounded_total)

amount_paid = float(input("Enter the amount of money you paid by the customer: "))
def calculate_change(paid,total):
    change = paid-total
    return change
change_due = calculate_change(amount_paid,rounded_total)
rounded_change = round(change_due,2)

def thankyou_msg(cups):
    if cups >= 5:
        print("Big Order! Thank You so much for the Support")
    else: 
        print("Thank You For coming to Our Stand!")