numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


def sort_list_imperative(numbers):
    for i in range(len(numbers) - 2):
        for j in numbers:
            if numbers[i] < numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]

    return numbers


def sort_list_declarative(numbers):
    numbers.sort(reverse=True)
    print(numbers)

sort_list_declarative(numbers)
print(sort_list_imperative(numbers))
