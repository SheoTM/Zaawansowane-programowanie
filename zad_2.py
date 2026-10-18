#2a
def function1(names):
    for name in names:
        print(name)
list_of_names = ["Agata", "Karolina", "Karol", "Marcel", "Oskar"]
print("Zad 2a")
function1(list_of_names)

#2b i
def function_for(numbers):
    score = []
    for number in numbers:
        score.append(number * 2)
    return score

#2b ii
def function_list_comprehension(numbers):
    return [number * 2 for number in numbers]

list_of_numbers = list(range(1,6))
print("Zad 2b i")
print(function_for(list_of_numbers))
print("Zad 2b ii")
print(function_list_comprehension(list_of_numbers))

# 2c
def function_even_numbers(numbers):
    even_numbers = []

    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    print(even_numbers)


# 2d
def function_every_second_element(numbers):
    print(numbers[::2])
list_of_numbers = list(range(1, 11))
print("Zad 2c")
function_even_numbers(list_of_numbers)
print("Zad 2d")
function_every_second_element(list_of_numbers)