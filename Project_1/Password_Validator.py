"""Create a dictionary of the validations"""
passValidation = {"have a length more than 8": False, "contain upper case": False,
                  "contain lower case": False, "contain numbers": False, "contain special character": False}


def validation(password, return_suggestions=False):
    """Check the password length"""
    passValidation["have a length more than 8"] = len(password) > 7

    """Check the password letters"""
    for letter in password:
        if not passValidation["contain lower case"]:
            """Check if there is at least one letter is Lower Case"""
            if letter.islower():
                passValidation["contain lower case"] = True

        if not passValidation["contain upper case"]:
            """Check if there is at least one letter is Lower Case"""
            if letter.isupper():
                passValidation["contain upper case"] = True

        if not passValidation["contain numbers"]:
            """Check if there is at least one letter is Numbers"""
            if letter.isdigit():
                passValidation["contain numbers"] = True

        if not passValidation["contain special character"]:
            """Check if there is at least one letter is Special Character"""
            if not letter.isalnum():
                passValidation["contain special character"] = True

    """Calculating the percentage of the password strenght from the passValidation dictionary"""
    validation_percentage = 0
    percentage = 100 / len(passValidation)
    for valid in passValidation.values():
        if valid:
            validation_percentage += percentage

    """If the password is not perfect here are some tips"""
    advises = []
    if validation_percentage < 100:
        for key in passValidation.keys():
            if not passValidation[key]:
                if key == "have a length more than 8":
                    advises.append(f"your password need at least {8 - len(password)} more chars")
                else:
                    key = "doesn't " + key
                    advises.append(key)

    if return_suggestions:
        return validation_percentage, advises
    else:
        return validation_percentage

    # """Printing the password strength"""
    # print(f"Your password strength is {validation_percentage}%")
    #
    # """If the password is not perfect here are some tips"""
    # advises = []
    # if validation_percentage < 100:
    #     print("Here are some advises to help you improve your password")
    #     for key in passValidation.keys():
    #         if not passValidation[key]:
    #             advises.append(key)
    # print(validation_percentage)

