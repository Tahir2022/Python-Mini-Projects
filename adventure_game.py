name = input("Type your name: ")
print("Welcome,", name, "to this adventure!")

answer = input("You are on dirt road, " \
"it has come to an end and you can go left or right." \
"Which way would you like to go?").lower()

if answer == "left":

elif answer == "right":

else:
    print("Not valid option. You lose.")
