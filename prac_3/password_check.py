password_input = input("Please enter password:")
while len(password_input) < 10:
    print("please enter a longer password. Must be more than 10 Characters")
    password_input = input("please enter password:")
password_hidden = '*' * len(password_input)
print(password_hidden, end=' ')