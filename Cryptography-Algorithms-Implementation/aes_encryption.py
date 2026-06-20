from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def main():
    print("--- 🔒 Cryptography Project: AES Encryption ---")

    # 1. Generate a random 16-byte (128-bit) secret key
    # Think of this as the physical key to a padlock.
    secret_key = get_random_bytes(16)
    
    # 2. The secret message we want to hide
    original_message = b"Codec Technologies Internship: Project 6 Complete!"
    print(f"\n[+] Original Message: {original_message.decode()}")

    # ==========================================
    #               ENCRYPTION
    # ==========================================
    # Create the cipher object (the padlock)
    cipher_encrypt = AES.new(secret_key, AES.MODE_EAX)
    
    # Encrypt the message to get ciphertext and a verification tag
    ciphertext, tag = cipher_encrypt.encrypt_and_digest(original_message)
    nonce = cipher_encrypt.nonce # We need this unique number to decrypt later

    print(f"[+] Encrypted Message (Ciphertext): {ciphertext}")

    # ==========================================
    #               DECRYPTION
    # ==========================================
    # Create a new cipher object using the SAME secret key and nonce
    cipher_decrypt = AES.new(secret_key, AES.MODE_EAX, nonce=nonce)
    
    # Decrypt the message back to normal text
    decrypted_message = cipher_decrypt.decrypt_and_verify(ciphertext, tag)
    
    print(f"[+] Decrypted Message: {decrypted_message.decode()}\n")
    print("Mission Accomplished. 😎")

if __name__ == "__main__":
    main()