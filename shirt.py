import sys
from PIL import Image, ImageOps

def apply_shirt(input_file, output_file):
    # Проверка расширений файлов
    if not (input_file.lower().endswith('.jpg') or input_file.lower().endswith('.jpeg') or input_file.lower().endswith('.png')):
        print("Ошибка: Входной файл должен быть в формате JPEG или PNG.")
        sys.exit(1)
    if not (output_file.lower().endswith('.jpg') or output_file.lower().endswith('.jpeg') or output_file.lower().endswith('.png')):
        print("Ошибка: Выходной файл должен быть в формате JPEG или PNG.")
        sys.exit(1)
    if input_file.split('.')[-1].lower() != output_file.split('.')[-1].lower():
        print("Ошибка: Расширения входного и выходного файлов должны совпадать.")
        sys.exit(1)

    try:
        # Открываем файл с футболкой и файл с изображением
        shirt_img = Image.open("shirt.png")
        input_img = Image.open(input_file)

        # Изменяем размер и обрезаем изображение
        input_img = ImageOps.fit(input_img, shirt_img.size)

        # Накладываем футболку на изображение
        input_img.paste(shirt_img, (0, 0), shirt_img)

        # Сохраняем результат
        input_img.save(output_file)
    except FileNotFoundError:
        print("Ошибка: Входной файл не найден.")
        sys.exit(1)


if __name__ == "__main__":
    # Проверка количества аргументов командной строки
    if len(sys.argv) != 3:
        print("Ошибка: Пожалуйста, укажите ровно два аргумента командной строки.")
        sys.exit(1)

    # Получение имен файлов из аргументов командной строки
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Применение футболки к изображению
    apply_shirt(input_file, output_file)
