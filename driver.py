import ElGamal
import RSA

def main():
    print("-----------------------------------------------------")
    print("Select the cryptographic algorithm:")
    print("-----------------------------------------------------")
    print("1. RSA")
    print("2. ElGamal")
    algorithm_choice = input("Enter your choice (1 or 2): ")

    if algorithm_choice == '1':
        rsa_operations()
    elif algorithm_choice == '2':
        elgamal_operations()
    else:
        print("Invalid choice. Please enter 1 or 2.")
    print("-----------------------------------------------------")

def rsa_operations():
    print("-----------------------------------------------------")
    print("------ SHARE YOUR PUBLIC KEY WITH THE SENDER --------")
    print("-----------------------------------------------------")
    pub_key, priv_key = RSA.generate_rsa_keys()
    print()
    print("Public Key (e,n): ", pub_key)
    print()
    print("-----------------------------------------------------")
    print("------------- DON'T SHARE PRIVATE KEY ---------------")
    print("-----------------------------------------------------")
    print()
    print("Private Key (d,n):", priv_key)
    print()
    print("-----------------------------------------------------")
    print("Select an RSA operation:")
    while True:
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Intercept a message")
        print("4. Exit")
        operation_choice = input("Enter your choice (1, 2, 3, or 4): ")
        if operation_choice == "1":
            rsa_encrypt()
        elif operation_choice == "2":
            rsa_decrypt()
        elif operation_choice == "3":
            rsa_intercept()
        elif operation_choice == "4":
            break
        else:
            print("Invalid option. Please try again.")
        print("-----------------------------------------------------")

def rsa_encrypt():
    print("-----------------------------------------------------")
    message = int(input("Message :"))
    e = int(input("Public key (e) : "))
    n = int(input("Enter n : "))
    encrypted_message = RSA.encrypt_rsa(message, (e, n))
    print("Encrypted message:", encrypted_message)

def rsa_decrypt():
    print("-----------------------------------------------------")
    encrypted_message = int(input("Encrypted message: "))
    d = int(input("Private key (d): "))
    n = int(input("Enter n: "))
    decrypted_message = RSA.decrypt_rsa(encrypted_message, (d, n))
    print("Decrypted message:", decrypted_message)

def rsa_intercept():
    print("-----------------------------------------------------")
    encrypted_message = int(input("Encrypted message :"))
    n = int(input("Enter n: "))
    e = int(input("Public key (e) : "))
    intercepted_message = RSA.intercept_rsa(encrypted_message, (e, n))
    print("Intercepted message:", intercepted_message)

def elgamal_operations():
    print("-----------------------------------------------------")
    print("------ SHARE YOUR PUBLIC KEY WITH THE SENDER --------")
    print("-----------------------------------------------------")
    pub_key, priv_key = ElGamal.generate_keys()
    print()
    print("Public Key (p, g, h): ", pub_key)
    print()
    print("-----------------------------------------------------")
    print("------------- DON'T SHARE PRIVATE KEY ---------------")
    print("-----------------------------------------------------")
    print()
    print("Private Key (x):", priv_key)
    print()
    print("-----------------------------------------------------")
    print("Select an ElGamal operation:")
    while True:
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Intercept a message")
        print("4. Exit")
        operation_choice = input("Enter your choice (1, 2, 3, or 4): ")
        if operation_choice == "1":
            elgamal_encrypt()
        elif operation_choice == "2":
            elgamal_decrypt()
        elif operation_choice == "3":
            elgamal_intercept()
        elif operation_choice == "4":
            break
        else:
            print("Invalid option. Please try again.")
        print("-----------------------------------------------------")


def elgamal_encrypt():
    print("-----------------------------------------------------")
    message = int(input("Message :"))
    print("Public key (p, g, h)")
    p = int(input("Enter p : "))
    g = int(input("Enter g : "))
    h = int(input("Enter h : "))
    encrypted_message = ElGamal.encrypt_elgamal(message, (p, g, h))
    print("Encrypted message:", encrypted_message)

def elgamal_decrypt():
    print("-----------------------------------------------------")
    print("Encrypted Message")
    c1 = int(input("Enter c1: "))
    c2 = int(input("Enter c2: "))
    x = int(input("Private key (x): "))
    p = int(input("Enter p: "))
    decrypted_message = ElGamal.decrypt_elgamal((c1,c2), x, p)
    print("Decrypted message:", decrypted_message)

def elgamal_intercept():
    print("-----------------------------------------------------")
    print("Encrypted message (c1, c2): ")
    c1 = int(input("Enter c1 :"))
    c2= int(input("Enter c2: "))
    p = int(input("Enter p : "))
    g = int(input("Enter g : "))
    h = int(input("Enter h : "))
    intercepted_message = ElGamal.intercept_elgamal((p,g,h), (c1, c2))
    print("Intercepted message:", intercepted_message)

if __name__ == "__main__":
    main()