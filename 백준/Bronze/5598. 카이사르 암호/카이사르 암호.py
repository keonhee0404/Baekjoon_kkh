def decode_caesar_cipher(cipher_text):
    decoded_text = []

    for char in cipher_text:
        # Calculate the original character by shifting 3 places back
        original_char = chr((ord(char) - 3 - 65) % 26 + 65)
        decoded_text.append(original_char)

    return ''.join(decoded_text)


cipher_text = input().strip()


decoded_text = decode_caesar_cipher(cipher_text)


print(decoded_text)
