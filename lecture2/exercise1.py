

password = input('Enter your password:')


if len(password) >= 8:

    isdigit = False
    islower = False
    isupper = False

    for char in password:  # h1P
        if char.isdigit():
            isdigit = True
        if char.islower():
            islower = True
        if char.isupper():
            isupper = True

    if isupper and islower and isdigit:
        print('Your password is valid!')
    else:
        print('Your password is invalid!')

else:
    print('Your password is less than 8 characters')







