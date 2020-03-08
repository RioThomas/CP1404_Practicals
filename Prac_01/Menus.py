
user_name = input("What's your name? ")


def menu():
    print("(H)ello \n(G)oodbye \n(Q)uit \n".format(user_name))
    choice = input("> ")
    if choice == "Q":
        print("\nquitting... \n")
    elif choice == "H":
        print("Hello {}".format(user_name))
        menu()
    elif choice == "G":
        print("Goodbye {}!".format(user_name))
        menu()
    else:
        print("Invalid Input")


menu()

# get name
# display menu
# get choice
# while choice != Q
#    if choice == H
#        display "hello" name
#    else if choice == G
#        display "goodbye" name
#    else
#        display invalid message
#    display menu
#    get choice
# display finished message
