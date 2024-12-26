def caesar_cipher_encrypt(plaintext):
    ciphertext = ""

    for char in plaintext:
        ciphertext += chr(ord(char) + 3)

    return ciphertext

def caesar_cipher_decrypt(ciphertext):
    plaintext = ""

    for char in ciphertext:
        plaintext += chr(ord(char) - 3)

    return plaintext

plaintext = "HELLO"
print(f"Plaintext: {plaintext}")

ciphertext = caesar_cipher_encrypt(plaintext)
print(f"Ciphertext: {ciphertext}")

plaintext = caesar_cipher_decrypt(ciphertext)
print(f"Decrypted: {plaintext}")
