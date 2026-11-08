# Zad 5
def function_contains(numbers: list[int], number: int) -> bool:
    return number in numbers


list_of_numbers = [1, 2, 3, 4, 5]
result = function_contains(list_of_numbers, 3)
print(result)
