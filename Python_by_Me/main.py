# Variable =  A container for a value (String, Integer, Float, Boolean)
#             A variable behaves as if it was the value it contains 


# String = A sequence of characters
# first_name = "Bro"
# food = "pizza"
# email = "Bro123@fake.com"

# print(first_name)
# print(f"hello {first_name}")
# print(f"I like {food}")
# print(f"Your Email is {email}")


#Integer = A whole number

# age = 30 
# quantity = 3
# print(f"Your age is {age}")
# print(f"You have {quantity} pizzas")


#Float = A number with a decimal point

# price = 19.99
# tax = 0.07

# print(f"price of this bicyle is ${price}")
# print(f"tax on this bicycle is ${tax}")




#Boolean = A true or false value
# is_hungry = True
# is_tired = False
# for_sale = False
#  print(f"Are you hungry? {is_hungry}")
#  print(f"Are you tired? {is_tired}")









# Typecasting = The process of converting a value of one data type to another 

#              Explicit  vs Implicit


# name = "Bro"
# age = 30
# gpa = 1.9
# student = True

# Explicit Typecasting
# age = float(age)
# print(type(age))
# print(type(name))
# print(type(age))
# print(type(gpa))
# print(type(student))


# Implicit Typecasting
# age = age + 5
# print(type(age)) # this will be an integer 

# x = 2
# y = 3.5

# x = x +y
# print(x)
# print(type(x)) #this will be a float because y is a float and x is an integer 

# x = 0.5
# y = 1

# y = y + x
# print(type(y))










# Input
# name = input("Enter your name:")
# age = int(input("Enter your age:"))
# age += 1
# print(f"hello {name}")
# print(f"your age is {age}")






# Arithmetic Operators in Python

# a = 10
# b = 3

# # 1. Addition
# add = a + b
# print("Addition:", add)  # Output: 13

# # 2. Subtraction
# sub = a - b
# print("Subtraction:", sub)  # Output: 7

# # 3. Multiplication
# mul = a * b
# print("Multiplication:", mul)  # Output: 30

# # 4. Division
# div = a / b
# print("Division:", div)  # Output: 3.333...

# # 5. Floor Division
# floor_div = a // b
# print("Floor Division:", floor_div)  # Output: 3

# # 6. Modulus
# mod = a % b
# print("Modulus:", mod)  # Output: 1

# # 7. Exponentiation
# exp = a ** b
# print("Exponentiation:", exp)  # Output: 1000


# a = 10
# b = 3

# a += b
# print("a += b:", a)  # 13

# a -= b
# print("a -= b:", a)  # 10

# a *= b
# print("a *= b:", a)  # 30

# a /= b
# print("a /= b:", a)  # 10.0

# a //= b
# print("a //= b:", a)  # 3.0

# a %= b
# print("a %= b:", a)  # 0.0

# a = 2
# a **= b
# print("a **= b:", a)  # 8



# x = 3.14
# y = -4
# z = 5
# result = round(x)    t
# result = abs(y)
# result = pow(4,3)
# result = max(x,y,z)
# result = min(x,y,z)
# print(result)






import math
# x = 9.9
# print(math.pi)
# print(math.e)

# result = math.sqrt(x)
# result = math.ceil(x)
# result = math.floor(x)
# print(result)



# radius = float(input("Enter the radius of circle"))
# area = math.pi * pow(radius,2)
# print(f"The area of circle is :{area}cm")






# circumference = 2 * math.pi * radius

# print(f"the circumference of circle is :{round(cirumference, 2)} cm")












# if = Do some code onlt IF some condition is True
#        Else  do something else



# age  = int(input("Enter your age"))

# if age>= 18:
#     print("You are eligible for vote")
# elif age < 0 :
#     print("Invalid age")

# else:
#     print("You are not eligible for vote")




# Pyhton Calculator
# operator = input("Enter an operator (+, -, *, /):")
# num1 = int(input("Enter first number:"))
# num2 = int(input("Enter second number:"))

# if operator == "+":
#     result = num1 + num2
#     print(result)
# elif operator == "-":
#     result = num1 - num2
#     print(result)
# elif operator == "*":
#     result = num1 * num2
#     print(result)
# elif operator == "/":
#     result = num1 / num2
#     print(result)
# else:
# print(f"{operator} is not valid")






# Python Weight converter


# weight = float(input("Enter your weight"))
# unit = input("kilograms or Pounds? (k  or  l):")

# if unit  == "k":
#    weight = weight * 2.205
#    unit = "Lbs."
# elif unit == "l":
#    weight = weight / 2.205
#    unit = "kgs."
# else:
#    print(f"{unit} was not valid")

# print(f"Your Weight is : {round(weight,3)} {unit}")






# logical operators = evaluate multiple conditions ( or, and ,not)
#                 or  = at least one condition must be true
#                and  = both condtions are true
#                not  = invetrs the condtion (not false , not true)



# temp = 36
# is_raining = False

# if temp > 35 or temp < 0 or is_raining:
#     print("the outdoor event is cancelled")

# else:
#     print("the outdoor event is on")






# Conditional Expression =  A one-line shortcur for the if-else statement (ternary operator )
#                         Print or assign one of two values based on a condition
#                         X if condition else Y





# num =  5 
# a = 6
# b = 7
# age = 19
#

# print("Psitive" if num>0 else "Negative")
# print("EVEN" if num % 2 == 0 else "ODD" )
# max_num = a if a>b else b
# print(max_num)
# min_num =  a if a<b else b
# print(min_num)
# status = "Adult" if age>=18 else "Child"
# print(status)












# String Methods

# name  = input("Enter your full name:")
# phone_number = int(input("Enter your phoner number:"))
# result = len(name)
# print(result)
# result = name.find("t")
# print(result)
# result = name.rfind("k")
# print(result)
# name = name.capitalize()
# print(name)
# name = name.upper()
# print(name)
# name = name.lower()
# print(name)
# result = name.isdigit()
# result = name.isalpha()
# result = phone_number.count("-")
# phone_number = phone_number.replace("-", " ")
# print(phone_number)






