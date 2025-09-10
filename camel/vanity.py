#this program prompts the user to enter a vanity license plate
#it then checks if the plate is valid according to the following rules:
#1. must start with at least two letters and end with at least 2 numbers 
#2. can only contain letters, numbers
#3. must not contain spaces, punctuation, or special characters
#4. must be between 2 and 6 characters long

def is_valid_vanity_plate(plate):
    if not (2 <= len(plate) <= 6):
        return False
    if not (plate[0:2].isalpha() and plate[-2:].isdigit()):
        return False
    for char in plate:
        if not (char.isalnum()):
            return False
    return True

def main():
    plate = input("Enter a vanity license plate: ")
    if is_valid_vanity_plate(plate):
        print("Valid vanity plate")
    else:
        print("Invalid vanity plate")
        print("Please enter a valid vanity plate.")
        main()
main()
