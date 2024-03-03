# deep.py

def main():
    answer = input("Какой ответ на главный вопрос жизни, вселенной и всего такого? ")
    answer = answer.lower()  # Преобразуем ответ в нижний регистр для удобства сравнения

    if answer == "42" or answer == "сорок два":
        print("Да")
    else:
        print("Нет")

if __name__ == "__main__":
    main()
