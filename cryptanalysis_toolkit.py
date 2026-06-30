#!/usr/bin/env python3
"""
Block Cipher Cryptanalysis Toolkit
Demonstrates algebraic, differential, and linear cryptanalysis concepts
"""

import struct
from collections import Counter
import math

class CryptanalysisToolkit:
    """
    Tools for analyzing block cipher security
    """
    
    @staticmethod
    def xor_analysis(plaintext, ciphertext):
        """
        Analyze XOR-based cipher through algebraic approach
        
        Args:
            plaintext: Original plaintext (bytes)
            ciphertext: Encrypted ciphertext (bytes)
        
        Returns:
            Recovered key (bytes)
        """
        if len(plaintext) != len(ciphertext):
            return None
        
        recovered_key = bytes(p ^ c for p, c in zip(plaintext, ciphertext))
        return recovered_key
    
    @staticmethod
    def differential_analysis(plaintext1, plaintext2, ciphertext1, ciphertext2):
        """
        Differential cryptanalysis: analyze how plaintext differences affect ciphertext
        
        Args:
            plaintext1: First plaintext
            plaintext2: Second plaintext (slightly different)
            ciphertext1: Ciphertext of first plaintext
            ciphertext2: Ciphertext of second plaintext
        
        Returns:
            Differential analysis results
        """
        # Calculate differences
        plaintext_diff = bytes(p1 ^ p2 for p1, p2 in zip(plaintext1, plaintext2))
        ciphertext_diff = bytes(c1 ^ c2 for c1, c2 in zip(ciphertext1, ciphertext2))
        
        # Count bit differences
        plaintext_bit_diffs = sum(bin(b).count('1') for b in plaintext_diff)
        ciphertext_bit_diffs = sum(bin(b).count('1') for b in ciphertext_diff)
        
        return {
            'plaintext_difference': plaintext_diff.hex(),
            'ciphertext_difference': ciphertext_diff.hex(),
            'plaintext_bit_differences': plaintext_bit_diffs,
            'ciphertext_bit_differences': ciphertext_bit_diffs,
            'diffusion_ratio': ciphertext_bit_diffs / max(plaintext_bit_diffs, 1)
        }
    
    @staticmethod
    def frequency_analysis(ciphertext):
        """
        Frequency analysis for statistical cryptanalysis
        
        Args:
            ciphertext: Encrypted data (bytes)
        
        Returns:
            Frequency distribution
        """
        frequency = Counter(ciphertext)
        total = len(ciphertext)
        
        # Calculate entropy
        entropy = 0
        for count in frequency.values():
            probability = count / total
            entropy -= probability * math.log2(probability + 1e-10)
        
        # Sort by frequency
        sorted_freq = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
        
        return {
            'total_bytes': total,
            'unique_values': len(frequency),
            'frequency_distribution': dict(sorted_freq[:10]),
            'entropy': entropy,
            'max_entropy': 8  # 8 bits per byte
        }
    
    @staticmethod
    def chi_square_test(ciphertext):
        """
        Chi-square test for randomness evaluation
        
        Args:
            ciphertext: Encrypted data (bytes)
        
        Returns:
            Chi-square test results
        """
        frequency = Counter(ciphertext)
        total = len(ciphertext)
        
        # Expected frequency for random data
        expected_freq = total / 256
        
        # Calculate chi-square statistic
        chi_square = 0
        for i in range(256):
            observed = frequency.get(i, 0)
            chi_square += ((observed - expected_freq) ** 2) / expected_freq
        
        return {
            'chi_square_statistic': chi_square,
            'degrees_of_freedom': 255,
            'is_random': chi_square < 300  # Rough threshold
        }
    
    @staticmethod
    def linear_bias_test(plaintexts, ciphertexts, num_samples=1000):
        """
        Detect linear bias in cipher (linear cryptanalysis concept)
        
        Args:
            plaintexts: List of plaintext values
            ciphertexts: List of ciphertext values
            num_samples: Number of samples to analyze
        
        Returns:
            Linear bias detection results
        """
        if len(plaintexts) != len(ciphertexts):
            return None
        
        sample_size = min(num_samples, len(plaintexts))
        
        # Test for linear relationships
        bias_count = 0
        expected_count = sample_size / 2
        
        for i in range(sample_size):
            p = plaintexts[i] if isinstance(plaintexts[i], int) else int.from_bytes(plaintexts[i], 'big')
            c = ciphertexts[i] if isinstance(ciphertexts[i], int) else int.from_bytes(ciphertexts[i], 'big')
            
            # Check for XOR relationship
            xor_result = p ^ c
            if bin(xor_result).count('1') % 2 == 0:  # Even number of 1s
                bias_count += 1
        
        bias = abs(bias_count - expected_count) / expected_count
        
        return {
            'samples_analyzed': sample_size,
            'bias_count': bias_count,
            'expected_count': expected_count,
            'bias_percentage': (bias_count / sample_size) * 100,
            'linear_bias': bias,
            'has_significant_bias': bias > 0.1
        }
    
    @staticmethod
    def avalanche_analysis(encrypt_function, plaintext1, plaintext2):
        """
        Analyze avalanche effect
        
        Args:
            encrypt_function: Function that encrypts plaintext
            plaintext1: Original plaintext
            plaintext2: Slightly modified plaintext
        
        Returns:
            Avalanche analysis
        """
        ciphertext1 = encrypt_function(plaintext1)
        ciphertext2 = encrypt_function(plaintext2)
        
        # Convert to bytes if necessary
        if isinstance(ciphertext1, int):
            ciphertext1 = ciphertext1.to_bytes((ciphertext1.bit_length() + 7) // 8, 'big')
        if isinstance(ciphertext2, int):
            ciphertext2 = ciphertext2.to_bytes((ciphertext2.bit_length() + 7) // 8, 'big')
        
        # Calculate bit differences
        differing_bits = 0
        total_bits = len(ciphertext1) * 8
        
        for b1, b2 in zip(ciphertext1, ciphertext2):
            differing_bits += bin(b1 ^ b2).count('1')
        
        avalanche_percentage = (differing_bits / total_bits) * 100
        
        return {
            'ciphertext1': ciphertext1.hex(),
            'ciphertext2': ciphertext2.hex(),
            'differing_bits': differing_bits,
            'total_bits': total_bits,
            'avalanche_percentage': avalanche_percentage,
            'strong_avalanche': 40 < avalanche_percentage < 60  # Ideal is ~50%
        }
    
    @staticmethod
    def weak_key_detection(key, encrypt_function, num_tests=1000):
        """
        Detect potentially weak keys
        
        Args:
            key: Encryption key
            encrypt_function: Encryption function
            num_tests: Number of tests
        
        Returns:
            Weak key analysis
        """
        import random
        random.seed(42)  # For reproducibility
        
        entropy_values = []
        
        for _ in range(num_tests):
            plaintext = bytes(random.randint(0, 255) for _ in range(16))
            ciphertext = encrypt_function(plaintext)
            
            # Calculate entropy of this ciphertext
            if isinstance(ciphertext, int):
                ciphertext = ciphertext.to_bytes(16, 'big')
            
            freq = Counter(ciphertext)
            entropy = 0
            for count in freq.values():
                p = count / len(ciphertext)
                entropy -= p * math.log2(p + 1e-10)
            
            entropy_values.append(entropy)
        
        avg_entropy = sum(entropy_values) / len(entropy_values)
        
        return {
            'average_entropy': avg_entropy,
            'max_entropy': 8,
            'entropy_ratio': avg_entropy / 8,
            'likely_weak': avg_entropy < 6
        }

def demonstrate_cryptanalysis():
    """
    Demonstrate cryptanalysis techniques
    """
    print("=" * 70)
    print("Block Cipher Cryptanalysis Toolkit")
    print("=" * 70)
    
    toolkit = CryptanalysisToolkit()
    
    # Example 1: Algebraic Attack (XOR Analysis)
    print("\n[Example 1] Algebraic Attack - XOR Analysis")
    print("-" * 70)
    
    plaintext = b"HELLO WORLD!!!!"
    key = b"SECRETKEYVALUE!"
    ciphertext = bytes(p ^ k for p, k in zip(plaintext, key))
    
    recovered_key = toolkit.xor_analysis(plaintext, ciphertext)
    
    print(f"Plaintext:  {plaintext}")
    print(f"Ciphertext: {ciphertext.hex()}")
    print(f"Original Key: {key}")
    print(f"Recovered Key: {recovered_key}")
    print(f"Key Match: {key == recovered_key}")
    
    # Example 2: Differential Cryptanalysis
    print("\n[Example 2] Differential Cryptanalysis")
    print("-" * 70)
    
    plaintext1 = b"HELLO WORLD!!!!"
    plaintext2 = b"HELLO WORLD!!!"  # Change last bit
    ciphertext1 = bytes((p ^ 0xAB) for p in plaintext1)
    ciphertext2 = bytes((p ^ 0xAB) for p in plaintext2)
    
    diff_analysis = toolkit.differential_analysis(
        plaintext1, plaintext2, ciphertext1, ciphertext2
    )
    
    print(f"Plaintext 1: {plaintext1}")
    print(f"Plaintext 2: {plaintext2}")
    print(f"Plaintext bit differences: {diff_analysis['plaintext_bit_differences']}")
    print(f"Ciphertext bit differences: {diff_analysis['ciphertext_bit_differences']}")
    print(f"Diffusion Ratio: {diff_analysis['diffusion_ratio']:.2f}")
    
    # Example 3: Frequency Analysis
    print("\n[Example 3] Frequency Analysis")
    print("-" * 70)
    
    import random
    random.seed(42)
    ciphertext = bytes(random.randint(0, 255) for _ in range(1000))
    
    freq_analysis = toolkit.frequency_analysis(ciphertext)
    
    print(f"Total bytes: {freq_analysis['total_bytes']}")
    print(f"Unique values: {freq_analysis['unique_values']}")
    print(f"Entropy: {freq_analysis['entropy']:.2f} bits")
    print(f"Max Entropy: {freq_analysis['max_entropy']} bits")
    print(f"Top 5 frequencies: {list(freq_analysis['frequency_distribution'].items())[:5]}")
    
    # Example 4: Chi-Square Test
    print("\n[Example 4] Chi-Square Randomness Test")
    print("-" * 70)
    
    chi_result = toolkit.chi_square_test(ciphertext)
    
    print(f"Chi-Square Statistic: {chi_result['chi_square_statistic']:.2f}")
    print(f"Appears Random: {chi_result['is_random']}")
    
    # Example 5: Linear Bias Test
    print("\n[Example 5] Linear Bias Detection")
    print("-" * 70)
    
    plaintexts = [bytes(random.randint(0, 255) for _ in range(8)) for _ in range(100)]
    ciphertexts = [bytes(p ^ 0x42 for p in pt) for pt in plaintexts]
    
    bias_result = toolkit.linear_bias_test(plaintexts, ciphertexts, num_samples=100)
    
    print(f"Samples analyzed: {bias_result['samples_analyzed']}")
    print(f"Bias percentage: {bias_result['bias_percentage']:.1f}%")
    print(f"Has significant linear bias: {bias_result['has_significant_bias']}")

if __name__ == "__main__":
    demonstrate_cryptanalysis()
