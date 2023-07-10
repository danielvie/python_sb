from returns.result import safe

# define a function that returns an Either monad
@safe
def divide(a, b):
    return a / b

# use the Either monad to safely divide two numbers
result1 = divide(10, 1)
result2 = divide(10, 0)

# check if the result is a value or an error
if isinstance(result1, Exception):
    print("Error occurred:", result2.value_or(0))
else:
    print("The result is:", result2)
print('sdfasdf')