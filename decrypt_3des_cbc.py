from Crypto.Cipher import DES3
from base64 import b64decode

def decrypt_3des_cbc(encoded_text, key_24bytes):
    try:
        # Decode Base64 and separate IV and encrypted content
        raw_data = b64decode(encoded_text)
        initialization_vector = raw_data[:8]
        encrypted_payload = raw_data[8:]

        # Initialize 3DES cipher in CBC mode with given key and IV
        cipher = DES3.new(key_24bytes, DES3.MODE_CBC, iv=initialization_vector)
        decrypted_bytes = cipher.decrypt(encrypted_payload)

        # Strip null bytes at the end and decode to string
        return decrypted_bytes.rstrip(b"\0").decode('utf-8', errors='ignore')

    except Exception as error:
        return f"Error during decryption: {error}"

if __name__ == "__main__":
    secret_key = input("Please enter the 24-byte key: ").encode('utf-8')
    if len(secret_key) != 24:
        print(f"Invalid key length: {len(secret_key)} bytes. Expected exactly 24 bytes.")
        exit(1)

    encrypted_input = input("Please enter the Base64 encrypted string: ").strip()

    output = decrypt_3des_cbc(encrypted_input, secret_key)
    print("[+] Decrypted output:", output)
