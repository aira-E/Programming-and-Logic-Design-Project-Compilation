#Create a program which you will enter the amount of money you have, it will also ask for the price of an apple. Display the maximum number of apples that you can buy and the remaining money that you will have. Display the output in the following format. You can buy ___ apples and your change is ___ pesos.
def money ():
    money_function = int (input("How much money do you have? "))
    return money_function

def apple_price ():
    apple_price_function = int (input("How much for an apple? "))
    return apple_price_function

def maximum_apples (output_money,output_apple_price):
    maximum_apples_function = (output_money/output_apple_price)
    return maximum_apples_function

def change (output_money,output_apple_price,output_maximum_apples):
    change_function = output_money-(output_apple_price*output_maximum_apples)
    return change_function

output_money = money ()
output_apple_price = apple_price ()
output_maximum_apples = maximum_apples (output_money,output_apple_price)
output_change = change (output_money,output_apple_price,output_maximum_apples)

print (f"You can buy {output_maximum_apples} apples, having {output_change} change")
