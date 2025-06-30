# # Questions on len() Function

# #    1) Write a Python program to find the length of the string "Hello, World!" using the len() function.

# # string = "Hello, World!"
# # print(len(string))  # Output: 13


# #    2) Given a list fruits = ['apple', 'banana', 'cherry'], use the len() function to find how many items are in the list.


# # fruits = ['apple', 'banana', 'cherry']
# # print(len(fruits))  # Output: 3


# #    3) Write a Python program to find the length of the tuple (10, 20, 30, 40, 50).

# # numbers_tuple = (10, 20, 30, 40, 50)
# # print(len(numbers_tuple))  # Output: 5


# #    4) Create a Python function that takes a string as input and returns whether its length is greater than 10.

# # def is_length_greater_than_10(s):
# #     return len(s) > 10


# # print(is_length_greater_than_10("Hello, World!"))  # Output: True
# # print(is_length_greater_than_10("Python"))  # Output: False

# #    5) Given a nested list matrix = [[1, 2], [3, 4], [5, 6]], use the len() function to find how many rows are in the matrix.

# # matrix = [[1, 2], [3, 4], [5, 6]]
# # print(len(matrix))  # Output: 3

# #    6) Write a program to determine if a list has an odd or even number of elements using the len() function.

# # def is_list_length_even_or_odd(lst):
# #     return "Even" if len(lst) % 2 == 0 else "Odd"

# # sample_list = [1, 2, 3, 4, 5]
# # print(is_list_length_even_or_odd(sample_list))  # Output: Odd

# # another_list = [1, 2, 3, 4]
# # print(is_list_length_even_or_odd(another_list))  # Output: Even


# Questions on count() Function

#    1) Write a Python program to count how many times the letter 'a' appears in the string "Banana".

# string = "Banana"
# print(string.count('a'))  # Output: 3


#    2) Given the list numbers = [1, 2, 3, 2, 4, 2, 5], use the count() function to count the occurrences of the number 2.

# numbers = [1, 2, 3, 2, 4, 2, 5]
# print(numbers.count(2))  # Output: 3


#    3) Create a Python function that takes a list and an item as input and returns how many times that item appears in the list.


# items = input("Enter list items separated by space: ").split()


# item = input("Enter item to count: ")


# count = items.count(item)


# print("Item appears", count, "times.")

#    4) Write a program to count how many spaces are in the string "Python is fun to learn!".

# sentence = "Python is fun to learn!"
# print(sentence.count(' '))  # Output: 4

#    5) Using the count() function, count how many 'b's are in the string "bubblebee".

# word = "bubblebee"
# print(word.count('b'))  # Output: 4

#    6) Write a Python script to count the number of occurrences of the word 'the' in a given sentence.

# text = "The quick brown fox jumps over the lazy dog. The dog barked."
# print(text.lower().count('the'))  # Output: 3
