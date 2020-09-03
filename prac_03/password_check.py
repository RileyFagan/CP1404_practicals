
def main():
    get_password = input("Please enter password:")
    while len(get_password) < 10:
        print("please enter a longer password. Must be more than 10 Characters")
        get_password = input("please enter password:")
    password_hidden = '*' * len(get_password)
    print(password_hidden, end=' ')


main()
