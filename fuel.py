import sys

def main():
    while True:
        try:
            fraction = input("Дробь: ")
            x, y = map(int, fraction.split('/'))

            if y == 0 or x > y:
                continue

            fuel(x, y)

            break

        except (ValueError, ZeroDivisionError):
            continue

def fuel(x, y):
    if y == 0 or x > y:
        sys.exit("Бак не может быть полон более чем на 100%")

    percentage = round(x / y * 100)

    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")

if __name__ == "__main__":
    main()
