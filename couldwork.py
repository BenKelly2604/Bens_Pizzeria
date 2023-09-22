# Initialize the flags
order_summary = {}

yes_synonyms = {
    "yes": ["sure", "absolutely", "okay", "fine", "yea", "yeah", "yep", "yup", "totally", "of course", "indeed",
            "mhm", "ok", "alright", "y"]
}

no_synonyms = {
    "no": ["nope", "nah", "never", "nay", "n"]
}

pizza_menu = {
    "1": ("Ham and cheese", 11),
    "2": ("Margherita", 13),
    "3": ("Pepperoni", 15),
    "4": ("Vegetarian", 14),
    "5": ("Beef and Onion", 16),
    "6": ("Meat Lovers", 17),
}

extra_toppings_menu = {
    "1": ("Extra cheese", 1.20),
    "2": ("Stuffed crust", 2.00),
    "3": ("Aioli", 0.50),
    "4": ("BBQ sauce", 0.50),
    "5": ("Tomato sauce", 0.50),
}

side_menu = {
    "1": ("Crispy Fries", 5),
    "2": ("Loaded Wedges", 6),
    "3": ("Garlic Bread", 4),
    "4": ("Vegan Garlic Bread", 5),
    "5": ("Cheesy Scrolls", 5),
    "6": ("Green salad", 4.50),
    "7": ("Orange juice", 2.50),
    "8": ("Fizzy drink", 2),
    "9": ("Iced coffee", 3),
    "10": ("Water Bottle", 1.50),
    "11": ("Chocolate Milk", 2.50),
    "12": ("Energy Drink", 3),
}


def number_to_words(num):
    units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    if 1 <= num <= 9:
        return units[num]


def display_menu(menu_dict, title):
    print(f"{title} :")
    print()
    for key, (item_name, item_price) in menu_dict.items():
        print(f"{key}. {item_name} - ${item_price:.2f}")


def get_yes_no_input(question):
    while True:
        response = input(question).lower()

        if response == 'hangup':
            print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
            exit()
        if response in ['yes'] + yes_synonyms.get("yes", []):
            return True
        elif response in ['no'] + no_synonyms.get("no", []):
            return False
        else:
            print("I'm sorry, I don't understand that. Please answer with 'yes' or 'no'.")


def name_payment():
    print()
    name_response = input("Cool, and what's the name for the pick-up? ")
    print()

    payment_response = input("And are you paying with cash or card? ")
    print()

    if payment_response == 'cash' or payment_response == 'card':
        print()
        print("Awesome,")
        print(f"Okay, {name_response}, your order will be ready in about 15-20 minutes")
        print("See you soon!")
        print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
        exit()
    else:
        final_payment_response = input("Sorry, is that cash or card that you'll be paying for the pizza with? ")

        if final_payment_response == 'cash' or final_payment_response == 'card':
            print()
            print("Awesome,")
            print(f"Okay, {name_response}, your order will be ready in about 15-20 minutes")
            print("See you soon!")
            print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
            exit()
        else:
            print()
            print("I'm very sorry, I don't understand what you're saying, ")
            print("I hope you find what you're looking for elsewhere. Have a good day!")
            print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
            exit()


