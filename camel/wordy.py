#With this program we want to create a word game.
#This game will present the user with 6 random generated letters containing at least 2 vowels.
#User must make words out of these letters.

def main ():
    #we want to add a dictionary to tell user the number of valid words they can make with the given letters.
    valid_words = ["AT", "IT", "TO", "OR", "ARE", "ART", "RAT", "TAR", "TEAR", "RATE", "EAR", "EAT", "TEA", "OAT",
                   "AIR", "TIRE", "RITE", "TIER", "AORTER", "RATIO", "ORATE", "AORTIA"]
        # fill remaining_words with all valid_words
    remaining_words = list(valid_words)

    print(f"""
    Welcome to WORD GAME!
    You will be given 6 random letters containing at least 2 vowels.
    You must make words out of these letters.
    You will get points based on the length of the word you make.
    
    Let's begin!

    Here are your letters: A, E, I, O, T, R
    """)

    while remaining_words:
        word = input("Make a word: ").upper()
        if word.lower() == 'quit':
            break
        if len(word) < 2 or len(word) > 6:
            print("Invalid word. Please make a word using the given letters (2-6 letters).")
            continue
        if word in valid_words and word in remaining_words:
            print("Valid word!")
            points = len(word)
            print("You get", points, "points!")
            remaining_words.pop(remaining_words.index(word)) #remove word from remaining_words
            print("You can make", len(remaining_words), "more valid words with the given letters.")
        if word == "OATIER":
            print("You found the special word OATIER!")
            print("You get 10 points!")
            #remove all remaining words from remaining_words
            remaining_words.clear()
            print("Za warudo! You win!")
        elif word in valid_words and word not in remaining_words:
            print("You already found that word!")
            print("You can make", len(remaining_words), "more valid words with the given letters.")
        else:
            print("Invalid word!")
            print("You get 0 points!")
            print("You can make", len(remaining_words), "more valid words with the given letters.")

        if not remaining_words:
            print("Congratulations! You found all the valid words!")

if __name__ == "__main__":
    main()

#improvement ideas:
#1. Add scoreboard to keep track of points.
#2. Add additional words to valid_words list.
#3. Randomly generate letters instead of hardcoding them.
#4. Add difficulty levels (easy, medium, hard) with different sets of letters
#5. Add a timer to limit the time user has to make words.
#6. when time is up ask user if they want to play again.
#7. Add a hint system to help user find words.
#8. add feature that shows user all possible words when they finish the game.