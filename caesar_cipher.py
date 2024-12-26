def caesar_cipher_encrypt(plaintext):
    ciphertext = ""

    for char in plaintext:
        ciphertext += chr(ord(char) + 3)

    return ciphertext

plaintext = "HELLO"
ciphertext = caesar_cipher_encrypt(plaintext)

print(f"Plaintext: {plaintext}\nCiphertext: {ciphertext}")
