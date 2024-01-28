#!/usr/bin/python3
a = 10
b = 5

from calculator_1 import add, subtract, multiply, divide

add_result = add(a, b)
sub_result = subtract(a, b)
mul_result = multiply(a, b)
div_result = divide(a, b)

print("Addition result:", add_result)
print("Subtraction result:", sub_result)
print("Multiplication result:", mul_result)
print("Division result:", div_result)
