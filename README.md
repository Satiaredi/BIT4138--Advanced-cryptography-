# WEEK 5: BLOCK CIPHERS AND FEISTEL STRUCTURES

## Topic
Block Cipher Design and Security Principles

## Learning Objectives
Students should be able to:
- Define block ciphers
- Explain permutations and substitutions
- Understand confusion and diffusion
- Implement Feistel structures
- Analyze avalanche effect

---

## Block Cipher Definition
A block cipher encrypts fixed-size blocks of plaintext using a secret key.

### Examples:
- DES (Data Encryption Standard)
- AES (Advanced Encryption Standard)
- Blowfish

---

## Stream Cipher vs Block Cipher

| Aspect | Stream Cipher | Block Cipher |
|--------|---------------|---------------|
| **Encryption** | One symbol at a time | Fixed-size blocks |
| **Speed** | Faster for streaming | Better for bulk data |
| **Method** | Uses keystream | Uses rounds |
| **Example** | RC4 | AES |

---

## Permutation
Rearranging positions of bits or characters to improve diffusion.

---

## Substitution
Replacing values using predefined mappings.

### Purpose:
- Introduce confusion
- Hide relationships

---

## Confusion
Hides the relationship between:
- Ciphertext
- Secret key

---

## Diffusion
Spreads plaintext influence throughout ciphertext.
- Changing one plaintext bit should affect many ciphertext bits

---

## Feistel Cipher Structure
Plaintext is divided into:
- Left half
- Right half

Encryption uses:
- XOR operations
- Swapping
- Multiple rounds

### Feistel Formula:
```
L_i = R_{i-1}
R_i = L_{i-1} XOR F(R_{i-1}, K_i)
```

---

## Avalanche Effect
A small plaintext change should cause large ciphertext changes.

---

## Practical Demonstrations
Students will:
- Divide plaintext into blocks
- Apply permutations
- Simulate substitutions
- Perform Feistel rounds
- Observe avalanche effect

---

## Class Activities

### Activity 1
Manual permutation practice.

### Activity 2
Feistel simulation using XOR.

### Activity 3
Discussion on confusion vs diffusion.

---

## Assignment 1
**Develop a simple block cipher simulation program.**

Requirements:
- Block division
- Substitution
- Permutation
- Multiple block handling

---

## Assignment 2
**Mini Research Report:**
1. DES
2. AES
3. Feistel structure
4. Confusion and diffusion

---

## Assignment 3
**Avalanche Effect Experiment:**
- Encrypt similar texts
- Change one character
- Compare outputs

---

## Advanced Programming Tasks
Students should:
- Add multiple rounds
- Implement block padding
- Build menu-driven encryption systems
- Develop mini Feistel ciphers

---

## Extra CAT Preparation Tasks

Students are encouraged to build:
- Mini stream cipher toolkit
- Randomness analyzer
- Block cipher simulator
- Cryptanalysis toolkit

### Bonus Marks Awarded For:
- Creativity
- Visualization
- Secure design improvements
- Advanced statistical testing
- Clear documentation
