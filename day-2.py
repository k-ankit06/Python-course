# **Python Basic Concepts with Examples**

# ---

# ### 1. `input()` Function

# **Definition:** Used to take input from the user. Always returns data as a **string**.

# ```python
# name = input("Enter your name: ")
# print("Hello,", name)
# ```

# ---

# ### 2. `type()` Function

# **Definition:** Used to find the **data type** of a variable.

# ```python
# x = 10
# print(type(x))  # Output: <class 'int'>
# ```

# ---

# ### 3. Variable and Concatenation

# **Variable:** A named container to store data.

# **Concatenation:** Joining two or more strings using `+` operator.

# ```python
# first_name = "Ankit"
# last_name = "Kumar"
# full_name = first_name + " " + last_name
# print("Full Name:", full_name)
# ```

# ---

# ### 4. Data Type Conversion (Type Casting)

# **Definition:** Converting one data type into another.

# ```python
# a = "5"
# b = int(a)     # String to int
# print(b + 3)   # Output: 8

# x = 3.14
# y = str(x)     # Float to string
# print("Value is " + y)
# ```

# ---

# ### 5. `len()` Function

# **Definition:** Returns the number of items in an object (like string, list).

# ```python
# text = "Hello World"
# print(len(text))  # Output: 11
# ```

# ---

# ### 6. `count()` Function

# **Definition:** Returns the number of times a value appears in a string or list.

# ```python
# text = "banana"
# print(text.count("a"))   # Output: 3
# print(text.count("na"))  # Output: 2
# ```

# ---

# ### 7. Iterating vs Non-Iterating Objects

# **Iterable:** An object capable of returning its elements one by one (like string, list, tuple).

# ```python
# for char in "hello":
#     print(char)
# ```

# **Non-Iterable:** An object that does not return elements one by one (like `int`, `float`).

# ```python
# num = 123
# # for digit in num:  # Error: 'int' object is not iterable
# #     print(digit)
# ```

# To iterate digits in an integer:

# ```python
# for digit in str(num):
#     print(digit)
# ```



