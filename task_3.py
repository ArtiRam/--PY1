import random


def get_unique_list_numbers() -> list[int]:
    unique_numbers = set()
    while len(unique_numbers) < 15:
        unique_numbers.add(random.randint(-10, 10))
    return list(unique_numbers)


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers))
