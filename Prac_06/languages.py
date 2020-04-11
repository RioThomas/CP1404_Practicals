"""CP1404 Practical - Programming Language Class"""

from Prac_06.programming_language import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    program_list = (ruby, python, visual_basic)

    print("Dynamically typed languages:")
    for language in program_list:
        if language.is_dynamic():
            print(">" + language.name)


main()
