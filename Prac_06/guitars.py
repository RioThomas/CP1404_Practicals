from Prac_06.guitar import Guitar


def main():
    """Guitar Listing Program"""

    my_guitar_list = []
    print("My guitars!")
    name = str(input("Name: "))

    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))

        my_guitar = Guitar(name, year, cost)

        print("Added: {}".format(my_guitar))
        my_guitar_list.append(my_guitar)

        name = str(input("Name: "))

    my_guitar_list.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    my_guitar_list.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    print("\nThese are my guitars:")
    for i, entry in enumerate(my_guitar_list, 1):
        vintage_string = " (Vintage)" if entry.is_vintage() else ""
        print("Guitar {}: {} ({}), worth ${:,.2f}{}"
              .format(i, entry.name, entry.year, entry.cost, vintage_string))


main()
