from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

def main():
    print("--- 🔐 Cryptography Project: RSA Asymmetric Encryption ---")

    # 1. Generate RSA Keys (This might take a split second)
    print("\n[*] Generating RSA 2048-bit keys...")
    key = RSA.generate(2048)
    private_key = key
    public_key = key.publickey()

    message = b"Top Secret RSA Message for Project 6 Evaluators!"
    print(f"[+] Original Message: {message.decode()}")

    # ==========================================
    #               ENCRYPTION
    # ==========================================
    # We encrypt using the PUBLIC key
    cipher_encrypt = PKCS1_OAEP.new(public_key)
    encrypted_message = cipher_encrypt.encrypt(message)
    
    # Converting to hex just so it prints nicely in the terminal
    hex_encrypted = binascii.hexlify(encrypted_message).decode()
    print(f"[+] Encrypted (Hex snippet): {hex_encrypted[:50]}...[truncated]")

    # ==========================================
    #               DECRYPTION
    # ==========================================
    # We decrypt using the PRIVATE key
    cipher_decrypt = PKCS1_OAEP.new(private_key)
    decrypted_message = cipher_decrypt.decrypt(encrypted_message)
    
    print(f"[+] Decrypted Message: {decrypted_message.decode()}\n")

if __name__ == "__main__":
    main()