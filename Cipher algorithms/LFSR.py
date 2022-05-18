import sys


def generate_lfsr(seed, mask, cycles):
    lfsr = [int(i) for i in seed]
    result = []

    xor_indexes = []
    # lista pozycji "xorowanych" bitów
    for i in range(len(mask)):
        if mask[i] == "1":
            xor_indexes.append(i)

    cycle = 0
    while cycle < cycles:
        print(f"{cycle + 1}: {lfsr}")
        cycle += 1
        # xor na podstawie indeksów z maski
        xor = None
        for idx in xor_indexes:
            if xor is None:
                xor = lfsr[idx]
            else:
                xor = xor ^ lfsr[idx]
        # ostatni bit do wyniku i przesunięcie w prawo
        result.append(lfsr.pop())
        # dodanie wyniku xor do początku lfsr
        lfsr.insert(0, xor)
    print(f"Generated LFSR: {result}")
    return result


def string_to_binary(string):
    ascii_values, binary_values = [], []
    # konwersja na dziesiętny
    for i in string:
        ascii_values.append(ord(i))
    print(f"ASCII: {ascii_values}")
    # konwersja na binarny
    for i in ascii_values:
        binary = bin(i)[2:]
        # uzupełnianie do 8 bitów
        while len(binary) < 8:
            binary = '0' + binary
        binary_values.append(binary)
    # przepisanie na 2d list integerów
    result = [[bit for bit in bits]
              for bits in binary_values]
    return result


def binary_to_string(binary_values):
    ascii_result = []
    result = ""
    # konwersja znaków z binarnego na dziesiętny
    for i in binary_values:
        ascii_result.append(int(i, 2))
    print(f"Encrypted ASCII: {ascii_result}")
    # z dziesiętnego na tekst
    for i in ascii_result:
        result += chr(i)
    return result


def encrypt(text, seed, mask):
    text_binary = string_to_binary(text)
    # zliczanie ilości bitów słowa
    length = 0
    for i in text_binary:
        for _ in i:
            length += 1
    # generowanie lfsr odpowiedniej długości
    lfsr = generate_lfsr(seed, mask, length)
    idx = 0
    binary_result = []
    print(f"Word in binary: {text_binary}")
    # przejście po znakach zapisanych binarnie i xor z lfsr
    for char in text_binary:
        tmp = ""
        for bit in char:
            tmp += str(int(bit) ^ lfsr[idx])
            idx += 1
        binary_result.append(tmp)
    print(f"Encrypted binary: {binary_result}")
    result = binary_to_string(binary_result)
    print(f"Encrypted word: {result}")


if __name__ == "__main__":
    param = sys.argv[1]
    if param == "-g":
        print("Initial state: ")
        init_state = input()
        print("Mask: ")
        polynomial = input()
        generate_lfsr(init_state, polynomial, 2 ** len(polynomial) - 1)
    if param == "-e":
        print("Word: ")
        word = input()
        print("Initial state: ")
        init_state = input()
        print("Mask: ")
        polynomial = input()
        encrypt(word, init_state, polynomial)
