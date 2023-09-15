def words_to_numbers(word):
    # Define a dictionary to map words to numbers
    word_to_number = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
    }
    # Try to convert the word to a number, default to 0 if not found
    return word_to_number.get(word.lower(), 0)


def order_pizza():
    while True:
        print()
        quantity_response = input("So how many are you looking to get today then? ").lower()

        if quantity_response.isdigit():
            quantity = int(quantity_response)
            if 1 <= quantity <= 10:
                print()
                print(f"So that's {quantity_response} pizza(s).")
                print()
                print("Program continues...")
                return  # Exit the function and return to the main loop

        if quantity_response == 'hangup':
            print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
            return  # Exit the function and return to the main loop

        elif quantity_response.lower() in ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
                                           "ten"]:
            # Map word quantity responses to numbers
            quantity = words_to_numbers(quantity_response)
            print()
            print(f"So that's {quantity} pizza(s).")
            print()
            print("Program continues...")
            return  # Exit the function and return to the main loop

        print()
        print("I'm sorry, I don't understand.")
        print(
            "Oh yes, I should probably let you know that unfortunately, at Big Ben's Pizzeria, we have a policy of "
            "only doing 10 pizzas per order max")


order_pizza()
