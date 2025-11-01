name = input("Type your name: ")
print("Welcome,", name, "to this adventure!")

answer = input("You are on dirt road, " \
"it has come to an end and you can go left or right." \
"Which way would you like to go?").lower()

if answer == "left":
    answer = input("You come to river, you can walk around it" \
    "or swim across? Type walk to walk around " \
    "and swim to swim across: ")

    if answer == "swim":
        print("You swam across and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost.")
    else:
        print("Not a valid option. You lose.")

elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly," \
    "do you want to across it or")
else:
    print("Not valid option. You lose.")
