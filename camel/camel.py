#Let's create a program that prompts the user for input and then changes that from camel to snake case
def main():
    camel_case = input("What's your camelCase name? ")
    snake_case = convert_to_snake_case(camel_case)
    print(f"snake_case: {snake_case}")

def convert_to_snake_case(camel_case): 
    snake_case = ""
    for char in camel_case:
        if char.isupper():
            snake_case += "_" + char.lower()
        else:
            snake_case += char
    if snake_case.startswith("_"):
        snake_case = snake_case[1:]
    return snake_case

main()  
