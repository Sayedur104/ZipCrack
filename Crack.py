import pyzipper
import itertools
import string
import time
import os

def print_banner(name):
    banner = f"""
\033[92m
##############################################
#                {name}                      #
##############################################
\033[0m
"""
    print(banner)

def test_password(zip_path, password):
    try:
        with pyzipper.AESZipFile(zip_path) as zip_file:
            zip_file.pwd = password.encode('utf-8')
            # Try to read all files in the zip to ensure the password is correct
            for file in zip_file.infolist():
                try:
                    with zip_file.open(file) as f:
                        f.read()
                except Exception:
                    return False  # If any file fails to read, the password is incorrect
        return True
    except Exception:
        return False

def brute_force_zip(zip_path, output_folder, possible_characters, min_password_length, max_password_length):
    tried_passwords = 0
    start_time = time.time()
    for length in range(min_password_length, max_password_length + 1):
        for password in itertools.product(possible_characters, repeat=length):
            pwd = ''.join(password)
            tried_passwords += 1
            print(f"\033[93mTrying password: {pwd}\033[0m", end='\r', flush=True)  # Show each password being tried in the same line
            if test_password(zip_path, pwd):
                try:
                    with pyzipper.AESZipFile(zip_path) as zip_file:
                        zip_file.pwd = pwd.encode('utf-8')
                        # Create the output folder if it doesn't exist
                        if not os.path.exists(output_folder):
                            os.makedirs(output_folder)
                            print(f"\033[94mOutput folder '{output_folder}' created successfully.\033[0m")
                        zip_file.extractall(path=output_folder)
                    elapsed_time = time.time() - start_time
                    print(f"\033[92m\nPassword found: {pwd}\033[0m")
                    print(f"\033[92mPasswords tried: {tried_passwords}\033[0m")
                    print(f"\033[92mTime taken: {elapsed_time:.2f} seconds\033[0m")
                    return True, tried_passwords
                except Exception as e:
                    print(f"\033[91mError extracting with password {pwd}: {e}\033[0m")
                    return False, tried_passwords
    elapsed_time = time.time() - start_time
    print(f"\033[91m\nPassword not found within the given length.\033[0m")
    print(f"\033[91mPasswords tried: {tried_passwords}\033[0m")
    print(f"\033[91mTime taken: {elapsed_time:.2f} seconds\033[0m")
    return False, tried_passwords

def get_possible_characters(option):
    if option == '1':
        return string.ascii_uppercase  # Capital letters
    elif option == '2':
        return string.ascii_lowercase  # Small letters
    elif option == '3':
        return string.ascii_letters  # Capital and small letters
    elif option == '4':
        return string.digits  # Numbers
    elif option == '5':
        return string.ascii_uppercase + string.digits  # Capital letters and numbers
    elif option == '6':
        return string.ascii_lowercase + string.digits  # Small letters and numbers
    elif option == '7':
        return string.ascii_letters + string.digits  # Capital letters, small letters, and numbers
    else:
        raise ValueError("Invalid option")

def get_valid_zip_path():
    while True:
        zip_path = input("\033[96mEnter the path to the zip file: \033[0m")
        if os.path.isfile(zip_path):
            return zip_path
        else:
            print("\033[91mFile path is not valid. Please enter a valid file path.\033[0m")

def get_output_folder():
    output_folder = input("\033[96mEnter the name for the output folder (leave blank for default 'Output'): \033[0m")
    if output_folder == '':
        output_folder = 'Output'
    else:
        output_folder = f"Output_{output_folder}"
    return output_folder

# Print the banner with your name
print_banner("SAYEDUR 104")

# Get the password from the user
user_password = input("\033[96mEnter the password to start the program: \033[0m")
correct_password = "Update104"

# Check if the provided password is correct
if user_password != correct_password:
    print("\033[91mIncorrect password. Please contact for the correct password.\033[0m")
else:
    print("\033[92mPassword correct. Continuing program execution...\033[0m")

    # Get the zip file path from the user
    zip_path = get_valid_zip_path()

    # Get the minimum and maximum password length from the user
    min_password_length = int(input("\033[96mEnter the minimum password length to try: \033[0m"))
    max_password_length = int(input("\033[96mEnter the maximum password length to try: \033[0m"))

    # Show the pattern options to the user
    print("\033[96m\nChoose the type of characters to try in passwords:\033[0m")
    print("1: Capital letters")
    print("2: Small letters")
    print("3: Capital and small letters")
    print("4: Numbers")
    print("5: Capital letters and numbers")
    print("6: Small letters and numbers")
    print("7: Capital letters, small letters, and numbers")

    # Get the character pattern option from the user
    pattern_option = input("\033[96mEnter the number corresponding to your choice: \033[0m")
    possible_characters = get_possible_characters(pattern_option)

    output_folder = get_output_folder()  # Define your output folder here

    print("\033[96m\nStarting brute-force attack...\033[0m\n")
    success, tried_passwords = brute_force_zip(zip_path, output_folder, possible_characters, min_password_length, max_password_length)

    if success:
        print("\033[92m\nPassword recovery successful.\033[0m")
    else:
        print("\033[91m\nPassword recovery failed.\033[0m")