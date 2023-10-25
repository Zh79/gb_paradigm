numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


def sort_list_imperative(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    

    return numbers


def sort_list_declarative(numbers):
    numbers.sort(reverse=True)
    print(numbers)

sort_list_declarative(numbers)
print(sort_list_imperative(numbers))
