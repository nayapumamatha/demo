def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def is_strong(number):
    temp = number
    digit_sum = 0

    while temp != 0:
        digit = temp % 10
        digit_sum += factorial(digit)
        temp //= 10

    return digit_sum == number

strong_numbers = []

for num in range(1, 5001):
    if is_strong(num):
        strong_numbers.append(num)

print("The strong numbers between 1 and 5000 are:")
print(strong_numbers)

