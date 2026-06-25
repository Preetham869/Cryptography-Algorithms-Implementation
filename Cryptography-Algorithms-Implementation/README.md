Cryptography Algorithms Implementation using Python 🛡️

This repository contains my submission for Project 6 of the Codec Technologies Internship.
It demonstrates the implementation of core cryptographic concepts, from basic string manipulation to advanced file-locking mechanisms.

🌟 Features Included:

AES String Encryption (aes_encryption.py): Demonstrates Symmetric Encryption where the same 128-bit key is used to both encrypt and decrypt data.

RSA Encryption (rsa_encryption.py): Demonstrates Asymmetric Encryption utilizing a 2048-bit Public/Private key pair for highly secure data transmission.

SHA-256 Hashing (sha256_hashing.py): Demonstrates cryptographic Hashing, creating a fixed-size, irreversible digital fingerprint.

🔥 Advanced AES File Vault (aes_file_encryption.py): A practical, interactive utility that uses PBKDF2 (Password-Based Key Derivation Function 2) with 1,000,000 iterations and a cryptographic salt to turn a human password into a secure 256-bit key to encrypt and decrypt actual files (.enc).

⚙️ How to Run:

Ensure you have the pycryptodome library installed:
pip install pycryptodome

(Run the scripts in your terminal to interact with the encryption tools!)

📸 Execution Screenshots

1. Advanced AES File Encryption (File Vault)

2. Basic AES String Encryption

3. SHA-256 Hashing Output

4. RSA Encryption Output