# Q34. Write a program to encrypt a message
# using Caesar Cipher technique and decrypt
# it back to the original message.

text = input("Enter a message : ")

shift = 3

encrypted = ""

# encryption
for ch in text:

    if ch.isalpha():

        new_char = chr(ord(ch) + shift)

        encrypted = encrypted + new_char

    else:

        encrypted = encrypted + ch

print("\nEncrypted Message :", encrypted)

decrypted = ""

# decryption
for ch in encrypted:

    if ch.isalpha():

        original = chr(ord(ch) - shift)

        decrypted = decrypted + original

    else:

        decrypted = decrypted + ch

print("Decrypted Message :", decrypted)