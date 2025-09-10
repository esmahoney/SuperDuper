#this program prompts the user to enter a fruit
# outputs the number of calories in one portion.
#then asks the user how many portions they ate
# and outputs the total number of calories consumed.
#if the fruit is not in the list, it outputs "Unknown fruit"
#then prompts the user to enter a fruit again
def main():
    while True:
        fruit = input("Enter a fruit: ")
        calories = get_calories(fruit)
        if calories != -1:
            print(f"A portion of {fruit} has {calories} calories.")
            portions = int(input("How many portions did you eat? "))
            total_calories = calories * portions
            print(f"You consumed a total of {total_calories} calories.")
            break
        else:
            print("Unknown fruit.")
            continue

def get_calories(fruit):
    fruit_calories = {
        "apple": 130,
        "banana": 110,
        "orange": 80,
        "grapes": 90,
        "strawberry": 49,
        "avocado": 50,
        "cantaloupe": 50,
        "grapefruit": 60,
        "kiwifruit": 90,
        "peach": 60,
        "pear": 100,
        "pineapple": 50,
        "plums": 70,
        "raspberries": 30,
        "sweet cherries": 100,
        "tangerine": 50,
        "watermelon": 80,
        "blueberries": 85,
        "strawberries": 50,
        "honeydew melon": 50,
        "mango": 135,
        "nectarine": 60,
        "pomegranate": 105,
        "lemon": 15,
        "lime": 20

    }
    return fruit_calories.get(fruit.lower(), -1)

main()