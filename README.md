# WEEK 2: STREAM CIPHERS AND PSEUDORANDOMNESS

## Topic
Symmetric Ciphers I – Stream Ciphers

## Learning Objectives
Students should be able to:
- Define stream ciphers
- Differentiate randomness and pseudorandomness
- Explain One-Time Pad (OTP)
- Understand keystream generators
- Implement simple pseudorandom generators in Python

---

## Stream Cipher Definition
A stream cipher encrypts plaintext one bit or character at a time using a keystream.

### Formula
```
Ciphertext = Plaintext XOR Keystream
```

---

## Randomness vs Pseudorandomness

### True Randomness
- Generated from unpredictable physical processes
- Examples:
  - Atmospheric noise
  - Hardware random generators

### Pseudorandomness
- Generated mathematically using algorithms
- Examples:
  - Python random module
  - Linear Congruential Generator (LCG)

---

## One-Time Pad (OTP)
A theoretically unbreakable encryption system where:
- Key length equals message length
- Key is truly random
- Key is used only once

---

## Keystream Generators
Algorithms that generate pseudorandom sequences.

### Examples:
- LFSR (Linear Feedback Shift Register)
- RC4
- PRNGs (Pseudo-Random Number Generators)

### Requirements:
- Long period
- High unpredictability
- Statistical randomness

---

## Important Terms

### Seed
Initial value used in generation.

### Period
Length before repetition occurs.

### Entropy
Measure of unpredictability.

---

## Practical Demonstrations

### Demonstration 1: Python Random Numbers
Students generate random numbers using Python.

### Demonstration 2: Linear Congruential Generator (LCG)
Students observe pseudorandom sequence generation and repetition.

### Demonstration 3: XOR Stream Cipher
Students perform encryption and decryption using XOR operations.

### Demonstration 4: OTP Simulation
Students generate random keys and simulate OTP encryption.

---

## Class Activities

### Activity 1: Manual XOR Practice
Students:
- Convert letters into ASCII
- Apply XOR manually
- Recover plaintext

### Activity 2: PRNG Analysis
Students change:
- Seed
- Multiplier
- Modulus

Then observe:
- Repetition
- Randomness quality

---

## Assignment 1
**Develop a pseudorandom sequence generator in Python.**

Requirements:
- Accept user seed
- Generate 20+ values
- Explain period and randomness observations

---

## Assignment 2
**Mini Research Report:**
1. One-Time Pad
2. RC4 Stream Cipher
3. Real-world applications

---

## Advanced Practice Tasks

### Task 1
Modify XOR program to:
- Accept user input
- Encrypt full sentences
- Preserve spaces

### Task 2
Create a menu-driven stream cipher application.

### Task 3
Compare:
- True Random Generators
- Pseudorandom Generators

Discuss:
- Security
- Cost
- Speed
- Practicality
