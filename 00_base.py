# Define the yes_synonyms dictionary at the global level
yes_synonyms = {
    "yes": ["sure", "absolutely", "okay", "fine", "yea", "yeah", "yep", "yup", "totally", "of course",
            "indeed", "mhm", "y",
            "ok", "alright"]
}

# Define the no_synonyms dictionary at the global level
no_synonyms = {
    "no": ["nah", "nope", "never", "n", "nay", "negative", ]
}


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


def get_quantity():
    consecutive_invalid_responses = 0  # Track consecutive invalid responses
    while True:
        quantity_response = input("So how many pizzas are you looking to get today then? ").lower()
        print()

        if quantity_response == 'hangup':
            print("*Call ended*")
            exit()  # Exit the program

        quantity = words_to_numbers(quantity_response)

        if 1 <= quantity <= 10:
            return quantity

        if quantity_response.isdigit() and 1 <= int(quantity_response) <= 10:
            return int(quantity_response)

        consecutive_invalid_responses += 1
        if consecutive_invalid_responses == 2:
            print()
            print("I'm very sorry but I don't understand what you're trying to say, I hope you"
                  " find what you're looking elsewhere. "
                  "Have a good day!")
            print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
            exit()

        print()
        print("Please enter a number between 1 and 10 or one of the words: one, two, three, ..., ten.")
        print()


