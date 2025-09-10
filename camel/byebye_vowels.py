#this program prompts the user for a phrase and omits the vowels
#it then prints the phrase without vowels
def main():
    phrase = input("Enter a phrase: ")
    new_phrase = ""
    vowels = "aeiouAEIOU"
    for letter in phrase:
        if letter not in vowels:
            new_phrase += letter
    print("Phrase without vowels:", new_phrase)

main()