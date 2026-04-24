correct_username = "yussra"
correct_password = "08/21/2003"

attempts = 3

while attempts > 0:
    username = input(" Enter your username: ")
    password = input( " Enter your password: ")

    if username == correct_username and password == correct_password:
        print( " Access granted ")
        break
    else:
        attempts -= 1
        print ( attempts, " attempts remaining")

    if attempts == 0:
            print("Account locked. Please contact support.")


# This code is a simple login system that 
# checks for a correct username and password.
# The user has three attempts to enter the correct credentials 
# before the account is locked.