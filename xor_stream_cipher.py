#!/usr/bin/env python3
"""
XOR Stream Cipher Implementation
Demonstration of stream cipher encryption using XOR operations
"""

def xor_encrypt(plaintext, keystream):
    """
    Encrypt plaintext using XOR with keystream
    
    Args:
        plaintext: String to encrypt
        keystream: String/bytes to use as key
    
    Returns:
        Encrypted bytes as hex string
    """
    # Convert to bytes
    plaintext_bytes = plaintext.encode()
    keystream_bytes = keystream.encode() if isinstance(keystream, str) else keystream
    
    # Repeat keystream if necessary
    if len(keystream_bytes) < len(plaintext_bytes):
        repeats = (len(plaintext_bytes) // len(keystream_bytes)) + 1
        keystream_bytes = (keystream_bytes * repeats)[:len(plaintext_bytes)]
    
    # XOR operation
    ciphertext = bytes(a ^ b for a, b in zip(plaintext_bytes, keystream_bytes))
    return ciphertext.hex()

def xor_decrypt(ciphertext_hex, keystream):
    """
    Decrypt ciphertext using XOR with keystream
    
    Args:
        ciphertext_hex: Encrypted bytes as hex string
        keystream: String/bytes to use as key
    
    Returns:
        Decrypted plaintext string
    """
    ciphertext = bytes.fromhex(ciphertext_hex)
    keystream_bytes = keystream.encode() if isinstance(keystream, str) else keystream
    
    # Repeat keystream if necessary
    if len(keystream_bytes) < len(ciphertext):
        repeats = (len(ciphertext) // len(keystream_bytes)) + 1
        keystream_bytes = (keystream_bytes * repeats)[:len(ciphertext)]
    
    # XOR operation (same as encryption for XOR)
    plaintext = bytes(a ^ b for a, b in zip(ciphertext, keystream_bytes))
    return plaintext.decode()

if __name__ == "__main__":
    print("=" * 50)
    print("XOR Stream Cipher Demo")
    print("=" * 50)
    
    # Example 1: Simple encryption
    plaintext = "Hello"
    keystream = "SECRET"
    
    print(f"\nPlaintext: {plaintext}")
    print(f"Keystream: {keystream}")
    
    ciphertext = xor_encrypt(plaintext, keystream)
    print(f"Ciphertext (hex): {ciphertext}")
    
    decrypted = xor_decrypt(ciphertext, keystream)
    print(f"Decrypted: {decrypted}")
    
    # Example 2: Binary representation
    print("\n" + "=" * 50)
    print("Binary Representation")
    print("=" * 50)
    
    char1 = 'A'
    char2 = 'K'
    
    print(f"\nCharacter 1: {char1} (ASCII {ord(char1)}, Binary: {bin(ord(char1))})")
    print(f"Character 2: {char2} (ASCII {ord(char2)}, Binary: {bin(ord(char2))})")
    
    xor_result = ord(char1) ^ ord(char2)
    print(f"XOR Result: {xor_result} (Binary: {bin(xor_result)}, Char: {chr(xor_result) if 32 <= xor_result < 127 else 'Non-printable'})")
