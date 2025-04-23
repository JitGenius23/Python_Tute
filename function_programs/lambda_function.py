# create a lambda function to compute the cube of a number

cube = lambda num: num ** 3
print(cube(2))


# NOTE

''' 
-> A lambda function in python is a small, anonymous function that is defined using the 
keyword "lambda". 
-> Lambda function can only contain one expression, making them concise but less versatile 
than regular function.
-> They are nameless, but can be assigned to a variable for reuse.
-> Commonly used in situations requiring simple, quick operations, often as arguments to 
higher-order functions like map(), filter(), and reduce().

'''