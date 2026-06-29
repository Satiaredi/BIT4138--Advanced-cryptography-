# WEEK 6: SYMMETRIC CIPHERS II – SUBSTITUTION-PERMUTATION NETWORKS (SPN), S-BOXES AND NON-LINEARITY

## Learning Objectives
By the end of this week, students should be able to:
1. Define a Substitution-Permutation Network (SPN)
2. Explain the role of S-Boxes in block cipher design
3. Understand the concept of non-linearity in cryptography
4. Differentiate between Feistel Networks and SPNs
5. Describe how modern block ciphers such as AES use SPN structures
6. Implement a simple SPN model using Python
7. Analyze the security benefits of non-linear transformations

---

## Introduction
In Week 5, we studied Feistel ciphers, confusion, diffusion, and block cipher fundamentals. While many block ciphers such as DES use Feistel structures, modern encryption standards such as AES use a different design called the Substitution-Permutation Network (SPN).

SPNs combine substitution and permutation operations repeatedly to transform plaintext into ciphertext. These operations create confusion and diffusion, making it difficult for attackers to discover relationships between plaintext, ciphertext, and secret keys.

This week focuses on understanding how SPNs work, the importance of S-Boxes, and why non-linearity is critical in secure cryptographic systems.

---

## Key Definitions

### Substitution-Permutation Network (SPN)
An SPN is a block cipher structure that repeatedly applies:
1. Substitution
2. Permutation
3. Key Mixing

across several rounds.

**Examples:**
- AES (Advanced Encryption Standard)
- PRESENT Cipher
- SERPENT Cipher

---

### Substitution
Substitution replaces data elements with alternative values according to predefined rules.

**Example:**
| Input | Output |
|-------|--------|
| 0000 | 1110 |
| 0001 | 0100 |
| 0010 | 1101 |

**Purpose:**
- Introduces confusion
- Hides relationships between plaintext and ciphertext

---

### Permutation
Permutation rearranges the positions of bits without changing their values.

**Example:**
- Original: ABCD
- Permuted: CDAB

**Purpose:**
- Introduces diffusion
- Spreads information across the block

---

### S-Box (Substitution Box)
An S-Box is a lookup table used to substitute input values with output values.

**Example:**
| Input | Output |
|-------|--------|
| 0 | 14 |
| 1 | 4 |
| 2 | 13 |
| 3 | 1 |

**Purpose:**
- Introduces non-linearity
- Increases resistance to cryptanalysis

---

### Non-Linearity
Non-linearity refers to the inability to express a cryptographic transformation using simple linear equations.

**Importance:**
- Prevents attackers from predicting outputs
- Improves cipher strength
- Resists algebraic attacks

---

## SPN Structure
A typical SPN consists of multiple rounds:

```
Plaintext
    ↓
Round Key Addition
    ↓
Substitution (S-Box)
    ↓
Permutation
    ↓
Round Key Addition
    ↓
Substitution
    ↓
Permutation
    ↓
Ciphertext
```

Each round strengthens security.

---

## Difference Between Feistel and SPN Structures

| Aspect | Feistel Network | SPN |
|--------|-----------------|-----|
| **Data Splitting** | Splits data into halves | Operates on entire block |
| **Operations** | Uses round functions | Uses S-Boxes and permutations |
| **Decryption** | Same process for decryption | Separate inverse operations |
| **Example** | DES | AES |

---

## Why S-Boxes Matter

**Without S-Boxes:**
- Encryption becomes predictable
- Attackers can create equations describing the cipher
- Keys become easier to recover

**With S-Boxes:**
- Relationships become highly complex
- Patterns disappear
- Security improves significantly

---

## Non-Linearity and Security
Good S-Boxes provide:
- High non-linearity
- Resistance to linear cryptanalysis
- Resistance to differential cryptanalysis
- Avalanche effect

---

## Avalanche Effect

### Definition
A small change in plaintext or key should produce a large change in ciphertext.

**Example:**
- Plaintext 1: HELLO
- Plaintext 2: HELLo

The resulting ciphertexts should appear completely different.

---

## Modern Applications of SPNs
SPN structures are used in:
- AES Encryption
- Secure Banking Systems
- VPN Communications
- Secure Messaging Platforms
- Government Information Systems
- Cloud Security

---

## Mathematical Concept

A substitution operation can be represented as:
```
Y = S(X)
```

Where:
- X = Input value
- S = Substitution function (S-Box)
- Y = Output value

