## RSA Encryption

### Difficulty Level: Hard

### Instructions
**Task A**: Write an algorithm that performs an RSA encryption of a message. Clearly state the invariants. (How should one go about decrpyting the message?)

**Task B**: You have been given a message that is RSA encrypted. Write an algorithm that breaks it. Clearly state the invariants. (What did you observe?)

**Task C**: How does an RSA differ from Diffie Hellman algorithm, or other algorithms, you learned in class?

#####################################################################################################################################

SHREEVAR'S PART:
There was a lecture by Professor Debayan Gupta which touched the RSA Encryption. Along with that knowledge and a YouTube video, these are my learnings.
RSA encryption is a widely used public-key cryptographic system that secures digital communication by relying on the mathematical difficulty of factoring large prime numbers. The process begins with key generation, where two large prime numbers (p and q) are selected and multiplied to get n, which serves as the modulus for both the public and private keys. A public exponent e is chosen such that it is relatively prime to (p−1)(q−1), and a private exponent d is calculated so that it satisfies the modular inverse condition. The public key is then (e, n) and the private key is (d, n). For encryption, a plaintext message m is converted into ciphertext c using the formula c = m^e mod n. To decrypt the message, the receiver uses the private key to compute m = c^d mod n. RSA’s security comes from the fact that while it is easy to multiply large primes, it is extremely difficult and time-consuming to factor their product, especially when the numbers involved are very large. RSA is foundational to digital security and is commonly used in web browsers (HTTPS), email encryption, VPNs, and digital signatures.

This was extremely interesting to look into, but hard to understand, but still I tried.

SOURCES: https://www.youtube.com/watch?v=ZPXVSJnDA_A