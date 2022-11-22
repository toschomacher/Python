#!/usr/bin/env python3

import string


def caesar(input_string: str, rotation: int = 1) -> str:

    key = {}
    for ch in string.ascii_lowercase:
        key[ch] = chr((ord(ch) - ord('a') + rotation) % 26 + ord('a'))
    translation_table_low = str.maketrans(key)

    rot = {}
    for cap in string.ascii_uppercase:
        rot[cap] = chr((ord(cap) - ord('A') + rotation) % 26 + ord('A'))
    translation_table_up = str.maketrans(rot)

    translation_table = translation_table_low | translation_table_up
    return input_string.translate(translation_table)


if __name__ == "__main__":
    myString = "Bc cbs kcizr vojs pszwsjsr wb hvs zogh msofg ct hvs bwbshssbhv qsbhifm hvoh hvwg kcfzr kog pswbu" \


    for n in range(1, 27):
        encryptedString = caesar(myString, n)
        if 'the' and 'and' and 'was' in encryptedString:
            print(encryptedString)
