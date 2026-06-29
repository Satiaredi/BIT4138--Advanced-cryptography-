#!/usr/bin/env python3
"""
S-Box (Substitution Box) Analysis
Demonstrates non-linearity and cryptographic properties
"""

import math

class SBoxAnalyzer:
    """
    Analyzer for S-Box properties and non-linearity
    """
    
    @staticmethod
    def analyze_sbox(sbox, name="S-Box"):
        """
        Analyze S-Box properties
        
        Args:
            sbox: List or dictionary of S-Box values
            name: Name of S-Box
        
        Returns:
            Dictionary with analysis results
        """
        if isinstance(sbox, dict):
            sbox_list = [sbox[i] for i in sorted(sbox.keys())]
        else:
            sbox_list = list(sbox)
        
        results = {
            'name': name,
            'size': len(sbox_list),
            'min_value': min(sbox_list),
            'max_value': max(sbox_list),
            'mean': sum(sbox_list) / len(sbox_list),
            'unique_outputs': len(set(sbox_list)),
            'has_fixed_points': any(i == sbox_list[i] for i in range(len(sbox_list))),
        }
        
        # Check for linearity
        results['linearity_score'] = SBoxAnalyzer._check_linearity(sbox_list)
        
        return results
    
    @staticmethod
    def _check_linearity(sbox):
        """
        Check linearity of S-Box (higher is better/more non-linear)
        
        Returns score from 0 to 1
        """
        if len(sbox) < 2:
            return 0
        
        n = len(sbox)
        
        # Check if output follows linear pattern
        linear_count = 0
        
        for i in range(n):
            for j in range(i + 1, min(i + 5, n)):
                expected_diff = j - i
                actual_diff = abs(sbox[j] - sbox[i])
                
                # Penalize consistent differences
                if expected_diff == actual_diff:
                    linear_count += 1
        
        # Invert so higher score = more non-linear
        linearity = 1 - (linear_count / (n * 4))
        return max(0, min(1, linearity))
    
    @staticmethod
    def compare_sboxes(sboxes_dict):
        """
        Compare multiple S-Boxes
        
        Args:
            sboxes_dict: Dictionary of {name: sbox}
        
        Returns:
            Comparison results
        """
        results = {}
        
        for name, sbox in sboxes_dict.items():
            results[name] = SBoxAnalyzer.analyze_sbox(sbox, name)
        
        return results
    
    @staticmethod
    def visualize_sbox_distribution(sbox):
        """
        Create simple ASCII visualization of S-Box distribution
        
        Args:
            sbox: S-Box values
        
        Returns:
            ASCII visualization
        """
        if isinstance(sbox, dict):
            sbox_list = [sbox[i] for i in sorted(sbox.keys())]
        else:
            sbox_list = list(sbox)
        
        output = "S-Box Output Distribution:\n"
        output += "=" * 50 + "\n"
        
        # Create histogram
        max_val = max(sbox_list)
        min_val = min(sbox_list)
        
        for val in range(min_val, min(min_val + 16, max_val + 1)):
            count = sbox_list.count(val)
            bar = "█" * (count * 2)
            output += f"{val:3d}: {bar}\n"
        
        return output
    
    @staticmethod
    def check_avalanche_independence(sbox):
        """
        Check Strict Avalanche Criterion (SAC)
        For each input bit, changing it should flip ~50% of output bits
        
        Args:
            sbox: S-Box (for small sizes like 4-bit input)
        
        Returns:
            SAC score
        """
        if isinstance(sbox, dict):
            sbox_list = [sbox[i] for i in sorted(sbox.keys())]
        else:
            sbox_list = list(sbox)
        
        if len(sbox_list) > 256:  # Only for small S-Boxes
            return None
        
        n_bits_input = (len(sbox_list) - 1).bit_length()
        sac_scores = []
        
        for bit_pos in range(n_bits_input):
            flip_count = 0
            total_pairs = 0
            
            for i in range(len(sbox_list)):
                flipped_i = i ^ (1 << bit_pos)
                
                if flipped_i < len(sbox_list):
                    output_diff = sbox_list[i] ^ sbox_list[flipped_i]
                    bit_flips = bin(output_diff).count('1')
                    flip_count += bit_flips
                    total_pairs += 1
            
            if total_pairs > 0:
                avg_flips = flip_count / total_pairs
                sac_scores.append(avg_flips)
        
        return {
            'bit_flip_scores': sac_scores,
            'average': sum(sac_scores) / len(sac_scores) if sac_scores else 0,
            'ideal': (len(sbox_list[0].bit_length())) / 2  # Ideal is 50% flips
        }

