test_list = []

testing = int(input('How many numbers: '))

for n in range(testing):
    numbers = int(input('Enter number '))
    test_list.append(numbers)

print("Sum of elements in given list is :", test_list, sum(test_list))
