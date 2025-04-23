# create a function that takes two numbers as parameters and returns their sum

'''
def sum(num1, num2):
    return num1 + num2

result = sum(2,3)
print(result)
'''


# function with *args
# Write a function that takes variable number of arguments and returns their sum.

def add(*args):
    return sum(args)

print(add(1,2,3,4))

'''
def add(*args):
    result = 0
    print(args)  # This returns Tuple (1,2,3,4,5)
    for val in args:
        result += val
    return result

print(add(1,2, 3, 4, 5))
'''