# 3DES-CBC Decryption Utility

This is a simple Python script to decrypt data encrypted with 3DES (Triple DES) in CBC mode, where the ciphertext includes a prepended 8-byte IV and is Base64 encoded.

## Features
- Accepts a 24-byte key (required by 3DES).
- Accepts Base64-encoded encrypted input.
- Extracts IV and ciphertext automatically.
- Returns the decrypted plaintext, handling padding and decoding.
- Handles errors gracefully and informs the user.

## Requirements
- Python 3.x
- `pycryptodome` library

Install dependencies via pip:

```bash
pip install pycryptodome
```

## Usage
Run the script:

```bash
python decrypt_3des_cbc.py
```

You will be prompted to enter:
- The 24-byte decryption key.
- The Base64 encoded ciphertext string.

### Example
```plaintext
Please enter the 24-byte key: myCustomSecureKey!123456789
Please enter the Base64 encrypted string: Zk8j10B9RswKBr98lKTyyfTglPl78Bn+
[+] Decrypted output: secret_pass_2024
```

## Notes
- The key must be exactly 24 bytes long (characters encoded in UTF-8).
- The encrypted data must be Base64 encoded and contain the IV in the first 8 bytes.
- The script strips null bytes used for padding.

## License
MIT License — Feel free to use and modify as needed.
