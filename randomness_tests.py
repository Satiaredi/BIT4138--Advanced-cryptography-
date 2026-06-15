#!/usr/bin/env python3
"""
Randomness Testing Suite
Implements various statistical tests for pseudorandom sequences

- Frequency Test
- Runs Test
- Mean Test
- Chi-Square Test
"""

import math
from collections import Counter

class RandomnessTests:
    """
    Statistical tests for randomness evaluation
    """
    
    @staticmethod
    def frequency_test(binary_sequence):
        """
        Frequency Test: Tests if 0s and 1s occur with equal probability
        
        Args:
            binary_sequence: String or list of binary digits
        
        Returns:
            Dictionary with test results
        """
        # Convert to string if list
        if isinstance(binary_sequence, list):
            seq = ''.join(str(b) for b in binary_sequence)
        else:
            seq = str(binary_sequence)
        
        n = len(seq)
        zeros = seq.count('0')
        ones = seq.count('1')
        
        # Expected: n/2 each
        expected = n / 2
        
        # Chi-square statistic
        chi_square = ((zeros - expected) ** 2 / expected) + ((ones - expected) ** 2 / expected)
        
        return {
            'test_name': 'Frequency Test',
            'total_bits': n,
            'zeros': zeros,
            'ones': ones,
            'zero_proportion': zeros / n,
            'one_proportion': ones / n,
            'chi_square': chi_square,
            'expected_zeros': expected,
            'expected_ones': expected
        }
    
    @staticmethod
    def runs_test(binary_sequence):
        """
        Runs Test: Tests for clustering of bits
        A run is a maximal sequence of identical consecutive bits
        
        Args:
            binary_sequence: String or list of binary digits
        
        Returns:
            Dictionary with test results
        """
        if isinstance(binary_sequence, list):
            seq = ''.join(str(b) for b in binary_sequence)
        else:
            seq = str(binary_sequence)
        
        n = len(seq)
        
        # Count runs
        runs = 1
        for i in range(1, n):
            if seq[i] != seq[i-1]:
                runs += 1
        
        # Count 0s and 1s
        zeros = seq.count('0')
        ones = seq.count('1')
        
        # Expected number of runs
        expected_runs = (2 * zeros * ones) / (zeros + ones) + 1
        
        # Variance
        variance = (2 * zeros * ones * (2 * zeros * ones - zeros - ones)) / \
                   ((zeros + ones) ** 2 * (zeros + ones - 1))
        
        # Z-score
        z_score = (runs - expected_runs) / math.sqrt(variance) if variance > 0 else 0
        
        return {
            'test_name': 'Runs Test',
            'total_bits': n,
            'runs': runs,
            'expected_runs': expected_runs,
            'variance': variance,
            'z_score': z_score,
            'zeros': zeros,
            'ones': ones
        }
    
    @staticmethod
    def mean_test(sequence):
        """
        Mean Test: Tests if mean is within expected range
        
        Args:
            sequence: List or array of numbers
        
        Returns:
            Dictionary with test results
        """
        if isinstance(sequence, str):
            sequence = [int(c) for c in sequence]
        
        n = len(sequence)
        mean = sum(sequence) / n
        
        # For binary sequence, expected mean is 0.5
        expected_mean = 0.5 if all(x in [0, 1] for x in sequence) else sum(sequence) / n
        
        # Standard deviation
        variance = sum((x - mean) ** 2 for x in sequence) / n
        std_dev = math.sqrt(variance)
        
        # Confidence interval (95%)
        margin = 1.96 * (std_dev / math.sqrt(n))
        
        return {
            'test_name': 'Mean Test',
            'sample_size': n,
            'mean': mean,
            'expected_mean': expected_mean,
            'std_dev': std_dev,
            'variance': variance,
            'margin_of_error': margin,
            'ci_lower': mean - margin,
            'ci_upper': mean + margin
        }
    
    @staticmethod
    def chi_square_test(binary_sequence):
        """
        Chi-Square Test: Goodness of fit test
        
        Args:
            binary_sequence: String or list of binary digits
        
        Returns:
            Dictionary with test results
        """
        if isinstance(binary_sequence, list):
            seq = ''.join(str(b) for b in binary_sequence)
        else:
            seq = str(binary_sequence)
        
        n = len(seq)
        
        # Count occurrences
        counter = Counter(seq)
        
        # Expected frequency for each digit
        expected = n / len(counter)
        
        # Calculate chi-square
        chi_square = sum((counter[digit] - expected) ** 2 / expected 
                        for digit in counter)
        
        # Degrees of freedom
        df = len(counter) - 1
        
        return {
            'test_name': 'Chi-Square Test',
            'total_bits': n,
            'unique_symbols': len(counter),
            'frequencies': dict(counter),
            'expected_frequency': expected,
            'chi_square': chi_square,
            'degrees_of_freedom': df
        }

def print_test_results(results):
    """Pretty print test results"""
    print(f"\n{'='*60}")
    print(f"Test: {results['test_name']}")
    print(f"{'='*60}")
    for key, value in results.items():
        if key != 'test_name':
            if isinstance(value, float):
                print(f"{key:.<40} {value:.6f}")
            else:
                print(f"{key:.<40} {value}")

if __name__ == "__main__":
    # Example sequences
    print("\n" + "*" * 60)
    print("RANDOMNESS TESTING SUITE")
    print("*" * 60)
    
    # Good random sequence
    good_sequence = "0110101010011010101001110110101"
    
    # Poor sequence (too many zeros)
    poor_sequence = "0000000111111100000001111111000"
    
    print("\n[Testing GOOD sequence]")
    print(f"Sequence: {good_sequence}")
    
    tests = [
        RandomnessTests.frequency_test(good_sequence),
        RandomnessTests.runs_test(good_sequence),
        RandomnessTests.mean_test(good_sequence),
        RandomnessTests.chi_square_test(good_sequence)
    ]
    
    for result in tests:
        print_test_results(result)
    
    print("\n" + "-" * 60)
    print("\n[Testing POOR sequence]")
    print(f"Sequence: {poor_sequence}")
    
    tests = [
        RandomnessTests.frequency_test(poor_sequence),
        RandomnessTests.runs_test(poor_sequence),
        RandomnessTests.mean_test(poor_sequence),
        RandomnessTests.chi_square_test(poor_sequence)
    ]
    
    for result in tests:
        print_test_results(result)
    
    print("\n" + "*" * 60)
    print("Note: Good sequence should have:")
    print("  - ~50% 0s and ~50% 1s (Frequency)")
    print("  - Runs close to expected value (Runs)")
    print("  - Mean close to 0.5 (Mean)")
    print("  - Chi-square statistic not too large")
    print("*" * 60)
