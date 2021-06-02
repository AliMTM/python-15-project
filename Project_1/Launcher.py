from Password_Validator import *
from Password_Generator import *
import subprocess

"""Welcome message"""
print("Hello, welcome to my program to create and validate your passwords please")
print("please chose what function do you need")

while True:
    """Infinity loop to make sure that user only chose 1 or 2 or quit with q """
    pressed_number = input("1- Press 1 to Create a new password \n2- Press 2 to Validate your password\n")

    if pressed_number == "1":
        """we ask for length and exclusion of ambiguous characters using infinity loop"""
        length = 0
        sc = True

        while True:
            length = input("Please Enter The length you want for the password\n")
            if length.isdigit():
                length = int(length)
                if length < 8:
                    print("Your length is less than 8 thus we automatically change it to 8")
                    length = 8
                break
            elif length.lower() == 'q':
                quit()
            else:
                print("Invalid input please only enter a Number or Q to quit")

        print("Do you want to include ambiguous characters ( { } [ ] ( ) / \ ' \" ` ~ , ; : . < > )?")

        while True:
            sc = input("Please Enter Y, N or Q to quit\n")
            if sc.lower() == "y":
                break
            elif sc.lower() == "n":
                vocab["special_character"] = " !#$%&*+-=?@^_|"
                break
            elif sc.lower() == 'q':
                quit()
            else:
                print("Invalid input")

        """we generate the password using generator function from Password_generator class"""

        for i in range(5):

            password = generator(length, sc)
            print(f"{i + 1}- {password}")

        break

    elif pressed_number == "2":
        password = input("please enter your password\n")

        """we validate the password using validation function from Password_validator class"""
        validation_percentage, advises = validation(password, True)

        """Printing the password strength"""
        print(f"Your password strength is {validation_percentage}%")

        """If the password is not perfect here are some tips"""

        if validation_percentage < 100:
            print("Here are some advises to help you improve your password")
            for advise in advises:
                print(advise)
            print("Do you want a suggested strong password ?")
            q = input("Please Enter Y or anything else to quit\n")
            if q.lower() == "y":
                passwords = []
                for i in range(5):
                    """we create a suggestion using enhance function from Password_generator class"""
                    suggested_password = enhance(password, advises)
                    """we check if the password is not already in the list"""
                    if suggested_password in passwords:
                        i -= 1
                    else:
                        passwords.append(suggested_password)
                for password in passwords:
                    print(password)
            quit()

        break

    elif pressed_number.lower() == 'q':
        quit()
    else:
        print("Invalid input please only enter a Number or Q to quit")