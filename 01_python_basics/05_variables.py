# variables: objects containing specific values
x=5 #numeric or integer variable
print(x) 

y=("Learning python with Tehreem") #string variable
print(y)

x=x+20
print(x)

#type/class of variable

type(x) #function to check the type of variable

print(type(x)) #class integer
print(type(y)) #class string


#Rules to assign a variable
#1- The variable should contain only letters, numbers, and underscores
#2- Do not start the variable name with a number
#3- Do not use Python keywords as variable names (break, mean, meadian, test, etc.)
#4- Variable names are case-sensitive (lowercase and uppercase letters_lowercase letters should be used))
#5- Short and descriptive 
#6- Variable names should not contain spaces (use underscores instead)

fruit_basket='Mangoes, Bananas, Apples, Oranges'
print(fruit_basket)
print(type(fruit_basket)) #class string

fruit_basket=(8) #numeric variable
#del fruit_basket #delete the variable. It shows codes have been updating as we move down the code.
#  It will show error if we try to print the variable after deleting it.
print(fruit_basket)
print(type(fruit_basket)) #class integer
