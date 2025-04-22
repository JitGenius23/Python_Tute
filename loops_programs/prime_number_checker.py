# Check a number is prime number or not

number = int(input('enter a number to check prime number of not:'))

if(number == 2):
    print('prime number 😃')

for i in range(2, number):
    if(number % i == 0):
        print('not a prime number 😒')
        break
    else:
        print('prime number 😃')
        break