def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            # Determine whether the character is uppercase or lowercase
            is_upper = char.isupper()
            # Shift the character by the specified amount
            shifted_char = chr((ord(char) - ord('A' if is_upper else 'a') + shift) % 26 + ord('A' if is_upper else 'a'))
            result += shifted_char
        else:
            # If the character is not a letter, keep it unchanged
            result += char

    return result

# Example usage
plaintext = "Hello, World!"
shift_amount = 3
encrypted_text = caesar_cipher(plaintext, shift_amount)
decrypted_text = caesar_cipher(encrypted_text, -shift_amount)

print("Original Text:", plaintext)
print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)

shift = 3
char = "Y"
is_upper = char.isupper()
shifted_char = chr((ord(char) - ord('A' if is_upper else 'a') + shift) % 26 + ord('A' if is_upper else 'a'))


inner_0 = ord(char) - ord('A' if is_upper else 'a')
print(f"inner_0:{inner_0}")

plus_shift = inner_0 + shift
print(f"plus_shift:{plus_shift}")

plus_shift_mod = plus_shift %26
print(f"plus_shift_mod:{plus_shift_mod}")

plusAa = ord('A' if is_upper else 'a')
print(f"plusAa:{plusAa}")

total_calc = (ord(char) - ord('A' if is_upper else 'a') + shift) % 26 + ord('A' if is_upper else 'a')
print(f"total_calc:{total_calc}")

print(f"shifted_char:{shifted_char}")

