def caesar_cipher():
    def encrypt_decrypt(text, shift, mode):
        result = ""
        for char in text:
            if char.isalpha():
                start = ord('A') if char.isupper() else ord('a')
                if mode == 'encrypt':
                    code = (ord(char) - start + shift) % 26 + start
                elif mode == 'decrypt':
                    code = (ord(char) - start - shift) % 26 + start
                result += chr(code)
            else:
                result += char
        return result

    print("--- Caesar Cipher Program ---")
    
    # Continuous loop to keep running without restarting IDLE
    while True:
        message = input("\nEnter your message: ")
        
        while True:
            try:
                shift_value = int(input("Enter the shift value (number): "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        while True:
            choice = input("Do you want to (e)ncrypt or (d)ecrypt? ").lower()
            if choice == 'e':
                encrypted_message = encrypt_decrypt(message, shift_value, 'encrypt')
                print(f"\nEncrypted message: {encrypted_message}")
                break
            elif choice == 'd':
                decrypted_message = encrypt_decrypt(message, shift_value, 'decrypt')
                print(f"\nDecrypted message: {decrypted_message}")
                break
            else:
                print("Invalid choice. Please enter 'e' or 'd'.")

        # Ask if the user wants to go again
        again = input("\nDo you want to do another message? (y/n): ").lower()
        if again != 'y':
            print("Exiting program. Goodbye!")
            break

if __name__ == "__main__":
    caesar_cipher()
