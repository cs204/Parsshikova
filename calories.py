
calories_dict = {
    "Apple": 130,
    "Avocado": 50,
    "Lime": 20,
    "pear": 57
}


fruit = input("Фрукт: ")


if fruit in calories_dict:
    calories = calories_dict[fruit]
    print(f"Калории: {calories}")
else:
    print(" ")
