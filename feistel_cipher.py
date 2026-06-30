#!/usr/bin/env python3
"""
Feistel Cipher Implementation
Demonstrates block cipher structure and operation

Formula:
  L_i = R_{i-1}
  R_i = L_{i-1} XOR F(R_{i-1}, K_i)
"""

import struct
from typing import Tuple, List

class FeistelCipher:
    """
    Simple Feistel Cipher Implementation
    """
    
    def __init__(self, key: int, rounds: int = 4):
        """
        Initialize Feistel cipher
        
        Args:
            key: Integer key for encryption
            rounds: Number of rounds (default 4)
        """
        self.key = key
        self.rounds = rounds
        self.round_keys = self._generate_round_keys()
    
    def _generate_round_keys(self) -> List[int]:
        """
        Generate round keys from main key
        """
        keys = []
        temp_key = self.key
        
        for i in range(self.rounds):
            # Simple key scheduling
            temp_key = ((temp_key << 7) | (temp_key >> 25)) & 0xFFFFFFFF
            temp_key ^= (i + 1)
            keys.append(temp_key & 0xFFFF)
        
        return keys
    
    def _f_function(self, right_half: int, round_key: int) -> int:
        """
        F function: S-box and permutation simulation
        
        Args:
            right_half: Right half of block
            round_key: Round key
        
        Returns:
            F function output
        """
        # Mix with round key
        mixed = right_half ^ round_key
        
        # Simulate S-box substitution
        result = 0
        for i in range(4):
            byte_val = (mixed >> (i * 8)) & 0xFF
            # Simple substitution
            byte_val = ((byte_val + 1) ^ 0xAA) & 0xFF
            result |= (byte_val << (i * 8))
        
        # Permutation: bit rotation
        result = ((result << 5) | (result >> 27)) & 0xFFFFFFFF
        
        return result
    
    def _split_block(self, block: int) -> Tuple[int, int]:
        """
        Split 32-bit block into two 16-bit halves
        """
        left = (block >> 16) & 0xFFFF
        right = block & 0xFFFF
        return left, right
    
    def _merge_block(self, left: int, right: int) -> int:
        """
        Merge two 16-bit halves into 32-bit block
        """
        return ((left & 0xFFFF) << 16) | (right & 0xFFFF)
    
    def encrypt_block(self, plaintext_block: int) -> int:
        """
        Encrypt a single block using Feistel structure
        
        Args:
            plaintext_block: 32-bit plaintext block
        
        Returns:
            32-bit ciphertext block
        """
        L, R = self._split_block(plaintext_block)
        
        # Feistel rounds
        for round_num in range(self.rounds):
            # L_i = R_{i-1}
            L_new = R
            
            # R_i = L_{i-1} XOR F(R_{i-1}, K_i)
            F_output = self._f_function(R, self.round_keys[round_num])
            R_new = L ^ F_output
            
            L = L_new
            R = R_new
        
        # Final swap
        L, R = R, L
        
        return self._merge_block(L, R)
    
    def decrypt_block(self, ciphertext_block: int) -> int:
        """
        Decrypt a single block (reverse Feistel)
        
        Args:
            ciphertext_block: 32-bit ciphertext block
        
        Returns:
            32-bit plaintext block
        """
        L, R = self._split_block(ciphertext_block)
        
        # Feistel rounds in reverse
        for round_num in range(self.rounds - 1, -1, -1):
            # Reverse operations
            L_new = R
            F_output = self._f_function(L, self.round_keys[round_num])
            R_new = L ^ F_output
            
            L = L_new
            R = R_new
        
        # Final swap
        L, R = R, L
        
        return self._merge_block(L, R)
    
    def analyze_avalanche(self, plaintext: int) -> dict:
        """
        Analyze avalanche effect by flipping one bit
        
        Args:
            plaintext: Original plaintext
        
        Returns:
            Dictionary with avalanche analysis
        """
        # Encrypt original
        ciphertext1 = self.encrypt_block(plaintext)
        
        # Flip one bit
        modified_plaintext = plaintext ^ 1
        ciphertext2 = self.encrypt_block(modified_plaintext)
        
        # Count differing bits
        xor_result = ciphertext1 ^ ciphertext2
        differing_bits = bin(xor_result).count('1')
        
        return {
            'original_plaintext': format(plaintext, '032b'),
            'modified_plaintext': format(modified_plaintext, '032b'),
            'original_ciphertext': format(ciphertext1, '032b'),
            'modified_ciphertext': format(ciphertext2, '032b'),
            'xor_ciphertexts': format(xor_result, '032b'),
            'differing_bits': differing_bits,
            'avalanche_percentage': (differing_bits / 32) * 100
        }

def demonstrate_feistel():
    """
    Demonstrate Feistel cipher
    """
    print("=" * 70)
    print("Feistel Cipher Demonstration")
    print("=" * 70)
    
    # Initialize cipher
    key = 0xDEADBEEF
    cipher = FeistelCipher(key, rounds=4)
    
    # Example 1: Basic encryption/decryption
    print("\n[Example 1] Basic Encryption and Decryption")
    print("-" * 70)
    
    plaintext = 0x12345678
    print(f"Key: {key:08X}")
    print(f"Rounds: {cipher.rounds}")
    print(f"Plaintext: {plaintext:032b} ({plaintext:08X})")
    
    ciphertext = cipher.encrypt_block(plaintext)
    print(f"Ciphertext: {ciphertext:032b} ({ciphertext:08X})")
    
    decrypted = cipher.decrypt_block(ciphertext)
    print(f"Decrypted: {decrypted:032b} ({decrypted:08X})")
    print(f"Match: {plaintext == decrypted}")
    
    # Example 2: Avalanche Effect
    print("\n[Example 2] Avalanche Effect Analysis")
    print("-" * 70)
    
    plaintext1 = 0x00000000
    plaintext2 = 0x00000001  # Flip one bit
    
    print(f"Original plaintext:  {plaintext1:032b}")
    print(f"Modified plaintext:  {plaintext2:032b}")
    print(f"Bit difference: 1 bit")
    
    cipher1 = cipher.encrypt_block(plaintext1)
    cipher2 = cipher.encrypt_block(plaintext2)
    
    print(f"\nOriginal ciphertext: {cipher1:032b}")
    print(f"Modified ciphertext: {cipher2:032b}")
    
    xor_result = cipher1 ^ cipher2
    differing = bin(xor_result).count('1')
    
    print(f"XOR result: {xor_result:032b}")
    print(f"Differing bits: {differing} out of 32 ({(differing/32)*100:.1f}%)")
    
    # Example 3: Avalanche with analysis function
    print("\n[Example 3] Detailed Avalanche Analysis")
    print("-" * 70)
    
    plaintext = 0xFFFFFFFF
    analysis = cipher.analyze_avalanche(plaintext)
    
    print(f"Original plaintext:  {analysis['original_plaintext']}")
    print(f"Modified plaintext:  {analysis['modified_plaintext']}")
    print(f"Original ciphertext: {analysis['original_ciphertext']}")
    print(f"Modified ciphertext: {analysis['modified_ciphertext']}")
    print(f"Differing bits: {analysis['differing_bits']} ({analysis['avalanche_percentage']:.1f}%)")
    print(f"\nAvalanche effect observed: {analysis['avalanche_percentage'] > 20}%")

if __name__ == "__main__":
    demonstrate_feistel()
