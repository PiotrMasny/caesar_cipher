class CaesarCipher:
    def __init__(self, alphabet: list):
        self.alphabet = alphabet

    def encrypt(self, text_to_encrypt: str, key: int) -> str:
        encrypted_text = ""
        for sign in text_to_encrypt.lower():
            try:
                if not sign.isalpha():
                    encrypted_text += sign
                else:
                    encrypted_text += self.alphabet[
                        (self.alphabet.index(sign) + key) % len(self.alphabet)
                    ]
            except ValueError:
                encrypted_text += sign
        return encrypted_text

    def decrypt(self, text_to_decrypt: str, key: int) -> str:
        decrypted_text = ""
        for sign in text_to_decrypt.lower():
            try:
                if not sign.isalpha():
                    decrypted_text += sign
                else:
                    decrypted_text += self.alphabet[
                        (self.alphabet.index(sign) - key) % len(self.alphabet)
                    ]
            except ValueError:
                decrypted_text += sign
        return decrypted_text
