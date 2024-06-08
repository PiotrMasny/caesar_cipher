import pytest

from src.ciphers.caeser import CaesarCipher


@pytest.mark.parametrize("text_to_encrypt, key, encrypted_text", [
    ('opportunity', 2, 'qrrqtvwpkva'),
    ('5 diamonds', 5, '5 infrtsix')
])
def test_encrypt_lowercase_sentence_with_positive_key(text_to_encrypt, key, encrypted_text):
    cipher = CaesarCipher([chr(letter) for letter in range(ord('a'), ord('z') + 1)])  # from string import ascii_lowercase
    actual_result = cipher.encrypt(text_to_encrypt, key)
    expected_result = encrypted_text
    assert actual_result == expected_result


@pytest.mark.parametrize("text_to_decrypt, key, decrypted_text", [
    ('yjkuv', 2, 'whist'),
    ('fqq ns', 5, 'all in')
])
def test_decrypt_lowercase_sentence_with_positive_key(text_to_decrypt, key, decrypted_text):
    cipher = CaesarCipher([chr(letter) for letter in range(ord('a'), ord('z') + 1)])
    actual_result = cipher.decrypt(text_to_decrypt, key)
    expected_result = decrypted_text
    assert actual_result == expected_result


@pytest.mark.parametrize("text_to_encrypt, key, encrypted_text", [
    ('Bluff', 2, 'dnwhh'),
    ('After tHe GAME!', 5, 'fkyjw ymj lfrj!')
])
def test_encrypt_uppercase_sentence_with_positive_key(text_to_encrypt, key, encrypted_text):
    cipher = CaesarCipher([chr(letter) for letter in range(ord('a'), ord('z') + 1)])
    actual_result = cipher.encrypt(text_to_encrypt, key)
    expected_result = encrypted_text
    assert actual_result == expected_result


@pytest.mark.parametrize("text_to_decrypt, key, decrypted_text", [
    ('ejGEmocVg', 2, 'checkmate'),
    ('xytsjbfQQ Fyyfhp', 5, 'stonewall attack')
])
def test_decrypt_uppercase_sentence_with_positive_key(text_to_decrypt, key, decrypted_text):
    cipher = CaesarCipher([chr(letter) for letter in range(ord('a'), ord('z') + 1)])
    actual_result = cipher.decrypt(text_to_decrypt, key)
    expected_result = decrypted_text
    assert actual_result == expected_result

# TODO
# testy dal znaków specjalnych ze sa ignorowane ./*/- oraz ąćłż
# dodac test dla pojedynczej litery z -> a oraz a -> z
# dodac test dla psutego słowa
# dodac test dla key=0
