user_number = int(input())
factorial = 1
counter = user_number
while counter > 0:
    factorial = factorial * counter
    counter = counter - 1
print(factorial)
