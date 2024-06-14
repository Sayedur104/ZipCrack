import pyzipper
import time
import itertools
import string
import os
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def print_banner():
    """
    Prints the banner for the program.
    """
    print(Fore.CYAN + """
    ##############################################
    #                zL                          #
    ##############################################
    """ + Style.RESET_ALL)

def get_possible_characters(option):
    """
    Returns a string of possible characters based on user choice.
    """
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
        print(Fore.RED + "Invalid option" + Style.RESET_ALL)
        return ""

def get_valid_zip_path():
    """
    Prompts the user to enter a valid zip file path.
    """
    while True:
        zip_path = input(Fore.YELLOW + "Enter the path to the zip file: " + Style.RESET_ALL)
        if os.path.isfile(zip_path):
            return zip_path
        else:
            print(Fore.RED + "File path is not valid. Please enter a valid file path." + Style.RESET_ALL)

def get_output_folder():
    """
    Prompts the user to enter the output folder name.
    """
    output_folder = input(Fore.YELLOW + "Enter the name for the output folder (leave blank for default 'Output'): " + Style.RESET_ALL)
    if not output_folder:
        output_folder = "Output"
    return output_folder

def test_password(zip_path, password):
    """
    Tests a given password on the zip file.
    """
    try:
        with pyzipper.AESZipFile(zip_path) as zip_file:
            zip_file.extractall(pwd=password.encode('utf-8'))
        return True
    except:
        return False

def brute_force_zip(zip_path, output_folder, possible_characters, min_length, max_length):
    """
    Performs a brute-force attack on the zip file to find the password.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(Fore.GREEN + f"Output folder '{output_folder}' created successfully." + Style.RESET_ALL)
    
    start_time = time.time()
    tried_passwords = 0
    
    for length in range(min_length, max_length + 1):
        for password_tuple in itertools.product(possible_characters, repeat=length):
            password = ''.join(password_tuple)
            tried_passwords += 1
            print(f"\rTrying password: {password}", end='', flush=True)
            
            if test_password(zip_path, password):
                elapsed_time = time.time() - start_time
                print(Fore.GREEN + f"\nPassword found: {password}" + Style.RESET_ALL)
                print(Fore.GREEN + f"Passwords tried: {tried_passwords}" + Style.RESET_ALL)
                print(Fore.GREEN + f"Time taken: {elapsed_time:.2f} seconds" + Style.RESET_ALL)
                return password
            
    elapsed_time = time.time() - start_time
    print(Fore.RED + "\nPassword not found within the given length." + Style.RESET_ALL)
    print(Fore.RED + f"Passwords tried: {tried_passwords}" + Style.RESET_ALL)
    print(Fore.RED + f"Time taken: {elapsed_time:.2f} seconds" + Style.RESET_ALL)
    return None

def main():
    """
    Main function to drive the program.
    """
    print_banner()
    
    correct_password = "Update104"
    user_password = input(Fore.YELLOW + "Enter the password to start the program: " + Style.RESET_ALL)
    
    if user_password != correct_password:
        print(Fore.RED + "Incorrect password. Please contact for the correct password." + Style.RESET_ALL)
        return
    
    print(Fore.GREEN + "Password correct. Continuing program execution..." + Style.RESET_ALL)
    
    zip_path = get_valid_zip_path()
    output_folder = get_output_folder()
    
    min_length = int(input(Fore.YELLOW + "Enter the minimum password length to try: " + Style.RESET_ALL))
    max_length = int(input(Fore.YELLOW + "Enter the maximum password length to try: " + Style.RESET_ALL))
    
    print(Fore.CYAN + """
    Choose the type of characters to try in passwords:
    1: Capital letters
    2: Small letters
    3: Capital and small letters
    4: Numbers
    5: Capital letters and numbers
    6: Small letters and numbers
    7: Capital letters, small letters, and numbers
    """ + Style.RESET_ALL)
    pattern_option = int(input(Fore.YELLOW + "Enter the number corresponding to your choice: " + Style.RESET_ALL))
    
    possible_characters = get_possible_characters(pattern_option)
    
    if possible_characters:
        print(Fore.GREEN + "Starting brute-force attack..." + Style.RESET_ALL)
        brute_force_zip(zip_path, output_folder, possible_characters, min_length, max_length)
    else:
        print(Fore.RED + "Invalid character set option. Exiting program." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
