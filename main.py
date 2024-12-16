import cipher.caesar
import cipher.vigenere
import exceptions

def main():
    print("Cryptographic ciphers!")

    raw_cphr = input("Select a cipher:\n[1] - Caesar cipher\n[2] - Vigenere cipher\n[0] - Exit\n-> ")
    try:
        cphr = int(raw_cphr)
    except ValueError:
        raise exceptions.InvalidOperationError(raw_cphr, list(range(3)), "not an int")
    
    if cphr == 1:
        cipher.caesar.run()
    
    elif cphr == 2:
        cipher.vigenere.run()

    elif cphr == 0:
        pass

    else:
        raise exceptions.InvalidOperationError(cphr, list(range(3)), "unsupported code")

if __name__ == "__main__":
    main()