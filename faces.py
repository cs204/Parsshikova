# faces.py

def main():
    str = input()
    print(convert(str))


def convert(input_str):
    input_str = input_str.replace(":)", "🙂")
    input_str = input_str.replace(":(", "🙁")
    return input_str
if __name__ == "__main__":
    main()
