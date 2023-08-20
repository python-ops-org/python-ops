def find_largest_number(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest


numbers = [3,12,14,1,5,9,2,6]

largest_number = find_largest_number(numbers)
print(largest_number)
