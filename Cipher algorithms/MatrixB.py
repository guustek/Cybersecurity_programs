import math
import sys


def encrypt(text, key):
    print("Encrypting - " + text)
    num_rows = math.ceil(len(word) / len(key))

    matrix = [['' for _ in range(len(key))]
              for _ in range(num_rows)]

    idx = 0
    for i in range(num_rows):
        for j in range(len(key)):
            if idx < len(text):
                matrix[i][j] = text[idx]
                idx += 1

    # stworzenie na podstawie posortowanego klucza, listy indeksów w takiej kolejności, w jakiej mają być pobierane
    # wartości z kolumn
    numerical_key = []
    sorted_text = sorted(key)
    key = list(key)
    for c in range(len(sorted_text)):
        index = key.index(sorted_text[c])
        key[index] = "*"
        numerical_key.append(index)

    # pobranie wartości z kolumn wykorzystując utworzoną listę indeksów
    result = ""
    for i in range(len(numerical_key)):
        for j in range(num_rows):
            result += matrix[j][numerical_key[i]]

    return result


def decrypt(text, key):
    result = "Not implemented"
    return result


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Wrong number of arguments!")
    else:
        print("Text: ")
        word = input()
        word = word.replace(" ", "")
        print("Klucz: ")
        k = input()
        if sys.argv[1] == "-e":
            print("Result: " + encrypt(word, k))
        elif sys.argv[1] == "-d":
            print("Result: " + decrypt(word, k))
        else:
            print("Invalid arguments!.Arguments: -d (decryption)/ -e (encryption)")
