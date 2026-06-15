# WEEK 3: PERIOD, LINEAR COMPLEXITY AND RANDOMNESS TESTING

## Topic
Stream Cipher Security Evaluation

## Learning Objectives
Students should be able to:
- Define period and linear complexity
- Generate pseudorandom sequences
- Perform randomness testing
- Analyze weak generators

---

## Key Definitions

### Period
The number of values generated before repetition occurs.

**Example:**
```
Sequence: 2, 5, 7, 2, 5, 7
Period = 3
```

### Linear Complexity
Measures how difficult it is to reproduce a sequence using linear relationships.
- High complexity = stronger security

---

## Pseudorandom Sequence Generators

### Common Examples:
- LCG (Linear Congruential Generator)
- LFSR (Linear Feedback Shift Register)
- Python random module

### LCG Formula:
```
X_{n+1} = (aX_n + c) mod m
```

---

## Randomness Testing

### Common Tests
1. **Frequency Test** - Tests if 0s and 1s occur with equal probability
2. **Runs Test** - Tests if there are too many or too few runs
3. **Mean Test** - Tests if mean value is within expected range
4. **Chi-Square Test** - Statistical test for goodness of fit

### Why Statistical Testing Matters
**Benefits:**
- Detect weak generators
- Improve cipher security
- Evaluate unpredictability

---

## Practical Demonstrations

### Demonstration 1
Generate binary random sequences.

### Demonstration 2
Implement an LCG generator.

### Demonstration 3
Perform Frequency Test.

### Demonstration 4
Perform Runs Test.

### Demonstration 5
Perform Mean Test.

---

## Class Activities

### Activity 1: Finding Sequence Period
Students analyze:
- Repeated values
- Period length
- Effects of modulus changes

### Activity 2: Randomness Observation
Students compare:
- Frequency balance
- Runs count
- Repetition patterns

---

## Assignment 1
**Develop a randomness testing program that:**
- Generates 100+ random bits
- Performs statistical tests
- Displays interpretations

---

## Assignment 2
**Research:**
- Importance of randomness
- Weak random generators
- Historical cryptographic failures

**Suggested Examples:**
- Debian OpenSSL bug
- Weak encryption keys

---

## Advanced Programming Tasks
- User-defined sequence length
- Save results to file
- Menu-driven testing system
- Graph visualization using matplotlib
