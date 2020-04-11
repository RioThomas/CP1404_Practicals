"""
name = "Gibson L-5 CES"
year = 1922
cost = 16035.40
"""

from Prac_06.guitar import Guitar

my_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)

print(my_guitar)
print(my_guitar.get_age())
print(my_guitar.is_vintage())
