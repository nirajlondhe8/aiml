def main():
    text = "hello"

    print("Original string:", text)
    print("Strings are immutable, so this would fail:")
    print('text[1] = "a"')

    new_text = text[:1] + "a" + text[2:]

    print("Modified copy:", new_text)
    print("Original string is still:", text)


if __name__ == "__main__":
    main()
