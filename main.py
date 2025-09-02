import random


def rand_numbers(n: int) -> list:
    return [random.randint(1, 100) for _ in range(n)]

def show(numbers: list) -> None:
    for number in numbers:
        print(number, end = ' ')
    print()


# Sortowanie babelkowe
def bubble_sort(numbers: list) -> list:
    n = len(numbers)
    for j in range(0, n-1):
        for i in range(0, n - 1 -j):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
    return numbers


# Sortowanie poprzez wybor
def selection_sort(numbers: list) -> list:
    n = len(numbers)
    j = 0
    while j<n:
        p_min = j
        i = j+1
        while i<n:
            if numbers[i] < numbers[p_min]:
                p_min = i
            i += 1
        numbers[j], numbers[p_min] = numbers[p_min], numbers[j]
        j+=1
    return numbers






if __name__ == "__main__":
    numbers = rand_numbers(30)
    show(numbers)
    print(bubble_sort(numbers))
    print(selection_sort(numbers))