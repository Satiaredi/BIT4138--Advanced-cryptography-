#!/usr/bin/env python3
"""
One-Time Pad (OTP) Simulation
Theoretically unbreakable encryption system

Requirements:
- Key length = Message length
- Key is truly random
- Key used only once
"""

import random
import secrets
from binascii import hexlify, unhexlify

def generate_otp_key(length):
    """
    Generate a truly random OTP key
    Uses secrets module for cryptographically secure randomness
    
    Args:
        length: Length of key in bytes
    
    Returns:
        Random bytes of specified length
    """
    return secrets.token_bytes(length)

def otp_encrypt(plaintext, key):
    """
    Encrypt plaintext using One-Time Pad
    
    Args:
        plaintext: String to encrypt
        key: Bytes key (must be >= plaintext length)
    
    Returns:
        Encrypted bytes as hex string
    """
    plaintext_bytes = plaintext.encode()
    
    if len(key) < len(plaintext_bytes):
        raise ValueError("Key must be at least as long as plaintext")
    
    # XOR plaintext with key
    ciphertext = bytes(p ^ k for p, k in zip(plaintext_bytes, key[:len(plaintext_bytes)]))
    return hexlify(ciphertext).decode()

def otp_decrypt(ciphertext_hex, key):
    """
    Decrypt OTP ciphertext
    
    Args:
        ciphertext_hex: Encrypted bytes as hex string
        key: Bytes key
    
    Returns:
        Decrypted plaintext string
    """
    ciphertext = unhexlify(ciphertext_hex)
    plaintext = bytes(c ^ k for c, k in zip(ciphertext, key[:len(ciphertext)]))
    return plaintext.decode()

def demonstrate_otp():
    """
    Demonstrate OTP encryption and decryption
    """
    print("=" * 60)
    print("One-Time Pad (OTP) Simulation")
    print("=" * 60)
    
    # Example 1: Basic OTP
    print("\n[Example 1] Basic OTP Encryption")
    print("-" * 60)
    
    message = "ATTACK AT DAWN"
    key = generate_otp_key(len(message))
    
    print(f"Plaintext: {message}")
    print(f"Key (hex): {hexlify(key).decode()}")
    
    ciphertext = otp_encrypt(message, key)
    print(f"Ciphertext (hex): {ciphertext}")
    
    decrypted = otp_decrypt(ciphertext, key)
    print(f"Decrypted: {decrypted}")
    
    # Example 2: Key reuse vulnerability
    print("\n[Example 2] Security: Key Reuse Vulnerability")
    print("-" * 60)
    
    message1 = "HELLO WORLD"
    message2 = "GOODBYE ALL"
    key_reused = generate_otp_key(len(message1))
    
    cipher1 = otp_encrypt(message1, key_reused)
    cipher2 = otp_encrypt(message2, key_reused)
    
    print(f"Message 1: {message1}")
    print(f"Message 2: {message2}")
    print(f"Both encrypted with SAME key (VULNERABLE!)")
    print(f"Ciphertext 1: {cipher1}")
    print(f"Ciphertext 2: {cipher2}")
    print(f"\nXOR of ciphertexts reveals: {xor_ciphertexts(cipher1, cipher2)}")
    print("Warning: Reusing OTP key breaks security!")
    
    # Example 3: Binary representation
    print("\n[Example 3] Binary OTP Operation")
    print("-" * 60)
    
    char = 'A'
    key_byte = secrets.token_bytes(1)[0]
    
    print(f"Plaintext char: {char} (ASCII {ord(char)}, Binary: {bin(ord(char))})")
    print(f"Key byte: {key_byte} (Binary: {bin(key_byte)})")
    
    ciphertext_byte = ord(char) ^ key_byte
    print(f"Ciphertext: {ciphertext_byte} (Binary: {bin(ciphertext_byte)})")
    
    decrypted_char = chr(ciphertext_byte ^ key_byte)
    print(f"Decrypted: {decrypted_char}")

def xor_ciphertexts(cipher1_hex, cipher2_hex):
    """
    XOR two ciphertexts (demonstrates vulnerability of key reuse)
    """
    cipher1 = unhexlify(cipher1_hex)
    cipher2 = unhexlify(cipher2_hex)
    
    result = bytes(c1 ^ c2 for c1, c2 in zip(cipher1, cipher2))
    return hexlify(result).decode()

if __name__ == "__main__":
    demonstrate_otp()
