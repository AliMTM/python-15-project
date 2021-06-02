import random
import string
from Password_Validator import *

"""initializing a dictionary for the vocab that we are going to use for the password"""
vocab = {"lowercase_letters": string.ascii_lowercase, "uppercase_letters": string.ascii_uppercase,
         "digits": string.digits, "special_character": string.punctuation + " "}


def generator(length, sc, password=""):
    """
    :param length: is the length required for the password
    :param sc: are you allowing us to use ambiguous characters {}[]()/\'"`~,;:.<>
    """

    if not sc:
        """exclude ambiguous characters from special characters"""
        vocab["special_character"] = " !#$%&*+-=?@^_|"

    """were are going to save 5 passwords to provide more choices"""

    for j in range(length):
        """ three operations happens here
        first, random.choice(list(vocab.keys())) chose a random key
        second, vocab[...] bring up the values of that key
        finally, random.choice(...) chose a value from that vocab"""
        l = random.choice(vocab[random.choice(list(vocab.keys()))])
        password += l

    """we check the if the password is 100% valid if not we repeat the progress"""

    validation_percentage, advises = validation(password, True)
    if validation_percentage < 100:
        password = enhance(password, advises)

    return password


def enhance(password, advises):
    """
    :param password: the password that we want to improve
    :param advises: to avoid checking everything again
    :return: the improved password
    """

    """we copy the dict so the main vocab doesn't change"""
    new_vocab = vocab.copy()

    """Check the advises to optimize the generation of the new password
        I did this by removing unneeded vocab"""
    if "doesn't contain lower case" not in advises:
        new_vocab.pop("lowercase_letters")
    if "doesn't contain upper case" not in advises:
        new_vocab.pop("uppercase_letters")
    if "doesn't contain numbers" not in advises:
        new_vocab.pop("digits")
    if "doesn't contain special character" not in advises:
        new_vocab.pop("special_character")

    """here we are adding the missing chars in a random position"""
    for key in new_vocab.keys():

        r = random.choice(vocab[key])
        x = random.randint(0, len(password) - 1)

        if 0 < x < len(password) - 1:

            pass1 = password[0:x]
            pass2 = password[x:]

            password = pass1 + r + pass2

        elif x == 0:
            """if the position was first no need to split"""
            password = r + password

        else:
            """if the position was last no need to split"""
            password = password + r

    if len(password) < 8:
        """if the password still less than 8 chars long"""

        password = generator(8 - len(password), False, password)

    return password