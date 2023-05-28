import rsa

rsa.LOGGING = False

keys = rsa.generate_rsa_pair(16)
encrypted_data = rsa.encrypt_data(input("Enter text: "), keys["public_key"])
decrypted_data = rsa.decrypt_data(encrypted_data, keys["private_key"])

print(encrypted_data, decrypted_data, sep="\n")