def sides_order():
    print()
    if get_yes_no_input("Lastly, would you like any sides or drinks today? "):
        order_summary.clear()  # Clear order_summary for each new order
        print()
        display_menu(side_menu, "𝓢𝓲𝓭𝓮𝓼 & 𝓓𝓻𝓲𝓷𝓴𝓼")

        # Initialize some variables
        invalid_attempts = 0
        order_invalid = False

        while True:
            side_drink_response = input(
                "Awesome, just let me know what ones you want (Use 1-12 and separate "
                "with commas if getting multiple, e.g., '1,1,3,11') ").lower()

            if side_drink_response == 'hangup':
                print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
                exit()

            selected_items = side_drink_response.split(',')
            invalid_items = []

            for item in selected_items:
                if item in side_menu:
                    item_name = side_menu[item][0]
                    item_price = side_menu[item][1]
                    if item_name in order_summary:
                        order_summary[item_name][0] += 1  # Increment the quantity
                    else:
                        order_summary[item_name] = [1, item_price]  # Initialize quantity to 1
                else:
                    invalid_items.append(item)

            if invalid_items:
                invalid_attempts += 1
                print("Invalid item number(s):", ", ".join(invalid_items))
                if invalid_attempts >= 2:
                    print("You entered invalid items twice. Hanging up.")
                    order_invalid = True
                    break
                retry = get_yes_no_input("Try again? (yes/no) ")
                if not retry:
                    print("Hanging up.")
                    order_invalid = True
                    break
            else:
                break

        if order_invalid:
            return

        # Print the order summary
        if order_summary:
            print()
            print("Okay, you selected the following sides and drinks:")
            for item, (quantity, price) in order_summary.items():
                quantity_words = number_to_words(quantity)
                print(quantity_words + " " + item)
            print()
            total_items = sum([item[0] for item in order_summary.values()])
            total_price = sum([item[0] * item[1] for item in order_summary.values()])
            print(f"For a total of {number_to_words(total_items)} sides/drinks")
            print(f"Total price: ${total_price:.2f}")

            while True:
                confirmation = get_yes_no_input("\nIs that correct? ")
                if confirmation:
                    name_payment()
                else:
                    print("\nSorry about that, let's try that again")
                    order_summary.clear()
                    break


