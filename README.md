# Méthodes de Cryptologie

This repository contains materials related to cryptographic methods, including reports and Python scripts for various encryption techniques.

## Contents

- **RapportCryptage.pdf**: A detailed report on cryptographic methods.
- **RapportCryptage.tex**: The LaTeX source file for the report.
- **codeCesarAffine.py**: Python script implementing Caesar and Affine ciphers.
- **codeCrptologie.py**: Python script covering general cryptographic methods.
- **codeVigenere.py**: Python script for the Vigenère cipher.

## Cryptographic Methods

### Inverse Code
- **Description**: Encrypts a message by reversing its characters. Decryption is performed by reversing the process.
- **Functions**: 
  - `crypter(message)`: Encrypts the message by reversing it.
  - `decrypter_crypt(message)`: Decrypts the message by reversing it.

### Caesar Cipher (Simple)
- **Description**: Shifts each letter in the plaintext by a fixed number of positions down the alphabet.
- **Encryption Formula**: \( y = (x + b) \mod n \)
- **Decryption Formula**: \( y = (x - b) \mod n \)
- **Functions**:
  - `decalage_mot(mot, k)`: Encrypts the word by shifting each letter by \( k \) positions.
  - `decryptage_decalage_mot(mot, k)`: Decrypts the word by shifting each letter by \( -k \) positions.

### Vigenère Cipher
- **Description**: Uses a keyword to shift the characters in the plaintext. Each letter in the keyword determines the shift for the corresponding letter in the plaintext.
- **Functions**:
  - `vigenere_encrypt(mot, clé)`: Encrypts the message using the Vigenère cipher with the given key.
  - `vigenere_decrypt(mot, clé)`: Decrypts the message using the Vigenère cipher with the given key.

### Affine Cipher
- **Description**: Applies a linear transformation to the numerical equivalent of each letter in the plaintext.
- **Encryption Formula**: \( y = (ax + b) \mod n \)
- **Decryption Formula**: \( y = a^{-1}(x - b) \mod n \)
- **Functions**:
  - `affine_encrypt(mot, a, b)`: Encrypts the word using the Affine cipher.
  - `affine_decrypt(mot, a, b)`: Decrypts the word using the Affine cipher.

## Requirements

- Python 3.x
