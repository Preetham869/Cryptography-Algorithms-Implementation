from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes
import os

# --- 🧠 THE UPGRADE: PBKDF2 ---
# This takes a weak human password (like 'dog') and "cooks" it 1,000,000 times 
# to turn it into a super-strong, unbreakable 256-bit AES key.
def derive_key(password: str, salt: bytes) -> bytes:
    print("[*] Cooking password into a secure key (this takes a second)...")
    return PBKDF2(password, salt, dkLen=32, count=1_000_000, hmac_hash_module=SHA256)

def encrypt_file(filepath, password):
    # --- 🧠 BULLETPROOF UPGRADE ---
    # Automatically find the folder this script is living in
    script_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(script_dir, filepath)

    if not os.path.exists(full_path):
        print(f"[-] File not found! Make sure '{filepath}' is in the same folder as this script.")
        return

    salt = get_random_bytes(16)
    key = derive_key(password, salt)
    
    with open(full_path, "rb") as f:
        plaintext = f.read()
        
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)
    out_path = full_path + ".enc"
    
    with open(out_path, "wb") as f:
        # We pack the salt, nonce, tag, and ciphertext into one locked file
        f.write(salt + cipher.nonce + tag + ciphertext)
    
    print(f"\n[+] SUCCESS! File Encrypted -> {out_path} 🔒")
    print("    (Try opening it in notepad... it's total gibberish!)")

def decrypt_file(filepath, password):
    # --- 🧠 BULLETPROOF UPGRADE ---
    script_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(script_dir, filepath)

    if not os.path.exists(full_path):
        print(f"[-] Encrypted file not found! Make sure it is in the same folder.")
        return

    with open(full_path, "rb") as f:
        data = f.read()
        
    # Unpack the data
    salt, nonce, tag, ciphertext = data[:16], data[16:32], data[32:48], data[48:]
    key = derive_key(password, salt)
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    
    try:
        plaintext = cipher.decrypt_and_verify(ciphertext, tag)
        out_path = full_path.replace(".enc", ".decrypted.txt")
        with open(out_path, "wb") as f:
            f.write(plaintext)
        print(f"\n[+] SUCCESS! File Decrypted -> {out_path} 🔓")
    except ValueError:
        print("\n[❌] DECRYPTION FAILED! Incorrect password or corrupted file.")

def main():
    print("--- 🗄️ Advanced AES File Vault ---")
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    choice = input("Select mode (1 or 2): ")
    
    if choice == '1':
        file_to_encrypt = input("Enter filename to encrypt (e.g., secret.txt): ")
        password = input("Enter a strong password to lock it: ")
        encrypt_file(file_to_encrypt, password)
    elif choice == '2':
        file_to_decrypt = input("Enter filename to decrypt (e.g., secret.txt.enc): ")
        password = input("Enter the password to unlock it: ")
        decrypt_file(file_to_decrypt, password)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()