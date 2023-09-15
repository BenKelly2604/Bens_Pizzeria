# Initialize the flag to False
order_placed = False
order_summary = {}
menu_displayed = False  # Flag to check if the menu has been displayed

yes_synonyms = {
    "yes": ["sure", "absolutely", "okay", "fine", "yea", "yeah", "yep", "yup", "totally", "of course", "indeed",
            "mhm", "ok", "alright"]
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
    "1": "Extra cheese +$1.20 ",
    "2": "Stuffed crust +$2 ",
    "3": "Aioli +$0.50 ",
    "4": "BBQ sauce +$0.50 ",
    "5": "Tomato sauce +$0.50 ",
}

# Function to convert numbers to words


def number_to_words(num):
    units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    if 1 <= num <= 9:
        return units[num]


consecutive_invalid_responses = 0  # Track consecutive invalid responses

while True:
    if order_placed:
        confirmation = input("\nIs that correct? ").lower()
        if confirmation == 'yes' or confirmation in yes_synonyms.get("yes", []):
            print("\nCool, do you want any sides with that...")
        elif confirmation == 'no':
            print("\nSorry about that, let's try that again")
            order_summary.clear()  # Clear the order summary
            order_placed = False  # Reset the order_placed flag
        elif confirmation == 'hangup':
            print("Call ended")
            break
        else:
            final_confirmation = input("\nSorry, is that a yes or a no? ").lower()

            if final_confirmation == 'yes':
                print("\nCool, do you want any sides with that...")
            elif final_confirmation == 'hangup':
                print("Call ended")
                break
            else:
                print("\nSorry, I don't understand what you're trying to say here. Have a good rest of your day and "
                      "thank you for calling Ben's Pizzeria")
                print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")

        if confirmation == 'no' or final_confirmation == 'no':
            continue  # Continue the loop to reorder

        break  # Exit the loop if the order has been placed

    print()
    quantity_response = input("So, how many are you looking to get today then? ").lower()

    if quantity_response == "hangup":
        print("Call ended")
        break

    if quantity_response.isdigit():
        quantity = int(quantity_response)
        if 1 <= quantity <= 10:
            print()
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

            valid_order = True  # Flag to check if the order is valid

            for i in range(quantity):
                invalid_response_count = 0  # Track consecutive invalid responses for each pizza

                while True:
                    response = input(f"What type for pizza {number_to_words(i + 1)}? (Enter a number or"
                                     f" name): ").lower()
                    if response == 'hangup':
                        print("Call ended")
                        exit()
                    if response in pizza_menu:
                        pizza_type = pizza_menu[response]
                        if pizza_type not in order_summary:
                            order_summary[pizza_type] = {"count": 1, "extra_toppings": []}
                        else:
                            order_summary[pizza_type]["count"] += 1

                        pizza_count = order_summary[pizza_type]["count"]  # Get the count of the current pizza type
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

                        extra_choices = input(
                            "And what are the numbers of the extra toppings you want (or press Enter for none): ")

                        if extra_choices == "hangup":
                            print("Call ended")
                            exit()

                        if extra_choices:
                            selected_toppings = [extra_toppings_menu[topping_num] for topping_num in
                                                 extra_choices.split(',')]
                            order_summary[pizza_type]["extra_toppings"].extend(selected_toppings)

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

                            extra_choices = input(
                                "And what are the numbers of the extra toppings you want (or press Enter for none): ")
                            if extra_choices == "hangup":
                                print("Call ended")
                                exit()
                            if extra_choices:
                                selected_toppings = [extra_toppings_menu[topping_num] for topping_num in
                                                     extra_choices.split(',')]
                                order_summary[pizza_type]["extra_toppings"].extend(selected_toppings)
                            break
                        else:
                            print("hangUp")
                            exit()  # Exit the program when "hangUp" is displayed

            if valid_order:
                valid_order = False  # Reset the valid_order flag after adding pizzas

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
                    print()
                else:
                    print(f"{number_to_words(count)} {pizza_type} pizza(s)")
                    print()
            print(f"For a total of {number_to_words(total_pizzas)} pizzas")

            order_placed = True  # Set the order_placed flag to True

    else:
        print("Please enter a number between 1 and 10 for the quantity.")
        print("\nI'm sorry, I don't understand. Order canceled.")
        order_summary.clear()  # Clear the order summary
        order_placed = False  # Reset the order_placed flag
        break  # Break the loop if quantity is not valid
