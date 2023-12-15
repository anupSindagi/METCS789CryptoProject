
  

# MET CS 789 Cryptography Project

  

## Overview

This project is focused on implementing various cryptographic algorithms and functions in Python. It includes implementations of key cryptographic concepts such as RSA, ElGamal, and several algorithms for prime number testing and factorization.

  

## Modules

The project is divided into several modules, each focusing on different aspects of cryptography:

  

### CryptoFunctions.py

- Contains fundamental cryptographic functions used across the project.

- Includes implementations of algorithms like Pollard's Rho and Miller-Rabin primality test.

  

### RSA.py

- Dedicated to the RSA (Rivest–Shamir–Adleman) algorithm.

- Provides functionality for key generation, encryption, and decryption using RSA.

  

### ElGamal.py

- Focuses on the ElGamal encryption system.

- Includes key generation, encryption, and decryption functions specific to ElGamal.

  

### driver.py

- Serves as the main entry point for testing and demonstrating the cryptographic functions and algorithms.


  

## Usage

- Each module can be used independently to test and execute specific cryptographic algorithms.

-  `driver.py` can be used to see examples of how each module and function can be utilized.

  

## Testing

- Unit tests are provided for critical functions to ensure correctness and reliability.

- Tests include a variety of scenarios to validate the functionality of the cryptographic algorithms.

- To run coverage
- `pip3 install coverage`
- `python3 -m coverage run -m unittest discover -s tests` 
- `python3 -m coverage html`

![enter image description here](https://i.imgur.com/lm5aCpD.png)