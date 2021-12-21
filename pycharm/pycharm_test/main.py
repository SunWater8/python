def checkio(number):
    if number % 15 == 0:
        return 'Fizz Buzz'
    if number % 5 == 0:
        return 'Buzz'


b = checkio(30)

print(b)
