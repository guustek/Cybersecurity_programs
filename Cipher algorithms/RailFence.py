import sys


def encrypt(text, k):
    print("Encrypting - " + text)
    matrix = [['' for _ in range(len(text))]
              for _ in range(k)]

    row_idx = 0
    col_idx = 0
    dir_down = False

    # wypełnienie macierzy zadanym słowem na kształt płotka
    for i in range(len(text)):
        if row_idx == 0 or row_idx == k - 1:
            dir_down = not dir_down
        matrix[row_idx][col_idx] = text[i]
        col_idx += 1
        if dir_down:
            row_idx += 1
        else:
            row_idx -= 1

    # wpisanie po wierszach wartości do wyniku
    result = ""
    for i in range(k):
        for j in range(len(text)):
            if matrix[i][j] != '':
                result += matrix[i][j]
    return result


def decrypt(text, k):
    print("Decrypting - " + text)

    matrix = [['' for _ in range(len(text))]
              for _ in range(k)]

    row_idx = 0
    col_idx = 0
    dir_down = False

    # wpisanie * w miejsca, gdzie powinien być wyraz na kształt płotka
    for i in range(len(text)):
        if row_idx == 0:
            dir_down = True
        if row_idx == k - 1:
            dir_down = False
        matrix[row_idx][col_idx] = '*'
        col_idx += 1
        if dir_down:
            row_idx += 1
        else:
            row_idx -= 1
    index = 0

    # przejście wiersz po wierszu i wstawianie liter w miejsca *, tak jak było odczytywane słowo po zaszyfrowaniu
    for i in range(k):
        for j in range(len(text)):
            if ((matrix[i][j] == '*') and
                    (index < len(text))):
                matrix[i][j] = text[index]
                index += 1
    result = ""
    row_idx = 0
    col_idx = 0

    # czytanie wyrazu po ukosie, na kształt płotka
    for i in range(len(text)):
        if row_idx == 0:
            dir_down = True
        if row_idx == k - 1:
            dir_down = False
        result += matrix[row_idx][col_idx]
        col_idx += 1

        if dir_down:
            row_idx += 1
        else:
            row_idx -= 1

    return result


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Wrong number of arguments!")
    else:
        print("Text: ")
        word = input()
        print("Fence height: ")
        n = int(input())
        if n <= 0:
            print("Height needs to be greater than 0!")
        else:
            if sys.argv[1] == "-e":
                print("Result: " + encrypt(word, n))
            elif sys.argv[1] == "-d":
                print("Result: " + decrypt(word, n))
            else:
                print("Invalid arguments!.Arguments: -d (decryption)/ -e (encryption)")
