import math

def is_strong_number(num):
    """
    Checks if a given number is a strong number.
    A strong number is a number where the sum of the factorials of its digits
    equals the number itself.
    """
    if num < 0:
        return False  # Strong numbers are typically positive integers
    
    original_num = num
    sum_of_factorials = 0
    
    # Calculate factorial for each digit and sum them
    while num > 0:
        digit = num % 10
        sum_of_factorials += math.factorial(digit)
        num //= 10
        
    return sum_of_factorials == original_num

print("Strong numbers between 1 and 500 are:")
for number in range(1, 501):  # Iterate from 1 to 500 (inclusive)
    if is_strong_number(number):
        print(number)