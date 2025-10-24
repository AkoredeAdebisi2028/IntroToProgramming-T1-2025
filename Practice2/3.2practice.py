
def check_password():
    Genshin_password = "Arlecchino"
    submitted_password = (input("Enter your password twin\n>"))

    if Genshin_password == submitted_password:
        print("Password accepted")

    else:
        print("Try again please")
        check_password()
check_password()