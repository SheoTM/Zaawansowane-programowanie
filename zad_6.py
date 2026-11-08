# Zad 6
def function_lists(numbers1: list[int],
                   numbers2: list[int]) -> list[int]:
    combined = numbers1 + numbers2
    unique_numbers = set(combined)
    return [number ** 3 for number in sorted(unique_numbers)]


list_of_numbers1 = [1, 2, 3, 4, 5]
list_of_numbers2 = [3, 4, 5, 6, 7]

result = function_lists(list_of_numbers1, list_of_numbers2)
print(result)
