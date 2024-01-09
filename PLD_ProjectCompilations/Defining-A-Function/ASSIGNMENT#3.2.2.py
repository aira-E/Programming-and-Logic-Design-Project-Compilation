#Create a program that will ask how many apples and oranges you want to buy. Display the total amount you need to pay if apple price is 20 pesos and orange is 25. Display the output in the following format. The total amount is ______.
def apple ():
    apple_function = int (input ("How many apples you wish to buy? "))
    return apple_function

def orange ():
    orange_function = int (input ("How many oranges you wish to buy? "))
    return orange_function

def apple_price (output_apple):
    apple_price_function = output_apple*20
    return apple_price_function

def orange_price (output_orange):
    orange_price_function = output_orange*25
    return orange_price_function

def total (output_apple_price,output_orange_price):
    total_function = output_apple_price + output_orange_price
    return total_function
    
output_apple = apple ()
output_orange = orange ()
output_apple_price = apple_price (output_apple)
output_orange_price = orange_price (output_orange)
output_total = total (output_apple_price,output_orange_price)

print (f"the total of your groceries cost {output_total} pesos")
