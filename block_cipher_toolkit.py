#!/usr/bin/env python3
"""
Block Cipher Toolkit
Demonstrates permutation, substitution, and block operations
"""

class BlockCipherToolkit:
    """
    Tools for block cipher operations
    """
    
    @staticmethod
    def permutation(data: str, permutation_table: list) -> str:
        """
        Apply permutation to data
        
        Args:
            data: Input string or bits
            permutation_table: Indices for permutation
        
        Returns:
            Permuted data
        """
        return ''.join(data[i] for i in permutation_table)
    
    @staticmethod
    def substitution(value: int, sbox: list) -> int:
        """
        Apply S-box substitution
        
        Args:
            value: Input value (0-15 for 4-bit)
            sbox: Substitution box (16 entries)
        
        Returns:
            Substituted value
        """
        if 0 <= value < len(sbox):
            return sbox[value]
        return value
    
    @staticmethod
    def split_into_blocks(data: str, block_size: int = 8) -> list:
        """
        Split data into blocks
        
        Args:
            data: Input string
            block_size: Size of each block
        
        Returns:
            List of blocks
        """
        blocks = []
        for i in range(0, len(data), block_size):
            blocks.append(data[i:i+block_size])
        return blocks
    
    @staticmethod
    def add_padding(data: str, block_size: int = 8) -> str:
        """
        Add PKCS#7 padding
        
        Args:
            data: Input data
            block_size: Block size
        
        Returns:
            Padded data
        """
        padding_length = block_size - (len(data) % block_size)
        if padding_length == 0:
            padding_length = block_size
        
        padding = chr(padding_length) * padding_length
        return data + padding
    
    @staticmethod
    def remove_padding(data: str) -> str:
        """
        Remove PKCS#7 padding
        
        Args:
            data: Padded data
        
        Returns:
            Unpadded data
        """
        if not data:
            return data
        
        padding_length = ord(data[-1])
        return data[:-padding_length]
    
    @staticmethod
    def confusion_demo(plaintext_bit: str, key_bit: str) -> str:
        """
        Demonstrate confusion principle
        Using substitution to hide relationship
        
        Args:
            plaintext_bit: Plaintext bit
            key_bit: Key bit
        
        Returns:
            Confused output
        """
        # Combine plaintext and key
        combined = str(int(plaintext_bit) ^ int(key_bit))
        return combined
    
    @staticmethod
    def diffusion_demo(plaintext: str, rounds: int = 3) -> str:
        """
        Demonstrate diffusion principle
        Change in one bit spreads to others
        
        Args:
            plaintext: Binary string
            rounds: Number of diffusion rounds
        
        Returns:
            Diffused plaintext
        """
        data = list(plaintext)
        
        for round_num in range(rounds):
            # Shift and XOR for diffusion
            new_data = data.copy()
            for i in range(len(data)):
                # Mix with neighbors
                left = data[(i - 1) % len(data)]
                right = data[(i + 1) % len(data)]
                current = data[i]
                
                new_data[i] = str(int(current) ^ int(left) ^ int(right))
            
            data = new_data
        
        return ''.join(data)

def demonstrate_toolkit():
    """
    Demonstrate block cipher toolkit
    """
    toolkit = BlockCipherToolkit()
    
    print("=" * 70)
    print("Block Cipher Toolkit Demonstration")
    print("=" * 70)
    
    # Example 1: Permutation
    print("\n[Example 1] Permutation")
    print("-" * 70)
    
    plaintext = "HELLO!!!"
    perm_table = [7, 5, 3, 1, 6, 4, 2, 0]  # Reverse positions
    
    permuted = toolkit.permutation(plaintext, perm_table)
    print(f"Original:    {plaintext}")
    print(f"Perm table:  {perm_table}")
    print(f"Permuted:    {permuted}")
    
    # Example 2: Substitution (S-box)
    print("\n[Example 2] Substitution (S-box)")
    print("-" * 70)
    
    # DES-like S-box
    sbox = [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7]
    
    print("S-box: ", sbox)
    for i in range(16):
        substituted = toolkit.substitution(i, sbox)
        print(f"  {i:2d} -> {substituted:2d}", end="  ")
        if (i + 1) % 4 == 0:
            print()
    
    # Example 3: Block division and padding
    print("\n[Example 3] Block Division and Padding")
    print("-" * 70)
    
    plaintext = "CRYPTOGRAPHY"
    padded = toolkit.add_padding(plaintext, block_size=8)
    
    print(f"Original text: {plaintext} (length: {len(plaintext)})")
    print(f"Padded text:   {padded} (length: {len(padded)})")
    
    blocks = toolkit.split_into_blocks(padded, block_size=8)
    for i, block in enumerate(blocks):
        print(f"Block {i}: {block}")
    
    # Example 4: Confusion
    print("\n[Example 4] Confusion Principle")
    print("-" * 70)
    
    print("Plaintext bit | Key bit | Confused output")
    print("-" * 40)
    for p in ['0', '1']:
        for k in ['0', '1']:
            confused = toolkit.confusion_demo(p, k)
            print(f"      {p}       |    {k}    |       {confused}")
    
    # Example 5: Diffusion
    print("\n[Example 5] Diffusion Principle")
    print("-" * 70)
    
    plaintext = "01000000"
    print(f"Original:  {plaintext}")
    
    for round_num in range(1, 4):
        diffused = toolkit.diffusion_demo(plaintext, rounds=round_num)
        print(f"Round {round_num}:  {diffused}")
    
    print("\nObservation: Single bit change spreads across more positions")

if __name__ == "__main__":
    demonstrate_toolkit()
