import string

# Encryption function
def encrypt_text(content, n, m):
    encrypted = []
    for char in content:
        if char in string.ascii_lowercase:  # Lowercase letters
            encrypted_char = chr((ord(char) - ord('a') + n * m) % 26 + ord('a'))
            encrypted.append(encrypted_char)
        elif char in string.ascii_uppercase:  # Uppercase letters
            if ord(char) >= ord('N'):  # Uppercase (N-Z)
                encrypted_char = chr((ord(char) - ord('A') + n) % 26 + ord('A'))
            else:  # Uppercase (A-M)
                encrypted_char = chr((ord(char) - ord('A') + m ** 2) % 26 + ord('A'))
            encrypted.append(encrypted_char)
        else:  # Special characters and numbers remain unchanged
            encrypted.append(char)
    return ''.join(encrypted)

# Decryption function
def decrypt_text(content, n, m):
    decrypted = []
    for char in content:
        if char in string.ascii_lowercase:  # Lowercase letters
            decrypted_char = chr((ord(char) - ord('a') - n * m) % 26 + ord('a'))
            decrypted.append(decrypted_char)
        elif char in string.ascii_uppercase:  # Uppercase letters
            if ord(char) >= ord('N'):  # Uppercase (N-Z)
                decrypted_char = chr((ord(char) - ord('A') - n) % 26 + ord('A'))
            else:  # Uppercase (A-M)
                decrypted_char = chr((ord(char) - ord('A') - m ** 2) % 26 + ord('A'))
            decrypted.append(decrypted_char)
        else:  # Special characters and numbers remain unchanged
            decrypted.append(char)
    return ''.join(decrypted)

# Verify correctness of decryption
def verify_decryption(original, decrypted):
    return original == decrypted

# Main process
if __name__ == "__main__":
    # User inputs
    n = int(input("Enter value of n: "))
    m = int(input("Enter value of m: "))

    # Read raw_text.txt
    with open("raw_text.txt", "r") as file:
        raw_content = file.read()

    # Encrypt content
    encrypted_content = encrypt_text(raw_content, n, m)

    # Write encrypted text to encrypted_text.txt
    with open("encrypted_text.txt", "w") as file:
        file.write(encrypted_content)

    print("Encryption completed. Encrypted content saved to 'encrypted_text.txt'.")
    
    # Decrypt content
    decrypted_content = decrypt_text(encrypted_content, n, m)

    # Write decrypted content to decrypted_text.txt
    with open("decrypted_text.txt", "w") as file:
        file.write(decrypted_content)

    print("Decryption completed. Decrypted content saved to 'decrypted_text.txt'.")

    # Verify decryption
    if verify_decryption(raw_content, decrypted_content):
        print("Decryption verified successfully.")
    else:
        print("Decryption failed.")
