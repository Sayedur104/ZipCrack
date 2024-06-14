import pyzipper
import time
import itertools
import string
import os

def print_banner():
    print("""
    ##############################################
    #                zL                          #
    ##############################################
    """)

def get_possible_characters(option):
    if option == 1:
        return string.ascii_uppercase
    elif option == 2:
        return string.ascii_lowercase
    elif option == 3:
        return string.ascii_letters
    elif option == 4:
        return string.digits
    elif option == 5:
        return string.ascii_uppercase + string.digits
    elif option == 6:
        return string.ascii_lowercase + string.digits
    elif option == 7:
        return string.ascii_letters + string.digits
    else:
        print("Invalid option")
        return ""

def get_valid_zip_path():
    while True:
        zip_path = input("Enter the path to the zip file: ")
        if os.path.isfile(zip_path):
            return zip_path
        else:
            print("File path is not valid. Please enter a valid file path.")

def get_output_folder():
    output_folder = input("Enter the name for the output folder (leave blank for default 'Output'): ")
    if not output_folder:
        output_folder = "Output"
    return output_folder

def test_password(zip_path, password):
    try:
        with pyzipper.AESZipFile(zip_path) as zip_file:
            zip_file.extractall(pwd=password.encode('utf-8'))
        return True
    except:
        return False

def brute_force_zip(zip_path, output_folder, possible_characters, min_length, max_length):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Output folder '{output_folder}' created successfully.")
    
    start_time = time.time()
    tried_passwords = 0
    
    for length in range(min_length, max_length + 1):
        for password_tuple in itertools.product(possible_characters, repeat=length):
            password = ''.join(password_tuple)
            tried_passwords += 1
            print(f"\rTrying password: {password}", end='', flush=True)
            
            if test_password(zip_path, password):
                elapsed_time = time.time() - start_time
                print(f"\nPassword found: {password}")
                print(f"Passwords tried: {tried_passwords}")
                print(f"Time taken: {elapsed_time:.2f} seconds")
                return password
            
    elapsed_time = time.time() - start_time
    print("\nPassword not found within the given length.")
    print(f"Passwords tried: {tried_passwords}")
    print(f"Time taken: {elapsed_time:.2f} seconds")
    return None

def main():
    print_banner()
    
    correct_password = "Update104"
    user_password = input("Enter the password to start the program: ")
    
    if user_password != correct_password:
        print("Incorrect password. Please contact for the correct password.")
        return
    
    print("Password correct. Continuing program execution...")
    
    zip_path = get_valid_zip_path()
    output_folder = get_output_folder()
    
    min_length = int(input("Enter the minimum password length to try: "))
    max_length = int(input("Enter the maximum password length to try: "))
    
    print("""
    Choose the type of characters to try in passwords:
    1: Capital letters
    2: Small letters
    3: Capital and small letters
    4: Numbers
    5: Capital letters and numbers
    6: Small letters and numbers
    7: Capital letters, small letters, and numbers
    """)
    pattern_option = int(input("Enter the number corresponding to your choice: "))
    
    possible_characters = get_possible_characters(pattern_option)
    
    if possible_characters:
        print("Starting brute-force attack...")
        brute_force_zip(zip_path, output_folder, possible_characters, min_length, max_length)
    else:
        print("Invalid character set option. Exiting program.")

if __name__ == "__main__":
    main()
