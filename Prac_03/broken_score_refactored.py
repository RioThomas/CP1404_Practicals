
# CP1404/CP5632 - Practical
# Broken program to determine score status
import random


def main():
    while True:
        score = input("Enter score or 'r' for a random score: ")
        if score == "r":
            score = random.randint(1, 100)
            print("Score = " + str(score))

        score = float(score)
        convert_score_to_grade(score)


def convert_score_to_grade(score):
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Pass")
    else:
        print("Bad")


main()
