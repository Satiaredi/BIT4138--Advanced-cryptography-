#!/usr/bin/env python3
"""
Substitution-Permutation Network (SPN) Implementation
Demonstrates modern block cipher design principles
"""

import struct

class SPNCipher:
    """
    Simple SPN (Substitution-Permutation Network) Implementation
    """
    
    def __init__(self, key, rounds=4):
        """
        Initialize SPN cipher
        
        Args:
            key: Encryption key (integer)
            rounds: Number of rounds
        """
        self.key = key
        self.rounds = rounds
        self.round_keys = self._generate_round_keys()
        
        # Standard AES-like S-Box
        self.sbox = [
            0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5,
            0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
            0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0,
            0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
            0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc,
            0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
            0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a,
            0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
            0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0,
            0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
            0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b,
            0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
            0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85,
            0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
            0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5,
            0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2
        ]
        
        # Inverse S-Box
        self.inverse_sbox = [0] * 256
        for i in range(256):
            self.inverse_sbox[self.sbox[i]] = i
        
        # Permutation table
        self.perm_table = [
            0, 4, 8, 12,
            1, 5, 9, 13,
            2, 6, 10, 14,
            3, 7, 11, 15
        ]
        
        # Inverse permutation table
        self.inverse_perm_table = [0] * 16
        for i in range(16):
            self.inverse_perm_table[self.perm_table[i]] = i
    
    def _generate_round_keys(self):
        """
        Generate round keys from master key
        """
        keys = []
        temp_key = self.key
        
        for i in range(self.rounds + 1):
            keys.append(temp_key & 0xFFFFFFFF)
            temp_key = ((temp_key << 5) | (temp_key >> 27)) ^ (i + 1)
        
        return keys
    
    def _substitute_bytes(self, block):
        """
        Apply S-Box substitution
        
        Args:
            block: 16 bytes
        
        Returns:
            Substituted bytes
        """
        result = []
        for byte in block:
            result.append(self.sbox[byte])
        return bytes(result)
    
    def _inverse_substitute_bytes(self, block):
        """
        Apply inverse S-Box substitution
        
        Args:
            block: 16 bytes
        
        Returns:
            Inverse substituted bytes
        """
        result = []
        for byte in block:
            result.append(self.inverse_sbox[byte])
        return bytes(result)
    
    def _permute_bits(self, block):
        """
        Apply bit permutation
        
        Args:
            block: 16 bytes (128 bits)
        
        Returns:
            Permuted bytes
        """
        # Convert to nibbles (4-bit chunks)
        nibbles = []
        for byte in block:
            nibbles.append((byte >> 4) & 0xF)
            nibbles.append(byte & 0xF)
        
        # Apply permutation
        permuted_nibbles = [nibbles[i] for i in self.perm_table]
        
        # Convert back to bytes
        result = []
        for i in range(0, len(permuted_nibbles), 2):
            byte = (permuted_nibbles[i] << 4) | permuted_nibbles[i + 1]
            result.append(byte)
        
        return bytes(result)
    
    def _inverse_permute_bits(self, block):
        """
        Apply inverse bit permutation
        
        Args:
            block: 16 bytes
        
        Returns:
            Inverse permuted bytes
        """
        nibbles = []
        for byte in block:
            nibbles.append((byte >> 4) & 0xF)
            nibbles.append(byte & 0xF)
        
        inverse_permuted_nibbles = [nibbles[i] for i in self.inverse_perm_table]
        
        result = []
        for i in range(0, len(inverse_permuted_nibbles), 2):
            byte = (inverse_permuted_nibbles[i] << 4) | inverse_permuted_nibbles[i + 1]
            result.append(byte)
        
        return bytes(result)
    
    def _add_round_key(self, block, round_num):
        """
        XOR block with round key
        
        Args:
            block: 16 bytes
            round_num: Round number
        
        Returns:
            XORed block
        """
        key = self.round_keys[round_num]
        result = []
        
        for i, byte in enumerate(block):
            key_byte = (key >> (8 * (i % 4))) & 0xFF
            result.append(byte ^ key_byte)
        
        return bytes(result)
    
    def encrypt_block(self, plaintext_block):
        """
        Encrypt a 16-byte block using SPN
        
        Args:
            plaintext_block: 16 bytes
        
        Returns:
            16-byte ciphertext
        """
        block = plaintext_block
        
        # Initial round key addition
        block = self._add_round_key(block, 0)
        
        # SPN Rounds
        for round_num in range(1, self.rounds):
            # Substitution
            block = self._substitute_bytes(block)
            
            # Permutation
            block = self._permute_bits(block)
            
            # Round key addition
            block = self._add_round_key(block, round_num)
        
        # Final round (no permutation)
        block = self._substitute_bytes(block)
        block = self._add_round_key(block, self.rounds)
        
        return block
    
    def decrypt_block(self, ciphertext_block):
        """
        Decrypt a 16-byte block using SPN
        
        Args:
            ciphertext_block: 16 bytes
        
        Returns:
            16-byte plaintext
        """
        block = ciphertext_block
        
        # Initial round key addition
        block = self._add_round_key(block, self.rounds)
        
        # Inverse S-Box
        block = self._inverse_substitute_bytes(block)
        
        # SPN Rounds in reverse
        for round_num in range(self.rounds - 1, 0, -1):
            # Round key addition
            block = self._add_round_key(block, round_num)
            
            # Inverse permutation
            block = self._inverse_permute_bits(block)
            
            # Inverse substitution
            block = self._inverse_substitute_bytes(block)
        
        # Final round key addition
        block = self._add_round_key(block, 0)
        
        return block
    
    def analyze_avalanche(self, plaintext_block):
        """
        Analyze avalanche effect by flipping one bit
        
        Args:
            plaintext_block: 16 bytes
        
        Returns:
            Avalanche analysis
        """
        # Encrypt original
        ciphertext1 = self.encrypt_block(plaintext_block)
        
        # Flip first bit
        modified_plaintext = bytearray(plaintext_block)
        modified_plaintext[0] ^= 0x01
        ciphertext2 = self.encrypt_block(bytes(modified_plaintext))
        
        # Count differing bits
        differing_bits = 0
        for b1, b2 in zip(ciphertext1, ciphertext2):
            differing_bits += bin(b1 ^ b2).count('1')
        
        return {
            'original_ciphertext': ciphertext1.hex(),
            'modified_ciphertext': ciphertext2.hex(),
            'differing_bits': differing_bits,
            'total_bits': 128,
            'avalanche_percentage': (differing_bits / 128) * 100
        }

