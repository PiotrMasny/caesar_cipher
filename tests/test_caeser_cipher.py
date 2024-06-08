from string import ascii_lowercase

import pytest

from src.ciphers.caeser import CaesarCipher


@pytest.mark.parametrize(
    "text_to_encrypt, key, encrypted_text",
    [("opportunity", 2, "qrrqtvwpkva"), ("5 diamonds", 5, "5 infrtsix")],
)
def test_encrypt_lowercase_sentence_with_positive_key(
    text_to_encrypt, key, encrypted_text
):
    cipher = CaesarCipher(list(ascii_lowercase))
    actual_result = cipher.encrypt(text_to_encrypt, key)
    expected_result = encrypted_text
    assert actual_result == expected_result


@pytest.mark.parametrize(
    "text_to_decrypt, key, decrypted_text",
    [("yjkuv", 2, "whist"), ("fqq ns", 5, "all in")],
)
def test_decrypt_lowercase_sentence_with_positive_key(
    text_to_decrypt, key, decrypted_text
):
    cipher = CaesarCipher(list(ascii_lowercase))
    actual_result = cipher.decrypt(text_to_decrypt, key)
    expected_result = decrypted_text
    assert actual_result == expected_result


@pytest.mark.parametrize(
    "text_to_encrypt, key, encrypted_text",
    [("Bluff", 2, "dnwhh"), ("After tHe GAME!", 5, "fkyjw ymj lfrj!")],
)
def test_encrypt_uppercase_sentence_with_positive_key(
    text_to_encrypt, key, encrypted_text
):
    cipher = CaesarCipher(list(ascii_lowercase))
    actual_result = cipher.encrypt(text_to_encrypt, key)
    expected_result = encrypted_text
    assert actual_result == expected_result


@pytest.mark.parametrize(
    "text_to_decrypt, key, decrypted_text",
    [("ejGEmocVg", 2, "checkmate"), ("xytsjbfQQ Fyyfhp", 5, "stonewall attack")],
)
def test_decrypt_uppercase_sentence_with_positive_key(
    text_to_decrypt, key, decrypted_text
):
    cipher = CaesarCipher(list(ascii_lowercase))
    actual_result = cipher.decrypt(text_to_decrypt, key)
    expected_result = decrypted_text
    assert actual_result == expected_result


@pytest.mark.parametrize(
    "text_to_encrypt, key, encrypted_text",
    [("be-right-back", 2, "dg-tkijv-dcem"), ("i'm.on.it", 5, "n'r.ts.ny")],
)
def test_encrypt_special_signs_sentence_with_positive_key(
    text_to_encrypt, key, encrypted_text
):
    cipher = CaesarCipher(list(ascii_lowercase))
    actual_result = cipher.encrypt(text_to_encrypt, key)
    expected_result = encrypted_text
    assert actual_result == expected_result


@pytest.mark.parametrize(
    "text_to_decrypt, key, decrypted_text",
    [("ugg,aqw^uqqp", 2, "see,you^soon"), ('bj_bnqq"xjj', 5, 'we_will"see')],
)
def test_decrypt_special_signs_sentence_with_positive_key(
    text_to_decrypt, key, decrypted_text
):
    cipher = CaesarCipher(list(ascii_lowercase))
    actual_result = cipher.decrypt(text_to_decrypt, key)
    expected_result = decrypted_text
    assert actual_result == expected_result


@pytest.mark.parametrize(
    "text_to_encrypt, key, encrypted_text", [("dąb", 2, "fąd"), ("kęs", 5, "pęx")]
)
def test_encrypt_polish_signs_sentence_with_positive_key(
    text_to_encrypt, key, encrypted_text
):
    cipher = CaesarCipher(list(ascii_lowercase))
    actual_result = cipher.encrypt(text_to_encrypt, key)
    expected_result = encrypted_text
    assert actual_result == expected_result


@pytest.mark.parametrize(
    "text_to_decrypt, key, decrypted_text",
    [("dtbfęm", 2, "brzdęk"), ("ptżzhm", 5, "kożuch")],
)
def test_decrypt_polish_signs_sentence_with_positive_key(
    text_to_decrypt, key, decrypted_text
):
    cipher = CaesarCipher(list(ascii_lowercase))
    actual_result = cipher.decrypt(text_to_decrypt, key)
    expected_result = decrypted_text
    assert actual_result == expected_result


# dodac test dla pojedynczej litery z -> a oraz a -> z


@pytest.mark.parametrize(
    "text_to_encrypt, key, encrypted_text", [("z", 1, "a"), ("zzz", 1, "aaa")]
)
def test_encrypt_letter_z_with_positive_key(text_to_encrypt, key, encrypted_text):
    cipher = CaesarCipher(list(ascii_lowercase))
    actual_result = cipher.encrypt(text_to_encrypt, key)
    expected_result = encrypted_text
    assert actual_result == expected_result


@pytest.mark.parametrize(
    "text_to_decrypt, key, decrypted_text",
    [("a", 1, "z"), ("aaa", 1, "zzz")],
)
def test_decrypt_letter_a_with_positive_key(text_to_decrypt, key, decrypted_text):
    cipher = CaesarCipher(list(ascii_lowercase))
    actual_result = cipher.decrypt(text_to_decrypt, key)
    expected_result = decrypted_text
    assert actual_result == expected_result


# dodac test dla psutego słowa
# dodac test dla key=0
