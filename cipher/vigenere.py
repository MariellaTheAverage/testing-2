import exceptions

alphabet = "abcdefghijklmnopqrstuvwxyz"
letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))


def encrypt(message, key):
    encrypted = ""
    split_message = [
        message[i: i + len(key)] for i in range(0, len(message), len(key))
    ]

    for each_split in split_message:
        i = 0
        for letter in each_split:
            if letter not in alphabet:
                raise exceptions.SymbolError(letter, "plain text")
            number = (letter_to_index[letter] +
                      letter_to_index[key[i]]) % len(alphabet)
            encrypted += index_to_letter[number]
            i += 1

    return encrypted


def decrypt(cipher, key):
    decrypted = ""
    split_encrypted = [
        cipher[i: i + len(key)] for i in range(0, len(cipher), len(key))
    ]

    for each_split in split_encrypted:
        i = 0
        for letter in each_split:
            if letter not in alphabet:
                raise exceptions.SymbolError(letter, "ciphertext")
            number = (letter_to_index[letter] -
                      letter_to_index[key[i]] + len(alphabet)) % len(alphabet)
            decrypted += index_to_letter[number]
            i += 1

    return decrypted


def run():
    print("Vigenere cipher")
    message = input("Input text:\n-> ")
    message = message.lower()
    key = input("Input key:\n-> ")
    key = key.lower()
    if key == "":
        raise exceptions.EmptyKeyError()
    for s in key:
        if s not in alphabet:
            raise exceptions.SymbolError(s, "key")
    
    raw_action = input("[1] Encrypt:\n[2] Decrypt:\n[0] Exit\n-> ")
    try:
        action = int(raw_action)
    except ValueError:
        raise exceptions.InvalidOperationError(raw_action, list(range(3)), "not an int")

    if action == 1:
        result = encrypt(message, key)
    elif action == 2:
        result = decrypt(message, key)
    elif action == 0:
        return
    else:
        raise exceptions.InvalidOperationError(action, list(range(3)), "unsupported code")

    print(result)

