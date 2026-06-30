# WEEK 4: STREAM CIPHER CRYPTANALYSIS

## Topic
Berlekamp-Massey Algorithm and Algebraic Attacks

## Learning Objectives
Students should be able to:
- Define cryptanalysis
- Explain stream cipher attacks
- Understand LFSRs
- Apply Berlekamp-Massey Algorithm
- Analyze weaknesses in stream ciphers

---

## Cryptanalysis
The process of breaking cryptographic systems without knowing the secret key.

---

## Common Attack Types

### Ciphertext-only attack
Attacker has only ciphertext, no plaintext knowledge

### Known plaintext attack
Attacker knows some plaintext-ciphertext pairs

### Chosen plaintext attack
Attacker can choose plaintext to encrypt

### Algebraic attack
Attacker converts cipher into mathematical equations and solves them

---

## Linear Feedback Shift Register (LFSR)
A shift register using linear functions of previous bits.

### General LFSR Formula
```
S_n = S_{n-1} XOR S_{n-3}
```

Where:
- ( S_n ) = Newly generated bit
- ( S_{n-1} ) = Previous bit
- ( S_{n-3} ) = Third previous bit
- XOR = XOR (Exclusive OR) operation

---

## Berlekamp-Massey Algorithm
An algorithm used to determine the shortest LFSR capable of generating a binary sequence.

### Purpose:
- Recover recurrence relation
- Determine linear complexity
- Predict future sequence values

---

## Algebraic Attacks
Attackers convert cipher systems into equations and solve them mathematically.

### Targets:
- Weak nonlinear systems
- Filter generators
- Combination generators

---

## Security Measures
Secure stream ciphers should include:
- Long period
- High linear complexity
- Strong randomness
- Nonlinear components

### Modern examples:
- ChaCha20
- Salsa20

---

## Practical Demonstrations
Students will:
- Generate LFSR sequences
- Detect repetition
- Observe predictability
- Analyze weak patterns

---

## Assignments

### Programming Task
Develop an LFSR generator that:
- Detects repeated states
- Estimates sequence period
- Displays weaknesses

### Research Task
Research:
- Berlekamp-Massey Algorithm
- Algebraic attacks
- RC4 vulnerabilities

---

## Advanced Tasks
Students should build:
- Menu-driven stream cipher analyzer
- Randomness visualization tools
- Mini cryptanalysis toolkit
