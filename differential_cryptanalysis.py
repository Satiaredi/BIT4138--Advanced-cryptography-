#!/usr/bin/env python3
"""
Differential Cryptanalysis Simulator
Demonstrates differential attack concepts on simple ciphers
"""

class DifferentialAnalyzer:
    """
    Tool for differential cryptanalysis studies
    """
    
    @staticmethod
    def simple_cipher(plaintext, key):
        """
        Simple cipher for demonstration (vulnerable to differential analysis)
        
        Args:
            plaintext: Input bytes
            key: Key bytes
        
        Returns:
            Ciphertext bytes
        """
        # Vulnerable: simple XOR without proper diffusion
        return bytes(p ^ k for p, k in zip(plaintext, key))
    
    @staticmethod
    def better_cipher(plaintext, key, rounds=4):
        """
        Better cipher with some diffusion
        
        Args:
            plaintext: Input bytes
            key: Key bytes
            rounds: Number of rounds
        
        Returns:
            Ciphertext bytes
        """
        block = plaintext
        
        for round_num in range(rounds):
            # XOR with key
            block = bytes(b ^ k for b, k in zip(block, key))
            
            # Simple diffusion: rotate bytes
            block = block[1:] + block[:1]
            
            # Substitution: add round number
            block = bytes((b + round_num) % 256 for b in block)
        
        return block
    
    @staticmethod
    def analyze_differential_pattern(cipher_func, key, plaintext_pairs, num_pairs=100):
        """
        Analyze differential patterns in cipher
        
        Args:
            cipher_func: Encryption function
            key: Encryption key
            plaintext_pairs: Generator/list of plaintext pairs
            num_pairs: Number of pairs to analyze
        
        Returns:
            Differential pattern analysis
        """
        import collections
        
        differential_ratios = collections.defaultdict(int)
        
        for i in range(num_pairs):
            p1, p2 = plaintext_pairs[i]
            
            c1 = cipher_func(p1, key)
            c2 = cipher_func(p2, key)
            
            # Calculate differences
            plaintext_diff = bytes(a ^ b for a, b in zip(p1, p2))
            ciphertext_diff = bytes(a ^ b for a, b in zip(c1, c2))
            
            # Count bit differences
            p_bits = sum(bin(b).count('1') for b in plaintext_diff)
            c_bits = sum(bin(b).count('1') for b in ciphertext_diff)
            
            # Create differential ratio
            if p_bits > 0:
                ratio = c_bits / p_bits
                differential_ratios[ratio] += 1
        
        return differential_ratios
    
    @staticmethod
    def find_weak_patterns(cipher_func, key, plaintext_pairs, num_pairs=1000):
        """
        Find weak differential patterns that might leak information
        
        Args:
            cipher_func: Encryption function
            key: Encryption key
            plaintext_pairs: List of plaintext pairs
            num_pairs: Number of pairs to test
        
        Returns:
            List of weak patterns found
        """
        weak_patterns = []
        pattern_count = {}
        
        for i in range(min(num_pairs, len(plaintext_pairs))):
            p1, p2 = plaintext_pairs[i]
            
            c1 = cipher_func(p1, key)
            c2 = cipher_func(p2, key)
            
            # Check for patterns
            ciphertext_diff = bytes(a ^ b for a, b in zip(c1, c2))
            pattern = ciphertext_diff.hex()
            
            pattern_count[pattern] = pattern_count.get(pattern, 0) + 1
        
        # Find repeating patterns (weak)
        for pattern, count in pattern_count.items():
            if count > num_pairs * 0.01:  # Pattern appears >1% of time
                weak_patterns.append((pattern, count))
        
        return sorted(weak_patterns, key=lambda x: x[1], reverse=True)

def demonstrate_differential_analysis():
    """
    Demonstrate differential cryptanalysis
    """
    print("=" * 70)
    print("Differential Cryptanalysis Demonstration")
    print("=" * 70)
    
    analyzer = DifferentialAnalyzer()
    import random
    random.seed(42)
    
    key = b"SECRETKEY123456"
    
    # Generate plaintext pairs with controlled differences
    plaintext_pairs = []
    for _ in range(100):
        p1 = bytes(random.randint(0, 255) for _ in range(16))
        p2 = bytearray(p1)
        p2[0] ^= 0x01  # Flip one bit in first byte
        plaintext_pairs.append((p1, bytes(p2)))
    
    # Example 1: Vulnerable Cipher
    print("\n[Example 1] Differential Analysis on Vulnerable Cipher")
    print("-" * 70)
    
    print("Cipher: Simple XOR (vulnerable)")
    print("\nSample differential pairs:")
    
    for i in range(3):
        p1, p2 = plaintext_pairs[i]
        c1 = analyzer.simple_cipher(p1, key)
        c2 = analyzer.simple_cipher(p2, key)
        
        p_diff = sum(bin(b).count('1') for a, b in zip(p1, p2) for b in [a ^ b])
        c_diff = sum(bin(b).count('1') for a, b in zip(c1, c2) for b in [a ^ b])
        
        print(f"  Pair {i+1}: P-diff bits: {p_diff:2d}, C-diff bits: {c_diff:2d}")
    
    print("\nObservation: Differences remain constant (predictable!)")
    
    # Example 2: Better Cipher
    print("\n[Example 2] Differential Analysis on Improved Cipher")
    print("-" * 70)
    
    print("Cipher: XOR + Diffusion + Substitution (4 rounds)")
    print("\nSample differential pairs:")
    
    for i in range(3):
        p1, p2 = plaintext_pairs[i]
        c1 = analyzer.better_cipher(p1, key, rounds=4)
        c2 = analyzer.better_cipher(p2, key, rounds=4)
        
        p_diff = sum(bin(b).count('1') for a, b in zip(p1, p2) for b in [a ^ b])
        c_diff = sum(bin(b).count('1') for a, b in zip(c1, c2) for b in [a ^ b])
        
        print(f"  Pair {i+1}: P-diff bits: {p_diff:2d}, C-diff bits: {c_diff:2d}")
    
    print("\nObservation: Differences vary widely (good diffusion!)")
    
    # Example 3: Weak Pattern Detection
    print("\n[Example 3] Weak Pattern Detection")
    print("-" * 70)
    
    weak_patterns = analyzer.find_weak_patterns(
        analyzer.simple_cipher, key, plaintext_pairs, num_pairs=100
    )
    
    print(f"Found {len(weak_patterns)} repeating patterns in vulnerable cipher:")
    for i, (pattern, count) in enumerate(weak_patterns[:5]):
        print(f"  Pattern {i+1}: {pattern[:16]}... (appears {count} times)")
    
    print("\nThese repeating patterns can leak information to attackers!")

if __name__ == "__main__":
    demonstrate_differential_analysis()
