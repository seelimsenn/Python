# encapsulation
# def outer(num1):
#     print("Outer function")
#     def inner_increment(num1):
#         print("Inner function")
#         return num1 + 1
#     num2 = inner_increment(num1)
#     print(num1, num2)

# outer(10)
# inner_increment(10)  # This will raise an error because inner_increment is not accessible outside outer

def factorial(number):
    if not isinstance(number, int) or number < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    def inner_factorial(number):
        if number <= 1:
            return 1
        return number * inner_factorial(number - 1)
    return inner_factorial(number)

try:
    print(factorial(5))  # Output: 120
    print(factorial(-1))  # This will raise a ValueError
except ValueError as e:
    print(e)