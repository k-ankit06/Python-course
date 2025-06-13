# i = 1
# while i <= 10:
#     if i % 2 == 1:
#         print((str(i) + " ") * i if i != 1 else i)
#     else:
#         print(i)
#     i += 1





# n = 10  
# a, b = 0, 1
# count = 0

# while count < n:
#     print(a, end=" ")
#     a, b = b, a + b
#     count += 1




for i in range(1, 11):
    if i == 3 or i == 5 or i == 9:
        continue
    print(i)