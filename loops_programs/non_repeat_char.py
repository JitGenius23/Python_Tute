# findout first non repeating letter in a string

string = "hello python"

for char in string:
    if string.count(char) == 1:
        print('first non repeat letter:', char)
        break


    


