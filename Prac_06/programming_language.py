"""CP1404 Practical - Programming Language Class"""


class ProgrammingLanguage:

    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Check if typing type is dynamic"""
        return self.typing == "Dynamic"

    def __str__(self):
        """Output all data in sentence."""
        return "{}, {} Typing, reflection={}, First appeared in {}"\
            .format(self.name, self.typing, self.reflection, self.year)
