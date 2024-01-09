#Create a program that will ask for name, age and address. Display those details in the following format. Hi, my name is _____. I am ____ years old and I live in _____ .
def name ():
    name_function = input ("What is your name? ")
    return name_function

def age ():
    age_function = int (input ("How old are you? "))
    if age_function >= 18:
        print ("You are on the legal age")
    else:
        print ("You are underage")
    return age_function

def address ():
    address_function = input ("Where do you live? ")
    return address_function
    
output_name = name ()
output_age = age ()
output_address = address ()

print (f"Hi! I am {output_name}, I am {output_age} years old, and I live in {output_address}")
