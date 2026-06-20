import hashlib

def main():
    print("--- 🔍 Cryptography Project: SHA-256 Hashing ---")
    
    # The data we want to hash
    message = "Codec Technologies Internship is awesome!"
    print(f"\n[+] Original Message: {message}")

    # Generate the SHA-256 hash
    hash_object = hashlib.sha256(message.encode())
    hash_value = hash_object.hexdigest()
    
    print(f"[+] SHA-256 Hash: {hash_value}")
    print("\nNotice: Hashing is one-way! You cannot 'decrypt' this back to the original message. 😎")

if __name__ == "__main__":
    main()