def demonstrate_spn():
    """
    Demonstrate SPN cipher
    """
    print("=" * 70)
    print("Substitution-Permutation Network (SPN) Demonstration")
    print("=" * 70)
    
    # Initialize cipher
    key = 0xDEADBEEF
    cipher = SPNCipher(key, rounds=4)
    
    # Example 1: Basic encryption/decryption
    print("\n[Example 1] Basic Encryption and Decryption")
    print("-" * 70)
    
    plaintext = b"Hello World!!!!"
    print(f"Key: {key:08X}")
    print(f"Rounds: {cipher.rounds}")
    print(f"Plaintext: {plaintext}")
    print(f"Plaintext (hex): {plaintext.hex()}")
    
    ciphertext = cipher.encrypt_block(plaintext)
    print(f"Ciphertext (hex): {ciphertext.hex()}")
    
    decrypted = cipher.decrypt_block(ciphertext)
    print(f"Decrypted: {decrypted}")
    print(f"Match: {plaintext == decrypted}")
    
    # Example 2: Avalanche Effect
    print("\n[Example 2] Avalanche Effect Analysis")
    print("-" * 70)
    
    plaintext1 = b"HELLO WORLD!!!!"
    analysis = cipher.analyze_avalanche(plaintext1)
    
    print(f"Original plaintext: {plaintext1}")
    print(f"Modified plaintext: Change 1 bit")
    print(f"\nOriginal ciphertext:  {analysis['original_ciphertext']}")
    print(f"Modified ciphertext:  {analysis['modified_ciphertext']}")
    print(f"Differing bits: {analysis['differing_bits']} out of {analysis['total_bits']}")
    print(f"Avalanche effect: {analysis['avalanche_percentage']:.1f}%")
    print(f"\nStrong avalanche observed: {analysis['avalanche_percentage'] > 20}")
    
    # Example 3: S-Box Non-linearity
    print("\n[Example 3] S-Box Non-Linearity Properties")
    print("-" * 70)
    
    print("Sample S-Box mappings (showing non-linearity):")
    print("Input -> Output")
    for i in range(0, 16):
        print(f"{i:3d} (0x{i:02X}) -> {cipher.sbox[i]:3d} (0x{cipher.sbox[i]:02X})", end="  ")
        if (i + 1) % 4 == 0:
            print()
    
    # Example 4: Multiple rounds effect
    print("\n[Example 4] Effect of Multiple Rounds")
    print("-" * 70)
    
    plaintext = b"CRYPTOGRAPHY!!!"
    print(f"Plaintext: {plaintext}\n")
    
    for rounds in [1, 2, 4, 8]:
        cipher_temp = SPNCipher(key, rounds=rounds)
        ciphertext = cipher_temp.encrypt_block(plaintext)
        print(f"After {rounds} rounds: {ciphertext.hex()}")

if __name__ == "__main__":
    demonstrate_spn()
