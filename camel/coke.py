#we want to create a program that prompts user to insert coin until the reach 50 cents or more.
#if user inserts less than 50 cents, we want to keep asking them to insert more coins.
#If the user inserts more than 50 cents, we want to give them change.
#only accept coins in denominations of 1, 5, 10, 25 cents.
#give user feedback on how much they have inserted so far and how much more they need to insert.
#if user inserts invalid coin, we want to tell them it's invalid and ask them to insert a valid coin.

def main():
    total = 0
    while total < 50:
        coin = int(input("Insert coin (in cents): "))
        if coin in [1, 5, 10, 25]:
            total += coin
        else:
            print("Invalid coin. Please insert a valid coin (1, 5, 10, 25 cents).")
        if total < 50:
            print(f"You have inserted {total} cents. Please insert {50 - total} more cents.")
        if total > 50:
            print(f"Here is your change: {total - 50} cents")
        if total == 50:
                print("Thank you!")
    print("Thank you!")

main()