Permutation can be represented as:
```
P(X)
```

Where:
- P rearranges bit positions

---

## Class Demonstrations

### Demonstration 1: Simple Substitution Example
```python
sbox = {
    0: 14,
    1: 4,
    2: 13,
    3: 1
}

print(sbox[2])
```
**Expected Output:** 13

### Demonstration 2: Simple Permutation
```python
data = "ABCD"
permuted = data[2] + data[3] + data[0] + data[1]
print(permuted)
```
**Output:** CDAB

### Demonstration 3: Combining Substitution and Permutation
```python
plaintext = "1234"
substituted = "5678"
permuted = substituted[::-1]
print(permuted)
```

### Demonstration 4: Simple SPN Round
```python
plaintext = 9
key = 5
mixed = plaintext ^ key
print("Round Output:", mixed)
```

### Demonstration 5: Avalanche Observation
```python
text1 = "HELLO"
text2 = "HELLo"
print(hash(text1))
print(hash(text2))
```

---

## Class Activities

### Activity 1: Manual SPN Simulation
**Instructions:**
1. Take a 4-bit binary number
2. Apply substitution using a provided S-Box
3. Perform permutation
4. Repeat for two rounds

**Skills Developed:**
- Understanding SPN workflow
- Confusion and diffusion analysis

### Activity 2: S-Box Analysis
**Students should:**
1. Observe S-Box mappings
2. Identify repeated outputs
3. Discuss whether the S-Box appears secure

**Discussion Questions:**
- Why should outputs be unique?
- How do S-Boxes improve security?

### Activity 3: Feistel vs SPN Comparison
**Students compare:**
- Structure
- Security
- Complexity
- Practical applications

---

## Practical Tasks

### Task 1: Basic SPN Design
Develop a simple SPN implementation in Python.

**Requirements:**
1. User enters plaintext
2. Apply substitution
3. Apply permutation
4. Display ciphertext

**Deliverables:**
- Source code
- Screenshots
- Explanation of process

### Task 2: Non-Linearity Investigation
Research and explain:
1. What is non-linearity?
2. Why is it important in cryptography?
3. How do S-Boxes create non-linearity?

**Report Requirements:**
- 2–3 pages
- Include examples
- Include references

### Task 3: SPN Security Evaluation
Compare:
- SPN Structure
- Feistel Structure

Evaluate:
- Security
- Performance
- Ease of implementation
- Modern usage

---

## Advanced Programming Tasks
Modify the SPN implementation to:
1. Support multiple rounds
2. Accept custom keys
3. Use a larger S-Box
4. Demonstrate avalanche effect

---

## Challenge Task
Create a mini AES-inspired encryption simulator that includes:
- Key Mixing
- Substitution
- Permutation
- Multiple Rounds

**Bonus Features:**
- Graphical Interface
- User-selected keys
- Encryption and Decryption
- Security Analysis Report

---

## Recommended Tools
| Activity | Suggested Tools |
|----------|------------------|
| Programming | Python IDLE, VS Code |
| Cryptography Experiments | PyCryptodome |
| Visualization | Jupyter Notebook |
| Documentation | MS Word, Google Docs |
| Version Control | GitHub |

---

## Weekly Reflection Questions
1. What is a Substitution-Permutation Network?
2. How does an S-Box improve security?
3. Why is non-linearity important in block ciphers?
4. What is the difference between Feistel and SPN structures?
5. How does permutation contribute to diffusion?
6. What is the avalanche effect?
7. Why is AES considered secure?

---

## CAT 1 Follow-Up and Portfolio Development
Students should upload all Week 1–6 practical work to GitHub and organize it professionally.

**Repository Example:**
```
BIT4138-Advanced-Cryptography
├── Python Programs
├── Screenshots of Outputs
├── Notes and Reflections
├── Practical Reports
└── CAT 1 Corrections and Improvements
```

---

## Industry Insight
Almost every secure digital service today relies on block cipher technology. AES, which is based on the SPN structure studied this week, protects:
- Online Banking
- Mobile Money Transactions
- Government Systems
- Cloud Platforms
- Healthcare Records
- E-commerce Websites

Understanding SPNs and non-linearity gives students a strong foundation for careers in:
- Cybersecurity
- Software Engineering
- Digital Forensics
- Network Security
- Cloud Security
- AI Security
- Cryptographic Research

Security knowledge is becoming a valuable skill in every technology career, making cryptography one of the most practical and future-oriented fields in computing.
