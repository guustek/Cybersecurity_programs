import math
import sys

key = [3, 4, 1, 5, 2]
d = 5


def encrypt(text):
    print("Encrypting - " + text)
    # d = math.ceil(math.sqrt(len(text)))

    matrix = [['' for _ in range(d)]
              for _ in range(d)]
    idx = 0

    for i in range(d):
        for j in range(d):
            if idx < len(text):
                matrix[i][j] = text[idx]
                idx += 1

    row_idx = 0
    col_idx = 0
    result = ""

    # przejście po wszystkich komórkach macierzy pobierając znak ze wskazanego w kluczu indeksu
    for i in range(d ** 2):
        col_idx = col_idx % len(key)
        result += matrix[row_idx][key[col_idx] - 1]
        col_idx += 1
        if col_idx >= d:
            row_idx += 1

    return result


def decrypt(text):
    result = "Not implemented"
    return result


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Wrong number of arguments!")
    else:
        print("Word: ")
        word = input()
        if sys.argv[1] == "-e":
            print("Result: " + encrypt(word))
        elif sys.argv[1] == "-d":
            print("Result: " + decrypt(word))
        else:
            print("Invalid arguments!.Arguments: -d (decryption)/ -e (encryption)")
