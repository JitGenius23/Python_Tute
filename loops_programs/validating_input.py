# Keep Asking the user for input until the user enter a number between 1 and 10

while(True):
    user_input = int(input('enter a number between 1 and 10:'))
    if (user_input >=1 and user_input <=10):
        print("correct choice 😃")
        break
    else:
        print("Wrong choice! try again.")