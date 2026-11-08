# Zad 3
def function_even(number: int) -> bool:
    return number % 2 == 0


result = function_even(8)

if result:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")
