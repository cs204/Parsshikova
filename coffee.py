def main():
    price = 50
    total = 0

    print("Нужная сумма:", price)

    while total < price:
        coin = int(input("Вставьте монету: "))
        total += coin

    if total > price:
        change_owed = total - price
        print(f"Ваша сдача: {change_owed}", )
    else:
        print("Ваша сдача: 0")

if __name__ == "__main__":
    main()
