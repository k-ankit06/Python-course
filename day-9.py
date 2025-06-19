# Lambda function (anonymous function) to calculate the square of a number

# sybtax = lambda parameter: expression

# def add(x,y):
#     zx = x+y
#     print(zx)
# add(1,3)   

# x = lambda a, b: print(a+b)

# x(1,3)

# square = lambda x: x * x
# print(square(5))


#  use case :
#  map()
# filter()
# reduce()





# using map() generate 
# ["2 x 1 =2"............"2 x 10 =20"]
x =[1,2,3,4,5,6,7,8,9,10] 
tbl = list(map(lambda i : f"2 x {i} = {2*i}", x))
print(tbl)