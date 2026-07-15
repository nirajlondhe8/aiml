def replace_letter_with_slicing(text, index, new_letter):
    return text[:index] + new_letter + text[index + 1:]


def replace_letter_with_list(text, index, new_letter):
    letters = list(text)
    letters[index] = new_letter
    return "".join(letters)


def main():
    word = "hello"

    print(replace_letter_with_slicing(word, 1, "a"))
    print(replace_letter_with_list(word, 1, "a"))


if __name__ == "__main__":
    main()
