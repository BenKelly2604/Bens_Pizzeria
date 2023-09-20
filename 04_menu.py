# Initialize the flags
order_placed = False
order_summary = {}
menu_displayed = False
yes_synonyms = {
    "yes": ["sure", "absolutely", "okay", "fine", "yea", "yeah", "yep", "yup", "totally", "of course", "indeed",
            "mhm", "ok", "alright", "y"]
}
no_synonyms = {
    "no": ["nope", "nah", "never", "nay", "n"]
}

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


def number_to_words(num):
    units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    if 1 <= num <= 9:
        return units[num]


valid_order = False  # Initialize valid_order
consecutive_invalid_responses = 0


def menu_pizza():
    global order_placed, order_summary, menu_displayed, valid_order

    while True:
        if order_placed:
            confirmation = input("\nIs that correct? ").lower()
            if confirmation in ['yes'] + yes_synonyms.get("yes", []):
                print("\nCool, do you want any sides with that...")
                print()
                print("Program continues...")
                exit()
            elif confirmation in ['no'] + no_synonyms.get("no", []):
                print("\nSorry about that, let's try that again")
                order_summary.clear()
                order_placed = False
                menu_displayed = False
            elif confirmation == 'hangup':
                print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
                exit()
            else:
                final_confirmation = input("\nSorry, could you try that again? ").lower()
                if final_confirmation == 'yes':
                    print("\nCool, do you want any sides with that...")
                    print()
                    print("Program continues...")
                    exit()
                elif final_confirmation == 'hangup':
                    print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
                    exit()
                else:
                    print(
                        "\nSorry, I don't understand what you're trying to say here. Have a good rest of your day and "
                        "thank you for calling Ben's Pizzeria")
                    print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
                    break

        print()
        quantity_response = input("So, how many are you looking to get today then? ").lower()

        if quantity_response == "hangup":
            print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
            exit()

        if quantity_response.isdigit():
            quantity = int(quantity_response)
            if 1 <= quantity <= 10:
                print()
                if not menu_displayed:
                    # Display the menu when it's not displayed
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

                valid_order = True  # Flag to check if the order is valid

                for i in range(quantity):
                    pizza_type = None  # Initialize pizza_type for this iteration

                    while True:
                        print()
                        response = input(
                            f"What type for pizza {number_to_words(i + 1)}? (Enter a number or name): ").lower()
                        if response == 'hangup':
                            print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
                            exit()
                        if response in pizza_menu:
                            pizza_type = pizza_menu[response]
                            if pizza_type not in order_summary:
                                order_summary[pizza_type] = {"count": 0, "extra_toppings": []}
                            break
                        else:
                            print()
                            retry_response = input("Would you like to try that again? (yes/no): ").lower()

                            if retry_response == 'yes' or retry_response in yes_synonyms.get("yes", []):
                                continue

                            if retry_response == 'no' or retry_response in no_synonyms.get("no", []):
                                print("Have a good day!")
                                print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
                                return  # Exit the function if the user chooses not to retry

                            else:
                                print()
                                print("I'm sorry sir, I don't understand what you're saying, ")
                                print("I hope you find what you're looking for elsewhere. Have a good day!")
                                print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
                                return  # Exit the function for any other response

                    if response == 'hangup':
                        print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
                        exit()

                    if pizza_type is None:
                        continue  # Skip this iteration if pizza_type is None

                    pizza_count = order_summary[pizza_type]["count"]
                    order_summary[pizza_type]["count"] = pizza_count + 1

                    print()
                    if pizza_count == 0:
                        print(f"Cool, that's one {pizza_type} pizza.")
                    else:
                        print(f"Cool, that's {number_to_words(pizza_count + 1)} {pizza_type} pizzas.")
                    print()

                    # Extra Toppings Selection
                    invalid_extra_choices_count = 0  # Track consecutive invalid extra choices

                    # Inside the loop for asking extra toppings
                    options_displayed = False  # Track if the options have been displayed

                    while invalid_extra_choices_count < 2:
                        if not options_displayed:
                            print("\nSelect extra toppings (separate with commas, e.g., '1,3'):")
                            for topping_num, topping_name in extra_toppings_menu.items():
                                print(f"{topping_num}. {topping_name}")
                            options_displayed = True  # Set the flag to True after displaying the options

                        prompt = (
                            "And what are the numbers of the extra toppings you want? (or press Enter for none) "
                            if invalid_extra_choices_count == 0
                            else "\nSorry, could you try those numbers again? "
                        )

                        extra_choices = input(prompt).strip()

                        if extra_choices == "hangup":
                            print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
                            exit()

                        if not extra_choices:
                            break

                        selected_toppings = []

                        # Validate the extra choices
                        invalid_extra_choices = False
                        for topping_num in extra_choices.split(','):
                            if topping_num not in extra_toppings_menu:
                                invalid_extra_choices = True
                                invalid_extra_choices_count += 1

                        if not invalid_extra_choices:
                            for topping_num in extra_choices.split(','):
                                selected_toppings.append(extra_toppings_menu[topping_num])

                            order_summary[pizza_type]["extra_toppings"].append(selected_toppings)
                            break

                    if response == 'hangup':
                        print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
                        exit()

                    # Check if the user entered invalid extra choices twice and exit if so
                    if invalid_extra_choices_count == 2:
                        print()
                        print("I'm sorry, I don't understand what you're saying, ")
                        print("I hope you find what you're looking elsewhere. Have a good day!")
                        print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
                        return

            if valid_order:
                valid_order = False  # Reset the valid_order flag after adding pizzas

        if order_summary:
            print()
            print("Okay, so that's...")
            print()
            total_pizzas = sum([pizza_data["count"] for pizza_data in order_summary.values()])

            # Initialize a list to store individual pizza descriptions
            pizza_descriptions = []

            for pizza_type, pizza_data in order_summary.items():
                count = pizza_data["count"]
                extra_toppings_list = pizza_data["extra_toppings"]

                for _ in range(count):
                    pizza_description = f"One {pizza_type} pizza"

                    if extra_toppings_list:
                        toppings_description = ", ".join(extra_toppings_list.pop(0))
                        pizza_description += f", {toppings_description}"

                    pizza_descriptions.append(pizza_description)

            for pizza_description in pizza_descriptions:
                print(pizza_description)
            print()
            print(f"For a total of {number_to_words(total_pizzas)} pizza{'s' if total_pizzas > 1 else ''}")

            while True:
                confirmation = input("\nIs that correct? ").lower()
                if confirmation in ['yes'] + yes_synonyms.get("yes", []):
                    print("\nCool, do you want any sides with that...")
                    print()
                    print("Program continues...")
                    exit()
                elif confirmation in ['no'] + no_synonyms.get("no", []):
                    print("\nSorry about that, let's try that again")
                    order_summary.clear()
                    order_placed = False
                    menu_displayed = False
                    break
                elif confirmation == 'hangup':
                    print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
                    exit()
                else:
                    final_confirmation = input("\nSorry, I don't understand what you're trying to say here."
                                               " Please answer with 'yes' or 'no' ").lower()
                    if final_confirmation in ['yes'] + yes_synonyms.get("yes", []):
                        print("\nCool, do you want any sides with that...")
                        print()
                        print("Program continues...")
                        exit()
                    elif final_confirmation in ['no'] + no_synonyms.get("no", []):
                        print("\nSorry about that, let's try that again")
                        order_summary.clear()
                        order_placed = False
                        menu_displayed = False
                        break
                    else:
                        print()
                        print("I'm sorry, I don't understand what you're saying, I hope you find what you're "
                              "looking elsewhere. "
                              "Have a good day!")
                        print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
                        return


menu_pizza()
