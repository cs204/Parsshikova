# bank.py

def main():
    greeting = input("Приветствие: ")
    greeting = greeting.lower()  # Преобразуем приветствие в нижний регистр для удобства сравнения

    if greeting.startswith("здравствуйте"):
        print("$0")
    elif greeting.startswith("з"):
        print("$20")
    else:
        print("$100")

if __name__ == "__main__":
    main()