def menu_pizza():
    global order_summary

    while True:
        print()
        quantity_response = input("So, how many pizzas are you looking to get today? ").lower()

        if quantity_response == "hangup":
            print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
            exit()

        if quantity_response.isdigit():
            quantity = int(quantity_response)
            if 1 <= quantity <= 10:
                print()
                display_menu(pizza_menu, "𝓜𝓮𝓷𝓾")

                # Initialize some variables
                total_cost = 0.0  # Initialize the total cost as a float

                for i in range(quantity):
                    while True:
                        print()
                        response = input(
                            f"What type of pizza {number_to_words(i + 1)} would you like? (Enter a "
                            f"number or name): ").lower()
                        if response == 'hangup':
                            print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
                            exit()
                        if response in pizza_menu:
                            pizza_type = response  # Store pizza type as the entered value
                            if pizza_type not in order_summary:
                                order_summary[pizza_type] = {"count": 0, "extra_toppings": []}
                            break
                        elif any(pizza_name[0].lower() == response for pizza_name in pizza_menu.values()):
                            # Check if the entered text matches any pizza name
                            for key, value in pizza_menu.items():
                                if value[0].lower() == response:
                                    pizza_type = key
                                    if pizza_type not in order_summary:
                                        order_summary[pizza_type] = {"count": 0, "extra_toppings": []}
                                    break
                            break
                        else:
                            print()
                            print("I'm sorry, I don't understand what you're trying to say.")
                            print()
                            retry_response = get_yes_no_input("Would you like to try that again? ")
                            if not retry_response:
                                print("Have a good day!")
                                print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
                                exit()

                    if response == 'hangup':
                        exit()

                    pizza_count = order_summary[pizza_type]["count"]
                    order_summary[pizza_type]["count"] = pizza_count + 1

                    print()
                    if pizza_count == 0:
                        print(f"Great! That's one {pizza_menu[pizza_type][0]} pizza.")
                    else:
                        print(f"Great! That's {number_to_words(pizza_count + 1)} {pizza_menu[pizza_type][0]} pizzas.")

                    # Extra Toppings Selection
                    invalid_extra_choices_count = 0  # Track consecutive invalid extra choices
                    print()
                    display_menu(extra_toppings_menu, "Extra Toppings")  # Display the toppings menu once
                    extra_toppings_selected = False  # Flag to track if extra toppings have been selected

                    while True:
                        print()
                        if not extra_toppings_selected:
                            extra_choices = input(
                                "What extra toppings would you like for this pizza? (Enter "
                                "toppings separated by commas or press Enter for none): ").strip().lower()

                            if extra_choices == "hangup":
                                print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
                                exit()

                            if extra_choices == "":
                                # User entered no extra toppings, break out of the loop
                                break  # Add this line to break out of the loop

                            selected_toppings = []

                            # Validate the extra choices
                            invalid_extra_choices = False
                            for topping_num in extra_choices.split(','):
                                if topping_num not in extra_toppings_menu:
                                    invalid_extra_choices = True
                                    invalid_extra_choices_count += 1
                                    break

                            if not invalid_extra_choices:
                                for topping_num in extra_choices.split(','):
                                    topping_info = extra_toppings_menu[topping_num]
                                    selected_toppings.append(topping_info[0])  # Extract the topping name
                                    # Add the price of extra toppings to the total_cost
                                    total_cost += topping_info[1]

                                order_summary[pizza_type]["extra_toppings"].append(selected_toppings)
                                extra_toppings_selected = True  # Set the flag to indicate toppings are selected

                        else:
                            break  # If no extra toppings were added for the pizza, exit the loop

                # Calculate the total cost of pizzas and extra toppings
                total_pizza_cost = 0.0  # Initialize the total pizza cost as a float

                for pizza_type, pizza_data in order_summary.items():
                    count = pizza_data["count"]
                    extra_toppings_list = pizza_data["extra_toppings"]
                    pizza_price = pizza_menu[pizza_type][1]  # Get the base pizza price

                    for _ in range(count):
                        pizza_description = f"One {pizza_menu[pizza_type][0]} pizza"

                        if extra_toppings_list:
                            toppings_description = ", ".join(extra_toppings_list.pop(0))
                            pizza_description += f" with {toppings_description}"

                        # Calculate the cost for the current pizza and add it to the total_pizza_cost
                        total_pizza_cost += pizza_price  # Add base pizza price
                        if extra_toppings_list:
                            total_pizza_cost += sum(extra_toppings_menu[topping][1] for
                                                    topping in extra_toppings_list[0])

                print()
                for pizza_type, pizza_data in order_summary.items():
                    count = pizza_data["count"]
                    print(f"{number_to_words(count)} {pizza_menu[pizza_type][0]} pizza{'s' if count > 1 else ''}")
                print()
                print(f"For a total of {number_to_words(quantity)} pizza{'s' if quantity > 1 else ''}")
                print()
                print(f"Total cost for pizzas: ${total_pizza_cost:.2f}")

                if total_cost > 0:
                    print(f"Total cost for extra toppings: ${total_cost:.2f}")

                while True:
                    confirmation = get_yes_no_input("\nIs that correct? ")
                    if confirmation:
                        sides_order()
                    else:
                        print("\nSorry about that, let's try that again")
                        order_summary.clear()
                        break

        else:
            print()
            print("I'm sorry, I don't understand what you're saying.")
            print("I hope you find what you're looking for elsewhere. Have a good day!")
            print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
            exit()

        if order_summary:
            print()
            print("Okay, so that's...")
            print()
            total_pizzas = sum([pizza_data["count"] for pizza_data in order_summary.values()])

            # Initialize a list to store individual pizza descriptions
            pizza_descriptions = []

            total_pizza_cost = 0.0  # Initialize the total pizza cost as a float

            for pizza_type, pizza_data in order_summary.items():
                count = pizza_data["count"]
                extra_toppings_list = pizza_data["extra_toppings"]
                pizza_price = pizza_menu[pizza_type][1]  # Get the base pizza price

                for _ in range(count):
                    pizza_description = f"One {pizza_menu[pizza_type][0]} pizza"

                    if extra_toppings_list:
                        toppings_description = ", ".join(extra_toppings_list.pop(0))
                        pizza_description += f" with {toppings_description}"

                    pizza_descriptions.append(pizza_description)

                    # Calculate the cost for the current pizza and add it to the total_pizza_cost
                    total_pizza_cost += pizza_price  # Add base pizza price
                    if extra_toppings_list:
                        total_pizza_cost += sum(extra_toppings_menu[topping][1] for topping in extra_toppings_list[0])

            print()
            for pizza_description in pizza_descriptions:
                print(pizza_description)
            print()
            print(f"For a total of {number_to_words(total_pizzas)} pizza{'s' if total_pizzas > 1 else ''}")
            print(f"Total cost: ${total_pizza_cost:.2f}")

            while True:
                confirmation = get_yes_no_input("\nIs that correct? ")
                if confirmation:
                    sides_order()
                else:
                    print("\nSorry about that, let's try that again")
                    order_summary.clear()
                    break


