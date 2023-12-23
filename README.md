PASSWORD GENERATOR
This Python script, password.py, contains a PasswordGenerator class responsible for generating random passwords with a mix of alphabetic, numeric, and symbol characters.

Password Generation Logic
The PasswordGenerator class utilizes the following logic to generate passwords:

Alphabetic Characters: Randomly selects alphabetic characters from the ASCII letters set.
Symbol Characters: Randomly selects punctuation characters from the string's punctuation set.
Numeric Characters: Randomly selects numeric digits from the string's digits set.
Combining Characters: Combines the selected characters into a single character set.
Shuffling Characters: Shuffles the combined characters using random.sample() to create a random password.

Usage
To generate a password using the PasswordGenerator class, follow these steps:

Import the PasswordGenerator class from password.py.
Create an instance of the PasswordGenerator.
Call the generate() method to obtain a randomly generated password.
from password import PasswordGenerator

# Create an instance of PasswordGenerator
password = PasswordGenerator()
# Generate a password
generated_password = password.generate()
# Output the generated password
print(generated_password) 

Configuration
The script allows customization of the password length and the number of characters from different sets by modifying the constants in the script:
ALPHABET_CHARS: Number of alphabetic characters in the password.
PUNC_CHARS: Number of punctuation characters in the password.
NUM_CHARS: Number of numeric characters in the password.
PASSWORD_LENGTH: Total length of the generated password.

# Customize the password configuration
ALPHABET_CHARS = 8
PUNC_CHARS = 4
NUM_CHARS = 2
PASSWORD_LENGTH = 14

Contribution
Contributions to improve the password generation logic or add new features are welcome. To contribute:

Fork the repository.
Make your changes.
Create a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.
