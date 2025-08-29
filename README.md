# Méthodes de Cryptologie

This repository contains materials related to cryptographic methods, including reports and Python scripts for various encryption techniques.

---

## Contents

- **`RapportCryptage.pdf`** — A detailed report on cryptographic methods.  
- **`RapportCryptage.tex`** — The LaTeX source file for the report.  
- **`codeCesarAffine.py`** — Python script implementing Caesar and Affine ciphers.  
- **`codeCrptologie.py`** — Python script covering general cryptographic methods.  
- **`codeVigenere.py`** — Python script for the Vigenère cipher.

---

## Cryptographic Methods

### Inverse Code

**Description**  
Encrypts a message by reversing its characters. Decryption is done by reversing the process.

**Functions**
- `crypter(message)` — Encrypts the message by reversing it.  
- `decrypter_crypt(message)` — Decrypts the message by reversing it.

---

### Caesar Cipher (Simple)

**Description**  
Shifts each letter in the plaintext by a fixed number of positions down the alphabet.

**Formulas**
- Encryption:    \( y = (x + b) \mod n \)  
- Decryption:    \( y = (x - b) \mod n \)

**Functions**
- `decalage_mot(mot, k)` — Encrypts by shifting each letter by `k` positions.  
- `decryptage_decalage_mot(mot, k)` — Decrypts by shifting each letter by `-k` positions.

---

### Vigenère Cipher

**Description**  
Uses a keyword to shift characters in the plaintext. Each letter in the keyword defines the shift for the corresponding plaintext letter.

**Functions**
- `vigenere_encrypt(mot, clé)` — Encrypts using the Vigenère cipher with the given key.  
- `vigenere_decrypt(mot, clé)` — Decrypts using the Vigenère cipher with the given key.

---

### Affine Cipher

**Description**  
Applies a linear transformation to the numerical equivalent of each letter in the plaintext.

**Formulas**
- Encryption:    \( y = (ax + b) \mod n \)  
- Decryption:    \( y = a^{-1}(x - b) \mod n \)

**Functions**
- `affine_encrypt(mot, a, b)` — Encrypts using the Affine cipher.  
- `affine_decrypt(mot, a, b)` — Decrypts using the Affine cipher.

---

## Requirements

- Python 3.x
