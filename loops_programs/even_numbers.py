# sum of even numbers

number = 10
sum_of_even_numbers = 0

for num in range(1, number + 1):
    if num % 2 == 0:
        sum_of_even_numbers += num

print(sum_of_even_numbers)