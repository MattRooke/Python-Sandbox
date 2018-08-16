"""This file will be for any and all R-Pi ideas"""


def main():
    user_name = input("Enter your Raspberry Pi user name:")
    user_pass = input("Enter your Raspberry Pi password:")
    if user_name != "" and user_pass != "":
        print("User Name: {}\nUser Password: {}".format(user_name, user_pass))
    while user_name == "" or user_pass == "":
        print("Please do not leave either entry blank!")
        user_name = input("Enter your Raspberry Pi user name:")
        user_pass = input("Enter your Raspberry Pi password:")
    print("User Name: {}\nUser Password: {}".format(user_name, user_pass))


main()
