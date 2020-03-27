"""
CP1404 Practical
Hexadecimal Colours
"""

COLOUR_NAMES = {"red": "#ff0000", "blue": "#0000ff", "green": "", "yellow": "#ffff00",
                "violet": "#ee82ee", "orange": "#ffa500", "pink": "#ffc0cb"}


colour_code = input("Enter a colour: ").lower()
while colour_code != "":
    if colour_code in COLOUR_NAMES:
        print(COLOUR_NAMES[colour_code])
    else:
        print("Invalid colour code.")
    colour_code = input("Enter a colour: ").lower()
