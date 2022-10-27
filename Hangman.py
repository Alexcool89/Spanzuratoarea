

word = "bitacademy"
remaining_attempts = 3
selected_letters = []


def intro():
    """ Show intro of the Hangman game."""
    print(
        """
    Welcome to the intellectual quest known as the Hangman.
    This battle will take place between the machine represented by a silicon processor and man - the one who created the processor.
    Shave yourself, man, because you need it!!! THE BATTLE begins!\n""")


def instructions():
    """ Show instructions for the Hangman game."""
    print("\n\n")
    for e in word:
        if e in selected_letters:
            print(e),
        else:
            print("_"),
    print("\n")
    print("""You can try a completion by entering a letter.\
    It is allowed to be wrong 3 times!
    The number of chances left is:\t""",)


def final_message():
    if remaining_attempts > 0:
        print("\n Congratulations!")
    else:
        print("\n Keep trying!")


def lets_try():
    le = ""
    while not len(le) == 1:
        letter = input(
            "Write a letter that you think exists in the chosen word - hint academy:\t")
        le = letter.lower()
    return le


# main
intro()
while (remaining_attempts > 0):
    instructions()
    print(remaining_attempts)
    letter = lets_try()
    if letter in word:
        print(letter, " exists in the word you chose")
        selected_letters += [letter]
    else:
        print(letter, " does not exist in the word you chose")
        remaining_attempts -= 1
    unguessed_letters = 0
    for e in word:
        if e not in selected_letters:
            unguessed_letters += 1
    if not unguessed_letters:
        break

final_message()

input("\n\nPress <enter> to exit.")
