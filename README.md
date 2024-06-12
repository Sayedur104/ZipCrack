# ZIP File Password Crack

This script attempts to recover the password of a ZIP file using a brute-force attack method. It supports various character sets and allows the user to specify the minimum and maximum password lengths to try.

## Features

- Supports AES encrypted ZIP files.
- Allows the user to choose different character sets for the brute-force attack.
- Automatically creates an output folder if it doesn't exist.
- Provides detailed feedback on the progress of the brute-force attack.
- Interactive user interface with colorful prompts and messages.

## Requirements

- Python 3.6+
- `pyzipper` module

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Sayedur104/ZipCrack.git
    ```
2. Navigate to the project directory:
    ```bash
    cd ZipCrack
    ```
3. Install the required dependencies:
    ```bash
    pip install pyzipper
    ```

## Usage

1. Run the script:
    ```bash
    python3 Crack.py
    ```

2. Follow the on-screen prompts:
    - Enter the password to start the program (`For Password Contact me https://t.me/rakib009875`).
    - Enter the path to the ZIP file.
    - Enter the minimum and maximum password lengths to try.
    - Choose the type of characters to include in the passwords:
        - 1: Capital letters
        - 2: Small letters
        - 3: Capital and small letters
        - 4: Numbers
        - 5: Capital letters and numbers
        - 6: Small letters and numbers
        - 7: Capital letters, small letters, and numbers
    - Enter the name for the output folder (leave blank for default 'Output').

## Example

```bash
##############################################
#                SAYEDUR 104                 #
##############################################

Enter the password to start the program: Update104
Password correct. Continuing program execution...

Enter the path to the zip file: /path/to/your/zipfile.zip
Enter the minimum password length to try: 1
Enter the maximum password length to try: 4

Choose the type of characters to try in passwords:
1: Capital letters
2: Small letters
3: Capital and small letters
4: Numbers
5: Capital letters and numbers
6: Small letters and numbers
7: Capital letters, small letters, and numbers
Enter the number corresponding to your choice: 3
Enter the name for the output folder (leave blank for default 'Output'): MyOutput

Starting brute-force attack...

Trying password: abCd
...
Password found: abCd
Passwords tried: 4567
Time taken: 123.45 seconds

Password recovery successful.
