#!/usr/bin/env python3
"""
Linear Congruential Generator (LCG)
A simple pseudorandom number generator

Formula: X_{n+1} = (a*X_n + c) mod m
"""

class LCG:
    """
    Linear Congruential Generator
    
    Parameters:
    - a: Multiplier
    - c: Increment
    - m: Modulus
    - seed: Initial value
    """
    
    def __init__(self, seed, a=1103515245, c=12345, m=2**31):
        self.seed = seed
        self.a = a
        self.c = c
        self.m = m
        self.current = seed
        self.sequence = []
    
    def next(self):
        """Generate next pseudorandom number"""
        self.current = (self.a * self.current + self.c) % self.m
        self.sequence.append(self.current)
        return self.current
    
    def generate(self, count):
        """Generate multiple values"""
        return [self.next() for _ in range(count)]
    
    def normalize(self, value):
        """Normalize to range [0, 1)"""
        return value / self.m
    
    def get_period(self, max_iterations=10000):
        """Attempt to find the period (when sequence repeats)"""
        seen = {self.seed: 0}
        current = self.seed
        
        for i in range(1, max_iterations):
            current = (self.a * current + self.c) % self.m
            if current in seen:
                return i - seen[current]
            seen[current] = i
        
        return None  # Period not found within max_iterations

if __name__ == "__main__":
    print("=" * 60)
    print("Linear Congruential Generator (LCG) Demo")
    print("=" * 60)
    
    # Example 1: Default LCG
    print("\n[Example 1] Default LCG Parameters")
    print("-" * 60)
    lcg1 = LCG(seed=42)
    print(f"Seed: {lcg1.seed}")
    print(f"Multiplier (a): {lcg1.a}")
    print(f"Increment (c): {lcg1.c}")
    print(f"Modulus (m): {lcg1.m}")
    
    values = lcg1.generate(10)
    print(f"\nFirst 10 values: {values}")
    print(f"Normalized: {[lcg1.normalize(v) for v in values]}")
    
    # Example 2: Simple LCG with small parameters
    print("\n[Example 2] Simple LCG (Small Parameters)")
    print("-" * 60)
    lcg2 = LCG(seed=3, a=5, c=1, m=16)
    print(f"Seed: {lcg2.seed}")
    print(f"Multiplier (a): {lcg2.a}")
    print(f"Increment (c): {lcg2.c}")
    print(f"Modulus (m): {lcg2.m}")
    
    values = lcg2.generate(20)
    print(f"First 20 values: {values}")
    
    # Example 3: Period detection
    print("\n[Example 3] Period Detection")
    print("-" * 60)
    lcg3 = LCG(seed=1, a=5, c=1, m=16)
    period = lcg3.get_period()
    print(f"Period found: {period}")
    print(f"Sequence before repeat: {lcg3.sequence[:period if period else 10]}")
    
    # Example 4: Poor LCG (low quality randomness)
    print("\n[Example 4] Poor LCG Quality")
    print("-" * 60)
    lcg4 = LCG(seed=1, a=1, c=1, m=32)
    values = lcg4.generate(10)
    print(f"Poor LCG sequence: {values}")
    print(f"Period: {lcg4.get_period()}")
    print("Note: Poor parameters lead to short periods and patterns")
