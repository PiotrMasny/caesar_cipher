class CaesarCipher:
    def __init__(self, alphabet: list):
        self.alphabet = alphabet

    def encrypt(self, text_to_encrypt: str, key: int) -> str:
        encrypted_text = ''
        for sign in text_to_encrypt.lower():
            if not sign.isalpha():
                encrypted_text += sign
            else:
                encrypted_text += self.alphabet[
                    (self.alphabet.index(sign) + key) % len(self.alphabet)
                    ]
        return encrypted_text

    def decrypt(self, text_to_decrypt: str, key: int) -> str:
        decrypted_text = ''
        for sign in text_to_decrypt.lower():
            if not sign.isalpha():
                decrypted_text += sign
            else:
                decrypted_text += self.alphabet[
                    (self.alphabet.index(sign) - key) % len(self.alphabet)
                    ]
        return decrypted_text
