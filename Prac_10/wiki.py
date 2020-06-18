
import wikipedia

user_input = input("\nEnter a page title or search phrase: ")

while user_input != "":

    try:
        page = wikipedia.page(user_input)
    except wikipedia.exceptions.DisambiguationError as e:
        print("\'" + user_input + "\'" + " could refer to: ")
        i = 0
        for option in e.options:
            if i == 6:
                continue
            else:
                i += 1
            print("    > {}".format(option))
        print("    > . . .")
        print("Please specify one of the above or change your query.")
    except wikipedia.exceptions.PageError as e:
        print(e)
    else:
        print("______________________________________________________________")
        print("")
        print(page.title + ":")
        print(page.summary)
        print(page.url)
        print("______________________________________________________________\n")

    user_input = input("Enter a page title or search phrase: ")
