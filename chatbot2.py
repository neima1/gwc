def main():
    while(True):

        choice = input("Press 1 to read a poem, 2 to see whats for dinner, 3 to play hangman, 4 to exit\n")
        if choice == '1':
            poem()
        elif choice == '2':
            dinner()
        elif choice == '3':
            hangman()
        else:
            print("Bye!")
            exit()

def poem():
    print("Raindrops on this page. Wind blows my paper away, Oh crap! I need that...")

def dinner():
    import random

    main_courses = ["spaghetti", "hamburger", "steak", "tacos"]
    sides = ["fries", "veggies", "fruit", "bread"]
    desserts = ["ice cream", "pie", "cake", "cookies"]

    full_meal = random.choice(main_courses) + " , "+random.choice(sides) + " , "+random.choice(desserts)
    print(full_meal)


def hangman():
    from random import choice

    word = choice(["lemonade"])

    guessed = []
    wrong = []

    tries = 7

    while tries > 0:

        out = ""
        for letter in word:
            if letter in guessed:
                out = out + letter
            else:
                out = out + "_"

        if out == word:
            break

        print("Guess the word:", out)
        print(tries, "chances left")

        guess = input()

        if guess in guessed or guess in wrong:
            print("Already guessed", guess)
        elif guess in word:
            print("Yay")
            guessed.append(guess)
        else:
            print("Nope")
            tries = tries - 1
            wrong.append(guess)

        print()

    if tries:
        print("You guessed", word)
    else:
        print("You didn't get", word)

main()