def order_pizza():
    order_placed = False  # Initialize the flag to False
    order_summary = {}
    menu_displayed = False  # Flag to check if the menu has been displayed

    pizza_menu = {
        "1": "Ham and cheese",
        "2": "Margherita",
        "3": "Pepperoni",
        "4": "Vegetarian",
        "5": "Beef and Onion",
        "6": "Meat Lovers",
        "ham and cheese": "Ham and cheese",
        "margherita": "Margherita",
        "pepperoni": "Pepperoni",
        "vegetarian": "Vegetarian",
        "beef and onion": "Beef and Onion",
        "meat lovers": "Meat Lovers",
    }

    extra_toppings_menu = {
        "1": "Extra cheese +$1.20",
        "2": "Stuffed crust +$2",
        "3": "Aioli +$0.50",
        "4": "BBQ sauce +$0.50",
        "5": "Tomato sauce +$0.50",
    }

    # Function to convert numbers to words
    def number_to_words(num):
        units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

        if 1 <= num <= 9:
            return units[num]

    consecutive_invalid_responses = 0  # Track consecutive invalid responses
    valid_order = False  # Initialize valid_order flag

    while True:
        if order_placed:
            confirmation = input("\nIs that correct? ").lower()
            if confirmation == 'yes' or confirmation in yes_synonyms.get("yes", []):
                print("\nCool, do you want any sides with that...")
                break  # Exit the loop if the order is confirmed
            elif confirmation == 'no' or confirmation in no_synonyms.get("no", []):
                print("\nSorry about that, let's try that again")
                order_summary.clear()  # Clear the order summary
            elif confirmation == 'hangup':
                print("Call ended")
                break
            else:
                final_confirmation = input("\nSorry, is that a yes or a no? ").lower()

                if final_confirmation == 'yes' or final_confirmation in yes_synonyms.get("yes", []):
                    print("\nCool, do you want any sides with that...")
                    break  # Exit the loop if the order is confirmed
                elif final_confirmation == 'hangup':
                    print("Call ended")
                    break
                else:
                    print("\nSorry, I don't understand what you're trying to say here. Have a good rest"
                          " of your day and "
                          "thank you for calling Ben's Pizzeria")
                    print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
                    break  # Exit the loop if there's an unrecognized response

        print()
        quantity = get_quantity()

        if not menu_displayed:
            print()
            print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━┑")
            print("┃        𝓜𝓮𝓷𝓾             ┃")
            print("┃        ▔▔▔▔▔▔            ┃")
            print("┃ 1. Ham and cheese   $12  ┃")
            print("┃ 2. Margherita       $12  ┃")
            print("┃ 3. Pepperoni        $12  ┃")
            print("┃ 4. Vegetarian       $13  ┃")
            print("┃ 5. Beef and Onion   $13  ┃")
            print("┃ 6. Meat Lovers      $14  ┃")
            print("┖━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
            menu_displayed = True

        for i in range(quantity):
            while True:
                response = input(f"What type for pizza {number_to_words(i + 1)}? (Enter a number or"
                                 f" name): ").lower()

                if response == 'hangup':
                    print("Call ended")
                    exit()  # Exit the program

                if response in pizza_menu:
                    pizza_type = pizza_menu[response]
                    if pizza_type not in order_summary:
                        order_summary[pizza_type] = {"count": 1, "extra_toppings": []}
                    else:
                        order_summary[pizza_type]["count"] += 1

                    pizza_count = order_summary[pizza_type]["count"]  # Get the count of the current pizza
                    print()
                    if pizza_count == 1:
                        print(f"Cool, that's one {pizza_type} pizza.")
                    else:
                        print(f"Cool, that's {number_to_words(pizza_count)} {pizza_type} pizzas.")
                    print()

                    # Extra Toppings Selection
                    print("\nSelect extra toppings (separate with commas, e.g., '1,3'):")
                    for topping_num, topping_name in extra_toppings_menu.items():
                        print(f"{topping_num}. {topping_name}")

                    while True:
                        extra_choices = input(
                            "And what are the numbers of the extra toppings you want (or press Enter for none): ")

                        if extra_choices == "hangup":
                            print("Call ended")
                            exit()

                        if not extra_choices:
                            break  # No extra toppings, exit the loop

                        selected_toppings = []
                        invalid_toppings = []

                        for topping_num in extra_choices.split(','):
                            if topping_num in extra_toppings_menu:
                                selected_toppings.append(extra_toppings_menu[topping_num])
                            else:
                                invalid_toppings.append(topping_num)

                        if invalid_toppings:
                            print("Invalid topping numbers. Please select from 1 to 5.")
                            continue  # Ask again for valid toppings

                        order_summary[pizza_type]["extra_toppings"].extend(selected_toppings)
                        break  # Valid input, exit the loop

                    break  # Exit the loop when a valid response is provided
                else:
                    print()
                    last_chance_response = input(
                        "I'm sorry, I don't understand. Could you try that again? ").lower()

                    if last_chance_response == "hangup":
                        print("Call ended")
                        exit()

                    if last_chance_response in pizza_menu:
                        pizza_type = pizza_menu[last_chance_response]
                        if pizza_type not in order_summary:
                            order_summary[pizza_type] = {"count": 1, "extra_toppings": []}
                        else:
                            order_summary[pizza_type]["count"] += 1
                        print(f"Cool, that's one {pizza_type} pizza.")
                        print()

                        # Extra Toppings Selection
                        print("\nSelect extra toppings (separate with commas, e.g., '1,3'):")
                        for topping_num, topping_name in extra_toppings_menu.items():
                            print(f"{topping_num}. {topping_name}")

                        while True:
                            extra_choices = input(
                                "And what are the numbers of the extra toppings you want (or press Enter for none): ")
                            if extra_choices == "hangup":
                                print("Call ended")
                                exit()
                            if not extra_choices:
                                break
                            selected_toppings = []
                            invalid_toppings = []

                            for topping_num in extra_choices.split(','):
                                if topping_num in extra_toppings_menu:
                                    selected_toppings.append(extra_toppings_menu[topping_num])
                                else:
                                    invalid_toppings.append(topping_num)

                            if invalid_toppings:
                                print("Invalid topping numbers. Please select from 1 to 5.")
                                continue

                            order_summary[pizza_type]["extra_toppings"].extend(selected_toppings)
                            break
                        break
                    else:
                        print("hangUp")
                        exit()

        # Print the order summary
        if order_summary:
            total_pizzas = sum([pizza_data["count"] for pizza_data in order_summary.values()])
            # Calculate the total count of all pizzas
            print("\nOkay, so that's")
            for pizza_type, pizza_data in order_summary.items():
                count = pizza_data["count"]
                extra_toppings = pizza_data["extra_toppings"]
                if extra_toppings:
                    toppings_description = ", ".join(extra_toppings)
                    print(f"{number_to_words(count)} {pizza_type} pizza(s) with {toppings_description}")
                else:
                    for _ in range(count):
                        print(f"{number_to_words(1)} {pizza_type} pizza")
                    print()
            print(f"For a total of {number_to_words(total_pizzas)} pizzas")

            order_placed = True  # Set the order_placed flag to True

        else:
            print("Please enter a number between 1 and 10 for the quantity.")
            print("\nI'm sorry, I don't understand. Order canceled.")
            order_summary.clear()  # Clear the order summary
            break  # Break the loop if quantity is not valid

while True:
    print("(If you want to hang up, simply say 'hangup')")
    print()
    response = input("Hello, thank you for calling Ben's Pizzeria. Would you like to order some pizza? (yes/no): "
                     "").lower()

    if response == 'hangup':
        print("*Call ended*")
        break

    if response == 'yes' or response in yes_synonyms.get("yes", []):
        order_pizza()
        break

    elif response == 'no' or response in no_synonyms.get("no", []):
        print()
        followup_response = input(" Please don't be like that, I'm a minimum wage worker, I don't have"
                                  " time for prank calls. "
                                  "Do you want a pizza, yes or no? ").lower()
        if followup_response == 'hangup':
            print("*Call ended*")
            break
        if followup_response == 'yes' or followup_response in yes_synonyms.get("yes", []):
            order_pizza()
            break
        elif followup_response == 'no' or followup_response in no_synonyms.get("no", []):
            print()
            print("Have a good day!")
            print("*Call ended*")
            break
        else:
            print("Have a good day!")
            print("*Call ended*")
            break

    else:
        print()
        yes_or_no_response = input("Sorry, is that a yes or a no? ").lower()
        if yes_or_no_response == 'hangup':
            print("*Call ended*")
            break
        if yes_or_no_response == 'yes' or yes_or_no_response in yes_synonyms.get("yes", []):
            order_pizza()
            break
        elif yes_or_no_response == 'no' or yes_or_no_response in no_synonyms.get("no", []):
            print()
            print("Please don't waste my time, Have a good rest of your day.")
            print("*Call ended*")
            break
        else:
            print()
            print("I'm sorry, I don't understand what you're saying. "
                  "I hope you find what you're looking for elsewhere. Have a good day!")
            print("*Call ended*")
            break
