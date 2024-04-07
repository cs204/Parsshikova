import sys

def count_code_lines(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            count = 0
            for line in lines:
                line = line.strip()
                if line and not line.startswith('#'):
                    count += 1
            return count
    except FileNotFoundError:
        print("Файл не найден.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].endswith('.py'):
        print("Использование: python lines.py <имя_файла.py>")
        sys.exit(1)

    file_name = sys.argv[1]
    code_lines = count_code_lines(file_name)
    print(code_lines)
