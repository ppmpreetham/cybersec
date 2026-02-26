# Cryptography

Cryptography is the practice and study of techniques for secure communication in the presence of third parties called adversaries. In CTFs, it involves breaking weak implementations, analyzing classical/modern ciphers, cracking hashes, exploiting misconfigurations in protocols (RSA, AES, ECC, etc.), and increasingly tackling post-quantum challenges.

## Why Cryptography in CTFs?
Cryptography challenges test understanding of algorithms, mathematical foundations (number theory, lattices, discrete logs), implementation flaws, side-channels, and cryptanalysis techniques. They appear in almost every major CTF and range from beginner encodings to advanced attacks like Coppersmith or padding oracles.

## Types of Cryptography Challenges

### Classical Ciphers

Involves monoalphabetic, polyalphabetic, transposition, substitution, Vigenère, Beaufort, etc. Often combined with encodings (Base64, Hex, URL).
**Common Techniques:**
- Frequency analysis
- Index of coincidence
- Known-plaintext attacks
**Common Tools:**
- [CyberChef](https://gchq.github.io/CyberChef) : browser-based multi-operation crypto/encoding Swiss Army knife
- [dCode](https://www.dcode.fr) : huge collection of classical cipher solvers and tools
- [quipqiup](https://quipqiup.com) : automatic substitution cipher solver with frequency analysis

### Modern Symmetric / Asymmetric Attacks
AES modes (ECB, CBC padding oracles), RSA factoring/weak keys, ECC invalid curve, hash length extension, etc.
**Common Techniques:**
- Padding oracle attacks
- Small exponent / common modulus RSA
- Wiener attack
- Lattice reduction (LLL/Coppersmith)
**Common Tools:**
- [RsaCtfTool](https://github.com/RsaCtfTool/RsaCtfTool) : attacks common RSA weaknesses (factoring, Wiener, small exponents, etc.)
- [padre](https://github.com/glebarez/padre) : padding oracle attack detector and exploiter
- [attacksrsa](https://github.com/attackingrsa/attacksrsa) : collection of advanced RSA attacks (Boneh-Durfee, Coppersmith, etc.)
- [Factordb](http://factordb.com) : online integer factorization database

### Hash & Password Cracking
Cracking weak hashes (MD5, SHA-1), unsalted passwords, or custom hash functions.
**Common Techniques:**
- Dictionary + rules attacks
- Mask attacks
- Rainbow tables (less common now)
**Common Tools:**
- [Hashcat](https://hashcat.net/hashcat) : GPU-accelerated fastest hash cracker
- [John the Ripper](https://www.openwall.com/john) : versatile CPU-based hash cracker with community rules

### Stream Ciphers & XOR
Repeating-key XOR, stream cipher malleability, known-plaintext.
**Common Techniques:**
- Hamming distance for key length
- Crib-dragging
**Common Tools:**
- [xortool](https://github.com/hellman/xortool) : analyzes multi-byte XOR (repeating key detection)
- [cribdrag](https://github.com/SpiderLabs/cribdrag) : interactive crib-dragging for stream ciphers

### Automated & Miscellaneous
Tools that detect/attack multiple weaknesses automatically.
**Common Tools:**
- [FeatherDuster](https://github.com/nccgroup/featherduster) : automated cryptanalysis for common protocol weaknesses
- [yafu](https://github.com/bbuhrow/yafu) : fast integer factorization (SIQS, ECM)
- [msieve](https://github.com/radii/msieve) : GNFS for large numbers
- [Cryptohack](https://cryptohack.org) : interactive platform with built-in crypto challenges and practice

### Post-Quantum & Lattice-Based
Emerging in advanced CTFs (Kyber attacks, LWE/MLWE, lattice reduction).
**Common Techniques:**
- Lattice basis reduction
- Learning With Errors (LWE) attacks
**Common Tools:**
- [sage](https://www.sagemath.org) : mathematical software with lattice/crypto modules (use LLL, BKZ)
- [sympy](https://www.sympy.org) : symbolic math for number theory attacks
- [pqclean](https://pqclean.org) : clean post-quantum implementations (for understanding/testing)

---
## Practice
- [CryptoHack](https://cryptohack.org) : best interactive crypto learning + challenges
- [OverTheWire Natas / Bandit](https://overthewire.org) : some crypto elements
- [picoCTF Crypto](https://picoctf.org) : beginner-friendly crypto track
- [Cryptohack Challenges](https://cryptohack.org/challenges) : post-quantum and lattice too

---
## Common Resources
- **SageMath** for number theory / lattice scripts
- **Python libs**: PyCryptodome, cryptography, gmpy2 (bigints), mpmath (precision)
- **Google Dorks for crypto**: `filetype:pdf cryptography` or `intext:"BEGIN RSA PRIVATE KEY"`
- **Writeups**: Search CTFtime.org or GitHub for challenge names + "writeup"

## Analysis & Testing Tools

[Hashcat](https://hashcat.net/hashcat) : world's fastest password/hash recovery tool (GPU-accelerated)  
[John the Ripper](https://www.openwall.com/john) : fast password cracker supporting many hash formats and attack modes  
[CyberChef](https://gchq.github.io/CyberChef) : browser-based "Swiss Army knife" for encryption, encoding, hashing, compression, forensics  
[quipqiup](https://quipqiup.com) : online tool for solving substitution ciphers and frequency analysis  
[dCode](https://www.dcode.fr) : massive online collection of solvers for classical ciphers, hash identifiers, modern crypto attacks and tools  
[RsaCtfTool](https://github.com/RsaCtfTool/RsaCtfTool) : multi-tool for attacking common RSA vulnerabilities (factoring, Wiener, common modulus, small exponents, etc.)  
[xortool](https://github.com/hellman/xortool) : analyzes multi-byte XOR-encrypted data (very useful for repeating-key XOR)  
[FeatherDuster](https://github.com/nccgroup/featherduster) : automated cryptanalysis tool that detects and exploits common weaknesses in crypto implementations  
[Cryptohack](https://cryptohack.org) : interactive learning platform with built-in challenges and solvers (great for practice)  
[Factordb](http://factordb.com) : online database for factoring small/medium integers (very useful when n is factorable or already in DB)  
[yafu](https://github.com/bbuhrow/yafu) : Yet Another Factoring Utility — very fast integer factorization tool (SIQS, ECM, etc.)  
[cribdrag](https://github.com/SpiderLabs/cribdrag) : interactive crib-dragging tool for breaking stream ciphers and known-plaintext attacks  
[padre](https://github.com/glebarez/padre) : Padding Oracle Attack detector & exploiter (very useful for CBC padding oracles)  
[attacksrsa](https://github.com/attackingrsa/attacksrsa) : collection of many RSA attacks (Boneh-Durfee, Coppersmith, etc.) in one place  
[msieve](https://github.com/radii/msieve) : general number field sieve (GNFS) implementation for large integer factorization  

## Cryptographic Libraries (for devs)

[libsodium](https://doc.libsodium.org) : easy-to-use, high-speed, modern cryptography library (preferred for new projects)  
[OpenSSL](https://www.openssl.org) : the most widely used C library for TLS/SSL, certificates, and general crypto primitives  
[cryptography (Python)](https://cryptography.io) : modern, actively maintained Python cryptography library  
[Bouncy Castle](https://www.bouncycastle.org) : comprehensive crypto library for Java and C# (supports post-quantum algorithms)  
[PyCryptodome](https://pycryptodome.readthedocs.io) : self-contained Python package of low-level cryptographic primitives  
[rustls](https://rustls.rs) : modern TLS library for Rust written in safe Rust  
[sympy](https://www.sympy.org) : symbolic math library (perfect for number theory, modular arithmetic, discrete logs in crypto challenges)  
[mpmath](https://mpmath.org) : arbitrary-precision floating-point arithmetic (essential for high-precision math in crypto attacks)  
[gmpy2](https://github.com/aleaxit/gmpy) : Python interface to GMP library (fast multiple-precision arithmetic, very useful for big integers)  
[pqclean](https://pqclean.org) : clean implementations of post-quantum KEMs and signatures (for testing/research)  
[oqs-provider](https://openquantumsafe.org) : Open Quantum Safe provider for OpenSSL (adds post-quantum algorithms to OpenSSL)  
[wolfSSL](https://www.wolfssl.com) : lightweight, fast, embedded-friendly TLS/crypto library (alternative to OpenSSL)  

---
## Disclaimer
This repository is intended for educational and informational purposes only. The author does not condone or promote any illegal activities.
---
## Contact
If you have any questions or suggestions, feel free to reach out to me on [LinkedIn](https://www.linkedin.com/in/preethampete/).