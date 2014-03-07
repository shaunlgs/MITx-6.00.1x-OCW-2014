def fibonacci(x):
    if x == 0:
        return 1
    elif x == 1:
        return 2
    return fibonacci(x-1) + fibonacci(x-2)

x = 0
number = fibonacci(x)
sum = 0
while number < 4000000:
    number = fibonacci(x)
    if (number % 2 == 0):
        sum += number
    x += 1
print(sum)