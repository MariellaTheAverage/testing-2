import exceptions

def encrypt(message, key, alphabet='abcdefghijklmnopqrstuvwxyz'):
    l = len(alphabet)
    res = ""
    for s in message:
        if s in alphabet:
            res += alphabet[(key + alphabet.find(s)) % l]
        else:
            res += s
    return res

def get_key(plain_text, encrypted_text, alphabet='abcdefghijklmnopqrstuvwxyz'):
    l = len(plain_text)
    l1 = len(encrypted_text)
    if l != l1:
        raise exceptions.MismatchedTextsError(l, l1)
    
    la = len(alphabet)
    prev_key = (alphabet.find(encrypted_text[0]) - alphabet.find(plain_text[0]) + la) % la
    for i in range(1,l):
        cur_key = (alphabet.find(encrypted_text[i]) - alphabet.find(plain_text[i]) + la) % la
        if cur_key != prev_key:
            raise exceptions.InconsistentShiftError(0, prev_key, i, cur_key)
    return prev_key

def run():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    print("Caesar cipher")

    raw_action = input("[1] Encrypt:\n[2] Decrypt:\n[3] Find shift value:\n[0] Exit\n-> ")
    try:
        action = int(raw_action)
    except ValueError:
        raise exceptions.InvalidOperationError(raw_action, list(range(4)), "not an int")

    if action == 1:
        message = input("Plain text:\n-> ")
        message = message.lower()
        raw_shft = input("Enter the shift value:\n-> ")
        try:
            shft = int(raw_shft)
        except ValueError:
            raise exceptions.InvalidShiftError(raw_shft, "not an int")
        if shft >= len(alphabet) or shft < 0:
            raise exceptions.InvalidShiftError(shft, f"out of range (expected 0 to {len(alphabet)}, was {shft})")
        print(encrypt(message, shft, alphabet))

    elif action == 2:
        message = input("Ciphertext:\n-> ")
        message = message.lower()
        raw_shft = input("Enter the shift value:\n-> ")
        try:
            shft = int(raw_shft)
        except ValueError:
            raise exceptions.InvalidShiftError(raw_shft, "not an int")
        if shft >= len(alphabet) or shft < 0:
            raise exceptions.InvalidShiftError(shft, f"out of range (expected 0 to {len(alphabet)}, was {shft})")
        print(encrypt, message, len(alphabet)-shft, alphabet)

    elif action == 3:
        plain_text = input("Plain text:\n-> ")
        plain_text = plain_text.lower()
        encrypted_text = input("Ciphertext:\n-> ")
        encrypted_text = encrypted_text.lower()
        key = get_key(plain_text, encrypted_text, alphabet)
        print(f"The shift is: {key}")

    elif action == 0:
        pass

    else:
        raise exceptions.InvalidOperationError(action, list(range(4)), "unsupported code")
    
