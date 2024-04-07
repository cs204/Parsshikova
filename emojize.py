import emoji

def main():
    s = input("Input: ")
    result = emoji.emojize(s)
    print(f"Output: {result}")

if __name__ == "__main__":
    main()