def sides_order():
    global order_summary  # Add this line to indicate you're modifying the global variable
    while True:
        print()
        yes_no_response = input("Lastly, would you like any sides or drinks today? ").lower()

        if yes_no_response == "hangup":
            print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
            exit()
        if yes_no_response == 'no' or yes_no_response in no_synonyms.get("no", []):
            print()
            name_payment()

        if yes_no_response == 'yes' or yes_no_response in yes_synonyms.get("yes", []):
            order_summary = {}  # Clear order_summary for each new order
            display_menu(side_menu, "𝓢𝓲𝓭𝓮𝓼 & 𝓓𝓻𝓲𝓷𝓴𝓼")

            # Initialize some variables
            invalid_attempts = 0
            order_invalid = False

            while True:
                print()
                side_drink_response = input(
                    "Awesome, just let me know what ones you want (Use 1-12 and separate "
                    "with commas if getting multiple, e.g., '1,1,3,11') ").lower()

                if side_drink_response == 'hangup':
                    print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
                    exit()

                selected_items = side_drink_response.split(',')
                invalid_items = []

                for item in selected_items:
                    if item in side_menu:
                        item_name = side_menu[item][0]
                        item_price = side_menu[item][1]
                        if item_name in order_summary:
                            order_summary[item_name][0] += 1  # Increment the quantity
                        else:
                            order_summary[item_name] = [1, item_price]  # Initialize quantity to 1
                    else:
                        invalid_items.append(item)

                if invalid_items:
                    invalid_attempts += 1
                    print("Invalid item number(s):", ", ".join(invalid_items))
                    if invalid_attempts >= 2:
                        print("You entered invalid items twice. Hanging up.")
                        order_invalid = True
                        break
                    retry = get_yes_no_input("Try again? ")
                    if not retry:
                        print("Hanging up.")
                        order_invalid = True
                        break
                else:
                    break

            if order_invalid:
                break

            # Print the order summary
            if order_summary:
                print()
                print("Okay, you selected the following sides and drinks:")
                for item, (quantity, price) in order_summary.items():
                    quantity_words = number_to_words(quantity)
                    print(quantity_words + " " + item)
                print()
                total_items = sum([item[0] for item in order_summary.values()])
                total_price = sum([item[0] * item[1] for item in order_summary.values()])
                print(f"For a total of {number_to_words(total_items)} items")
                print(f"Total price: ${total_price:.2f}")

                while True:
                    confirmation = get_yes_no_input("\nIs that correct? ")
                    if confirmation:
                        name_payment()
                    else:
                        print("\nSorry, let's try that again")
                        order_summary.clear()
                        break


def main():
    print("𝓦𝓮𝓵𝓬𝓸𝓶𝓮 𝓽𝓸 𝓑𝓲𝓰 𝓑𝓮𝓷'𝓼 𝓟𝓲𝔃𝔃𝓮𝓻𝓲𝓪!")

    while True:
        print()
        order_response = get_yes_no_input("Would you like to order some pizza today? ")

        if order_response is None:
            print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
            exit()

        if order_response:
            menu_pizza()
        else:
            print()
            order_response = get_yes_no_input("I'm sorry, I don't understand what you're saying. "
                                              "Is that a yes or a no? ")

            if order_response is None:
                print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
                exit()

            if order_response:
                menu_pizza()
            else:
                print()
                print("I'm sorry, I don't understand what you're saying. I hope you find what you're looking "
                      "for elsewhere. Have a good day!")
                print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
                exit()


if __name__ == "__main__":
    main()
