#!/usr/bin/env python3
"""
Advanced Cryptography - Main Entry Point
Provides a unified interface for all cryptographic implementations
"""

import sys
import os
from pathlib import Path

# Add Week1 directory to path for imports
sys.path.insert(0, str(Path(__file__).parent / "Week1-Cryptography"))

from caesar_cipher import caesar_encrypt, caesar_decrypt, caesar_bruteforce
from vigenere_cipher import vigenere_encrypt, vigenere_decrypt


def print_menu():
    """Display main menu options"""
    print("\n" + "="*50)
    print("    ADVANCED CRYPTOGRAPHY TOOLKIT")
    print("="*50)
    print("\n1. Caesar Cipher")
    print("   a) Encrypt")
    print("   b) Decrypt")
    print("   c) Brute Force Attack")
    print("\n2. Vigenere Cipher")
    print("   a) Encrypt")
    print("   b) Decrypt")
    print("\n3. Exit")
    print("\n" + "="*50)


def caesar_menu():
    """Caesar cipher operations menu"""
    print("\n--- Caesar Cipher ---")
    choice = input("Select operation (a/b/c): ").strip().lower()
    
    if choice == 'a':
        plaintext = input("Enter plaintext: ")
        try:
            shift = int(input("Enter shift value (1-25): "))
            if not 1 <= shift <= 25:
                print("❌ Shift value must be between 1 and 25")
                return
            result = caesar_encrypt(plaintext, shift)
            print(f"✓ Encrypted: {result}")
        except ValueError:
            print("❌ Invalid shift value")
    
    elif choice == 'b':
        ciphertext = input("Enter ciphertext: ")
        try:
            shift = int(input("Enter shift value (1-25): "))
            if not 1 <= shift <= 25:
                print("❌ Shift value must be between 1 and 25")
                return
            result = caesar_decrypt(ciphertext, shift)
            print(f"✓ Decrypted: {result}")
        except ValueError:
            print("❌ Invalid shift value")
    
    elif choice == 'c':
        ciphertext = input("Enter ciphertext to attack: ")
        print("\nBrute Force Attack Results:")
        print("-" * 40)
        for shift, plaintext in caesar_bruteforce(ciphertext):
            print(f"Shift {shift:2d}: {plaintext}")
    
    else:
        print("❌ Invalid choice")


def vigenere_menu():
    """Vigenere cipher operations menu"""
    print("\n--- Vigenere Cipher ---")
    choice = input("Select operation (a/b): ").strip().lower()
    
    if choice == 'a':
        plaintext = input("Enter plaintext: ")
        key = input("Enter encryption key: ").strip()
        if not key or not key.isalpha():
            print("❌ Key must contain only alphabetic characters")
            return
        result = vigenere_encrypt(plaintext, key)
        print(f"✓ Encrypted: {result}")
    
    elif choice == 'b':
        ciphertext = input("Enter ciphertext: ")
        key = input("Enter decryption key: ").strip()
        if not key or not key.isalpha():
            print("❌ Key must contain only alphabetic characters")
            return
        result = vigenere_decrypt(ciphertext, key)
        print(f"✓ Decrypted: {result}")
    
    else:
        print("❌ Invalid choice")


def main():
    """Main application loop"""
    print("\n🔐 Welcome to Advanced Cryptography Toolkit")
    print("Educational tool for classical cryptographic algorithms\n")
    
    while True:
        print_menu()
        choice = input("\nSelect option (1/2/3): ").strip()
        
        if choice == '1':
            caesar_menu()
        elif choice == '2':
            vigenere_menu()
        elif choice == '3':
            print("\n👋 Goodbye!\n")
            break
        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Program interrupted. Goodbye!\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ An error occurred: {e}\n")
        sys.exit(1)
