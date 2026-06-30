#!/usr/bin/env python3
"""
Linear Feedback Shift Register (LFSR) Implementation
Demonstrates stream cipher generation and cryptanalysis
"""

class LFSR:
    """
    Linear Feedback Shift Register
    
    Parameters:
    - state: Initial state (list of bits)
    - taps: Feedback taps (polynomial positions)
    """
    
    def __init__(self, state, taps):
        """
        Initialize LFSR
        
        Args:
            state: Initial state as list of integers (0 or 1)
            taps: Positions of feedback taps (counting from right, 0-indexed)
        """
        self.state = list(state)
        self.taps = taps
        self.sequence = []
        self.states_seen = {}
    
    def next_bit(self):
        """
        Generate next bit using XOR of tap positions
        """
        # XOR all tap positions
        feedback = 0
        for tap in self.taps:
            if tap < len(self.state):
                feedback ^= self.state[tap]
        
        # Shift and insert feedback
        output_bit = self.state[-1]
        self.state = [feedback] + self.state[:-1]
        
        # Record state
        state_tuple = tuple(self.state)
        if state_tuple not in self.states_seen:
            self.states_seen[state_tuple] = len(self.sequence)
        
        self.sequence.append(output_bit)
        return output_bit
    
    def generate(self, count):
        """
        Generate multiple bits
        """
        return [self.next_bit() for _ in range(count)]
    
    def get_sequence_str(self):
        """
        Get sequence as binary string
        """
        return ''.join(str(b) for b in self.sequence)
    
    def detect_period(self):
        """
        Detect period (when state repeats)
        
        Returns:
            Period length if found, None otherwise
        """
        state_tuple = tuple(self.state)
        
        # Check if we've seen this state before
        if state_tuple in self.states_seen:
            # Period is the difference in indices
            first_occurrence = self.states_seen[state_tuple]
            current_position = len(self.sequence)
            return current_position - first_occurrence
        
        return None
    
    def linear_complexity(self):
        """
        Approximate linear complexity (Berlekamp-Massey simplified)
        For a true LFSR, this would be the size of the register
        
        Returns:
            Estimated linear complexity
        """
        return len(self.state)
    
    def reset(self, new_state):
        """
        Reset LFSR with new state
        """
        self.state = list(new_state)
        self.sequence = []
        self.states_seen = {}

def demonstrate_lfsr():
    """
    Demonstrate LFSR generation and analysis
    """
    print("=" * 70)
    print("Linear Feedback Shift Register (LFSR) Demonstration")
    print("=" * 70)
    
    # Example 1: 4-bit LFSR with taps at positions 0 and 3
    print("\n[Example 1] 4-bit LFSR with taps at [0, 3]")
    print("-" * 70)
    
    state1 = [1, 0, 0, 1]
    taps1 = [0, 3]
    lfsr1 = LFSR(state1, taps1)
    
    print(f"Initial state: {state1}")
    print(f"Taps: {taps1}")
    
    # Generate sequence
    sequence = lfsr1.generate(20)
    print(f"Generated sequence: {lfsr1.get_sequence_str()}")
    print(f"Length: {len(sequence)}")
    
    # Example 2: Detect period
    print("\n[Example 2] Period Detection")
    print("-" * 70)
    
    state2 = [1, 0, 0, 0]
    taps2 = [0, 2]
    lfsr2 = LFSR(state2, taps2)
    
    print(f"Initial state: {state2}")
    print(f"Taps: {taps2}")
    
    # Generate many bits and look for repetition
    sequence = lfsr2.generate(100)
    period = lfsr2.detect_period()
    
    print(f"Generated {len(sequence)} bits")
    if period:
        print(f"Period detected: {period}")
        print(f"First {period} bits: {lfsr2.get_sequence_str()[:period]}")
    else:
        print("Period not found in generated sequence")
    
    # Example 3: Linear Complexity Analysis
    print("\n[Example 3] Linear Complexity")
    print("-" * 70)
    
    state3 = [1, 0, 1, 0, 1, 0]
    taps3 = [0, 1, 4, 5]
    lfsr3 = LFSR(state3, taps3)
    
    print(f"Initial state: {state3}")
    print(f"Taps: {taps3}")
    print(f"Register size: {len(state3)}")
    print(f"Linear complexity (register size): {lfsr3.linear_complexity()}")
    
    sequence = lfsr3.generate(30)
    print(f"Generated sequence: {lfsr3.get_sequence_str()}")
    
    # Example 4: Weak vs Strong LFSR
    print("\n[Example 4] Weak vs Strong LFSR")
    print("-" * 70)
    
    # Weak: Single tap feedback
    print("\nWeak LFSR (single tap):")
    weak_lfsr = LFSR([1, 0, 0, 0], [0])
    weak_seq = weak_lfsr.generate(30)
    print(f"Sequence: {weak_lfsr.get_sequence_str()}")
    print("Problem: Predictable pattern")
    
    # Strong: Multiple tap feedback
    print("\nStrong LFSR (multiple taps):")
    strong_lfsr = LFSR([1, 0, 1, 0, 1], [0, 1, 3, 4])
    strong_seq = strong_lfsr.generate(30)
    print(f"Sequence: {strong_lfsr.get_sequence_str()}")
    print("Better: More complex pattern")

if __name__ == "__main__":
    demonstrate_lfsr()
