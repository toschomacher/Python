#!/usr/bin/env python3

def english_dictionary():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())
        word_file.close()
    return valid_words


def caesar(input_string: str, rotation: int = 1) -> str:
    from string import ascii_letters as letters
    key = {}
    for letter in letters:
        if 96 < ord(letter) < 123:
            key[letter] = chr((ord(letter) - ord('a') + rotation) % 26 + ord('a'))
        if 64 < ord(letter) < 91:
            key[letter] = chr((ord(letter) - ord('A') + rotation) % 26 + ord('A'))
    translation_table = str.maketrans(key)
    return input_string.translate(translation_table)


if __name__ == "__main__":
    from re import sub as replace
    import sys

    english_words = english_dictionary()
    if len(sys.argv) == 1:
        print("Error: Missing command-line argument.")
    else:
        try:
            with open(f"{sys.argv[1]}", "r") as file:
                myString = file.read()
            success = 0
            for n in range(1, 27):
                counter = 0
                encryptedString = caesar(myString, n)
                compare_list = replace("[^a-zA-Z]", " ", encryptedString).split()
                total_number_words = len(compare_list)
                for word in compare_list:
                    if word.lower() in english_words:
                        counter += 1
                if (int(counter / total_number_words * 100)) > 70:
                    print(encryptedString)
                    success = 1
                    # print(str(int(counter / total_number_words * 100)) + "%")
            if success == 0:
                print('Cannot decrypt. Most likely not a Caesar Cypher at work here.')
            file.close()
        except FileNotFoundError:
            print('Error: Cannot open "' + sys.argv[1] + '". Sorry about that.')