def demonstrate_sbox_analysis():
    """
    Demonstrate S-Box analysis
    """
    print("=" * 70)
    print("S-Box Analysis and Non-Linearity Evaluation")
    print("=" * 70)
    
    # Example 1: Simple S-Box analysis
    print("\n[Example 1] Simple S-Box Analysis")
    print("-" * 70)
    
    simple_sbox = [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7]
    analysis = SBoxAnalyzer.analyze_sbox(simple_sbox, "Example S-Box")
    
    print(f"S-Box Name: {analysis['name']}")
    print(f"Size: {analysis['size']}")
    print(f"Min Output: {analysis['min_value']}")
    print(f"Max Output: {analysis['max_value']}")
    print(f"Mean Output: {analysis['mean']:.2f}")
    print(f"Unique Outputs: {analysis['unique_outputs']}")
    print(f"Fixed Points: {analysis['has_fixed_points']}")
    print(f"Non-Linearity Score: {analysis['linearity_score']:.3f}")
    
    # Example 2: Compare different S-Boxes
    print("\n[Example 2] Compare S-Boxes")
    print("-" * 70)
    
    linear_sbox = list(range(16))  # Linear: output = input
    nonlinear_sbox = [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7]
    random_sbox = [7, 2, 15, 11, 9, 0, 5, 13, 3, 14, 8, 4, 12, 6, 1, 10]
    
    sboxes = {
        'Linear': linear_sbox,
        'Non-Linear': nonlinear_sbox,
        'Random': random_sbox
    }
    
    comparisons = SBoxAnalyzer.compare_sboxes(sboxes)
    
    print(f"{'S-Box':<15} {'Non-Linearity':<15} {'Unique Outputs':<15}")
    print("-" * 45)
    
    for name, result in comparisons.items():
        print(f"{name:<15} {result['linearity_score']:<15.3f} {result['unique_outputs']:<15}")
    
    # Example 3: Distribution visualization
    print("\n[Example 3] S-Box Output Distribution")
    print("-" * 70)
    
    print(SBoxAnalyzer.visualize_sbox_distribution(nonlinear_sbox))
    
    # Example 4: Avalanche criterion check
    print("\n[Example 4] Strict Avalanche Criterion (SAC) Check")
    print("-" * 70)
    
    sac_result = SBoxAnalyzer.check_avalanche_independence(nonlinear_sbox)
    
    if sac_result:
        print(f"Bit-Flip Scores per Input Bit:")
        for i, score in enumerate(sac_result['bit_flip_scores']):
            print(f"  Bit {i}: {score:.2f} flips (ideal ~50% = 2.0)")
        
        print(f"\nAverage: {sac_result['average']:.2f}")
        print(f"Ideal: {sac_result['ideal']:.2f}")
    
    # Example 5: AES S-Box analysis
    print("\n[Example 5] AES S-Box Analysis (partial)")
    print("-" * 70)
    
    aes_sbox = [
        0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5,
        0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
    ]
    
    aes_analysis = SBoxAnalyzer.analyze_sbox(aes_sbox, "AES S-Box (partial)")
    print(f"S-Box Name: {aes_analysis['name']}")
    print(f"Non-Linearity Score: {aes_analysis['linearity_score']:.3f}")
    print(f"Unique Outputs: {aes_analysis['unique_outputs']} (all unique = good)")
    print(f"\nNote: Full AES S-Box has 256 entries with excellent cryptographic properties")

if __name__ == "__main__":
    demonstrate_sbox_analysis()
