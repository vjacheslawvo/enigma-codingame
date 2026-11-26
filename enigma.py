# Лабораторна робота: Encryption/Decryption of Enigma Machine (CodinGame)
# Виконав: Войцещук Вячеслав РЕ-61мп

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def caesar(message, start, direction):
    """Зсув (Цезар): i-та літера зсувається на start + i.
    direction = 1 для шифрування, -1 для розшифрування."""
    result = ""
    for i, ch in enumerate(message):
        pos = ALPHABET.index(ch)
        result += ALPHABET[(pos + direction * (start + i)) % 26]
    return result


def encode(message, shift, rotors):
    text = caesar(message, shift, 1)
    for rotor in rotors:                      # ротори по черзі: I, II, III
        text = "".join(rotor[ALPHABET.index(ch)] for ch in text)
    return text


def decode(message, shift, rotors):
    text = message
    for rotor in reversed(rotors):            # у зворотному порядку: III, II, I
        text = "".join(ALPHABET[rotor.index(ch)] for ch in text)
    return caesar(text, shift, -1)


def main():
    operation = input().strip()
    shift = int(input())
    rotors = [input().strip() for _ in range(3)]
    message = input().strip()

    if operation == "ENCODE":
        print(encode(message, shift, rotors))
    else:
        print(decode(message, shift, rotors))


if __name__ == "__main__":
    main()
