menu = {
   "кофе": 20.00,
   "чай": 10.00,
   "булочка": 5.00,
   "салат": 30.40,
   "пирожное": 45.50
}

sum = 0

try:
    while True:
        item = input("Блюдо: ").lower()
        if item in menu:
            sum += menu[item]
except EOFError:
    print()
    print(f"Сумма: {sum:.2f}")
