class CipherError(Exception):
    pass

# All - wrong opcode
# not an int
# out of range
class InvalidOperationError(CipherError):
    def __init__(self, incode, codes: list, msg = "") -> None:
        self.opcode = incode
        self.coderange = codes
        self.message = f"Invalid operation code: {msg}"
        super().__init__(self.message)

    def __str__(self) -> str:
        return f"{self.message} (was {self.opcode})\nAvailable codes: {self.coderange}"

# Caesar - shift is either negative or
# > the alphabet length
class InvalidShiftError(CipherError):
    def __init__(self, shift, msg="") -> None:
        self.shift = shift
        self.message = f"Invalid shift value: {msg}"
        super().__init__(self.message)
    
    def __str__(self) -> str:
        return f"{self.message} (was {self.shift})"

# Caesar - get_key() returns differing shift values
class InconsistentShiftError(CipherError):
    def __init__(self, idx1, val1, idx2, val2) -> None:
        self.message = f"Inconsistent shift: index {idx1} produced value {val1}, while index {idx2} produced {val2}"
        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message
    
# Caesar - get_key() got texts of mismatched lengths
class MismatchedTextsError(CipherError):
    def __init__(self, plain_len, cipher_len) -> None:
        self.plen = plain_len
        self.clen = cipher_len
        self.message = f"Non-matching text lengths: plain text is {plain_len} characters long while ciphertext is {cipher_len} characters"
        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message
    
# Vigenere - symbol not in the predefined alphabet
class SymbolError(CipherError):
    def __init__(self, sym, msg) -> None:
        self.sym = sym
        self.msg = f"Encountered non-alphabet symbol {sym} in {msg}"
        super().__init__(self.msg)

    def __str__(self) -> str:
        return self.msg
    
# Vigenere - empty key string
class EmptyKeyError(CipherError):
    def __init__(self) -> None:
        self.message = "Key must not be empty"
        super().__init__(self.message)
    
    def __str__(self) -> str:
        return self.message