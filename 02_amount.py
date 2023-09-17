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
    first_mistake = True  # Flag to track the first mistake

    while True:
        print()
        quantity_response = input("So how many pizza/s are you looking to get today then? (use numbers only) ").lower()

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

        elif quantity_response in ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]:
            # Map word quantity responses to numbers
            quantity = words_to_numbers(quantity_response)
            print()
            print(f"So that's {quantity} pizza(s).")
            print()
            print("Program continues...")
            return  # Exit the function and return to the main loop

        if first_mistake:
            print()
            print("I'm sorry, I don't understand.")
            print("Oh yes, I should probably let you know, at Big Ben's Pizzeria,")
            print("we have a policy of only allowing at most, 10 pizzas per order")
            first_mistake = False  # Set the flag to False after the first mistake

        else:
            print()
            print("I'm sorry sir I don't understand what you're saying, ")
            print("I hope you find what you're looking elsewhere. Have a good day!")
            print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
            return  # Exit the function and return to the main loop


order_pizza()
