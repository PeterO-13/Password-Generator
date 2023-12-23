import random
import string

ALPHABET_CHARS = 8  # Number of alphabet characters in the generated password
PUNC_CHARS = 4  # Number of punctuation characters in the generated password
NUM_CHARS = 2  # Number of numeric characters in the generated password
PASSWORD_LENGTH = 14  # Total length of the password


class PasswordGenerator:
    def __init__(self):
        pass  # Initializing the PasswordGenerator class

    def generate(self):
        # Select random characters from different character sets (letters, symbols, numbers)
        letters = random.choices(list(string.ascii_letters), k=ALPHABET_CHARS)
        symbols = random.choices(list(string.punctuation), k=PUNC_CHARS)
        numbers = random.choices(list(string.digits), k=NUM_CHARS)

        # Combine the selected characters and generate a password of specified length
        password_characters = letters + symbols + numbers
        # Use random.sample to shuffle the characters and create the password
        password = "".join(random.sample(password_characters, k=PASSWORD_LENGTH))

        return password  # Return the generated password
