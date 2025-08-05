import random
import string

chars = " " + string.ascii_letters + string.punctuation + string.digits
characters = list(chars)
keys = characters.copy()
random.shuffle(keys)

# print(f"Chars: {characters}")

# print("\n\n")

# print(f"Keys : {keys}")

# ENCRYPT
def encrypt():
    plain_text = input("Enter your message: ")
    cipher_text = ""

    for letter in plain_text:
        index = characters.index(letter)
        cipher_text += keys[index]

    print(f"original text: {plain_text}")
    print(f"Cipher text  : {cipher_text}")


# DECRYPT
def decrypt():
    cipher_text = input("Enter your cipher text: ")
    plain_text = ""

    for letter in cipher_text:
        index = keys.index(letter)
        plain_text += characters[index]

    print(f"Cipher text  : {cipher_text}")
    print(f"original text: {plain_text}")

encrypt()
decrypt()