"""
Caesar Cipher Tool

This script allows a user to encrypt and decrypt text using the Caesar cipher algorithm.
The user can input a message and a shift value for both encryption and decryption.

For educational purposes only.
"""

def caesar_encrypt(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def main():
    print("Caesar Cipher Tool (Educational Use Only)")
    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").strip().lower()
    message = input("Enter your message: ")
    try:
        shift = int(input("Enter shift value (integer): "))
    except ValueError:
        print("Invalid shift value. Please enter an integer.")
        return
    if choice == 'e':
        encrypted = caesar_encrypt(message, shift)
        print(f"Encrypted message: {encrypted}")
    elif choice == 'd':
        decrypted = caesar_decrypt(message, shift)
        print(f"Decrypted message: {decrypted}")
    else:
        print("Invalid choice. Please select 'e' or 'd'.")

if __name__ == "__main__":
    main()
