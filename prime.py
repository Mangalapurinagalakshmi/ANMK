def is_prime(num):
    """
    Checks if a given number is prime.
    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
    """
    if num <= 1:
        return False  # Numbers less than or equal to 1 are not prime

    # Iterate from 2 up to the square root of num.
    # If num is divisible by any number in this range, it's not prime.
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False  # Found a divisor, so it's not prime
    return True  # No divisors found, so it's prime

prime_numbers = []
for number in range(1, 101):  # Iterate through numbers from 1 to 100
    if is_prime(number):
        prime_numbers.append(number)

print("Prime numbers between 1 and 100 are:")
print(prime_numbers)