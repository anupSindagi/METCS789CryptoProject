import unittest
import sys
sys.path.append('./')

from ElGamal import*

class TestElGamal(unittest.TestCase):

    def test_generate_keys(self):
        bit_length = 24
        (p, g, h), x = generate_keys(bit_length)

        self.assertTrue(is_prime(p), "p should be a prime number")

        self.assertTrue(is_primitive_root(g, p), "g should be a primitive root modulo p")

        self.assertEqual(h, pow(g, x, p), "h should be equal to g^x mod p")

        self.assertEqual(p.bit_length(), bit_length, "Bit length of p should be equal to the specified bit length")

    def test_encrypt_decrypt(self):
        public_key, private_key = generate_keys(24)  
        original_message = 123123

        ciphertext = encrypt_elgamal(original_message, public_key)
        decrypted_message = decrypt_elgamal(ciphertext, private_key, public_key[0])

        self.assertEqual(original_message, decrypted_message)

    def test_interception(self):
        # solving discrete logarithm
        public_key, _ = generate_keys(24) 
        original_message = 123123

        ciphertext = encrypt_elgamal(original_message, public_key)
        intercepted_message = intercept_elgamal(public_key, ciphertext)

        self.assertEqual(original_message, intercepted_message)

        # test for incorrect public key set
        intercepted_message = intercept_elgamal((11,2,0), ciphertext)
        self.assertEqual(intercepted_message, None)
        
# Commentting out to run coverage.py for complete test coverage     
# if __name__ == '__main__':
#     unittest.main()