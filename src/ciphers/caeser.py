class CaesarCipher:
    def __init__(self, alphabet: str):
        self.alphabet = alphabet

    def encrypt(self, text_to_encrypt: str, key: int) -> str:
        if key >= len(self.alphabet):
            key %= len(self.alphabet)
        shifted_alphabet = self.alphabet[key:] + self.alphabet[:key]
        encrypted_text = text_to_encrypt.lower().translate(
            str.maketrans(self.alphabet, shifted_alphabet)
        )
        return encrypted_text

    def decrypt(self, text_to_decrypt: str, key: int) -> str:
        if key >= len(self.alphabet):
            key %= len(self.alphabet)
        shifted_alphabet = self.alphabet[-key:] + self.alphabet[:-key]
        decrypted_text = text_to_decrypt.lower().translate(
            str.maketrans(self.alphabet, shifted_alphabet)
        )
        return decrypted_text
