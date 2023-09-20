def number_to_words(num):
    units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    if 1 <= num <= 9:
        return units[num]

# Function for name and payment


def name_payment():
    while True:
        print()
        name_response = input("Cool, and what's the name for the pick-up? ")
        print()

        payment_response = input("And are you paying with cash or card? ")
        print()

        if payment_response == 'cash' or payment_response == 'card':
            print()
            print("Awesome,")
            print("Okay, " + name_response + ", your order will be ready in about 15-20 minutes")
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

# Function for sides and drinks order


def sides_order():
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

            # Display the menu when it's not displayed
            print()
            print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┑   ┏━━━━━━━━━━━━━━━━━━━━━━━━━━┑")
            print("┃         𝓢𝓲𝓭𝓮𝓼               ┃   ┃         𝓓𝓻𝓲𝓷𝓴𝓼           ┃")
            print("┃        ▔▔▔▔▔▔               ┃   ┃        ▔▔▔▔▔▔▔▔          ┃")
            print("┃ 1. Crispy Fries        $6   ┃   ┃  7. Orange juice     $4  ┃")
            print("┃ 2. Loaded Wedges       $8   ┃   ┃  8. Fizzy drink      $4  ┃")
            print("┃ 3. Garlic Bread        $5   ┃   ┃  9. Iced coffee      $6  ┃")
            print("┃ 4. Vegan Garlic Bread  $6   ┃   ┃ 10. Water bottle     $3  ┃")
            print("┃ 5. Cheesy Scrolls      $6   ┃   ┃ 11. Chocolate Milk   $5  ┃")
            print("┃ 6. Green salad         $7   ┃   ┃ 12. Energy Drink     $4  ┃")
            print("┖━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛   ┖━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
            print()
            invalid_attempts = 0
            order_invalid = False

            while True:
                side_drink_response = input("Awesome, just let me know what ones you want (Use 1-12 and separate "
                                            "with commas if getting multiple, e.g., '1,1,3,11') ").lower()

                if side_drink_response == 'hangup':
                    print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
                    exit()

                selected_items = side_drink_response.split(',')

                invalid_items = []

                for item in selected_items:
                    if item in side_menu:
                        item_name = side_menu[item]
                        if item_name in order_summary:
                            order_summary[item_name] += 1  # Increment the quantity
                        else:
                            order_summary[item_name] = 1  # Initialize quantity to 1
                    else:
                        invalid_items.append(item)

                if invalid_items:
                    invalid_attempts += 1
                    print("Invalid item number(s):", ", ".join(invalid_items))
                    if invalid_attempts >= 2:
                        print("You entered invalid items twice. Hanging up.")
                        order_invalid = True
                        break
                    retry = input("Try again? (yes/no) ").lower()
                    if retry == 'no' or retry in no_synonyms.get("no", []):
                        print("Hanging up.")
                        order_invalid = True
                        break
                    elif retry != 'yes' and retry not in yes_synonyms.get("yes", []):
                        print("Nice try")
                        exit()
                else:
                    break

            if order_invalid:
                break

            # Print the order summary
            if order_summary:
                print()
                print("Okay, you selected the following sides and drinks:")
                for item, quantity in order_summary.items():
                    quantity_words = number_to_words(quantity)
                    print(quantity_words + " " + item)
                print()
                total_items = sum(order_summary.values())
                print(f"For a total of {number_to_words(total_items)} items")

                while True:
                    confirmation = input("\nIs that correct? ").lower()
                    if confirmation == 'hangup':
                        print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
                        exit()
                    elif confirmation == 'yes' or confirmation in yes_synonyms.get("yes", []):
                        name_payment()

                    elif confirmation == 'no' or confirmation in no_synonyms.get("no", []):
                        print("\nSorry about that, let's try that again")
                        order_summary.clear()
                        break
                    else:
                        print()
                        final_confirmation = input("Yes or no please, is this all correct?").lower()

                        if final_confirmation == 'hangup':
                            print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
                            exit()
                        elif final_confirmation == 'yes' or final_confirmation in yes_synonyms.get("yes", []):
                            name_payment()

                        else:
                            print()
                            print("I'm very sorry, I don't understand what you're saying, ")
                            print("I hope you find what you're looking elsewhere. Have a good day!")
                            print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
                            exit()
        else:
            print()
            yes_no_response = input("Sorry is that a yes or a no? ")

            if yes_no_response == 'hangup':
                print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
                exit()

            if yes_no_response == 'yes' or yes_no_response in yes_synonyms.get("yes", []):
                print()
                print("Let's try that again")
                continue

            if yes_no_response == 'no' or yes_no_response in no_synonyms.get("no", []):
                print()
                name_payment()

            else:
                print()
                print("I'm sorry, I don't understand what you're saying, ")
                print("I hope you find what you're looking elsewhere. Have a good day!")
                print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
                exit()

# Function for pizza menu


def menu_pizza():

    global order_placed, order_summary, menu_displayed

    first_mistake = True  # Initialize first_mistake to True before the loop

    while True:
        if order_placed:
            confirmation = input("\nIs that correct? ").lower()
            if confirmation in ['yes'] + yes_synonyms.get("yes", []):
                print()
                sides_order()

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
                    print()
                    sides_order()

                elif final_confirmation == 'hangup':
                    print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
                    exit()
                else:
                    print(
                        "\nSorry, I don't understand what you're trying to say here. Have a good rest of your day and "
                        "thank you for calling Ben's Pizzeria")
                    print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
                    exit()

        print()
        quantity_response = input("So, how many are you looking to get today then? (use numbers 1-10) ").lower()

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

                for i in range(quantity):

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
                            print("I'm sorry, I don't understand what you're trying to say.")
                            print()
                            retry_response = input("Would you like to try that again? (yes/no): ").lower()
                            if retry_response != 'yes' and retry_response not in yes_synonyms.get("yes", []):
                                print("Have a good day!")
                                print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
                                exit()

                    if response == 'hangup':
                        exit()

                    pizza_count = order_summary[pizza_type]["count"]
                    order_summary[pizza_type]["count"] = pizza_count + 1

                    print()
                    if pizza_count == 0:
                        print(f"Cool, that's one {pizza_type} pizza.")
                    else:
                        print(f"Cool, that's {number_to_words(pizza_count + 1)} {pizza_type} pizzas.")

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
                            "And what are the numbers of the extra toppings you want? (or press enter for none) "
                            if invalid_extra_choices_count == 0
                            else "\nSorry, could you try that again? "
                        )

                        extra_choices = input(prompt).strip()

                        if extra_choices == "hangup":
                            print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
                            exit()

                        if extra_choices == "":
                            # User entered no extra toppings, break out of the loop
                            break

                        selected_toppings = []

                        # Validate the extra choices
                        invalid_extra_choices = False

                        # Only check for invalid choices if extra_choices is not empty
                        if extra_choices:
                            for topping_num in extra_choices.split(','):
                                if topping_num not in extra_toppings_menu:
                                    invalid_extra_choices = True
                                    invalid_extra_choices_count += 1

                        if not invalid_extra_choices:
                            for topping_num in extra_choices.split(','):
                                selected_toppings.append(extra_toppings_menu[topping_num])

                            order_summary[pizza_type]["extra_toppings"].append(selected_toppings)
                            break

                    # Check if the user entered invalid extra choices twice and exit if so
                    if invalid_extra_choices_count == 2:
                        print()
                        print("I'm sorry, I don't understand what you're saying, ")
                        print("I hope you find what you're looking elsewhere. Have a good day!")
                        print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
                        exit()

        else:
            print()
            print("I'm sorry sir I don't understand what you're saying, ")
            print("I hope you find what you're looking elsewhere. Have a good day!")
            print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
            exit()
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
                    print()
                    sides_order()

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
                        print()
                        sides_order()

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
                        exit()
        if first_mistake:
            print()
            print("I'm sorry, I don't understand.")
            print("Oh yes, I should probably let you know, at Big Ben's Pizzeria,")
            print("we have a policy of only allowing at most, 10 pizzas per order")
            first_mistake = False  # Set the flag to False after the first mistake

# Main routine


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
    "0": " ",
    "1": "Extra cheese +$1.20",
    "2": "Stuffed crust +$2",
    "3": "Aioli +$0.50",
    "4": "BBQ sauce +$0.50",
    "5": "Tomato sauce +$0.50",
}

side_menu = {
    "1": "Crispy Fries",
    "2": "Loaded Wedges",
    "3": "Garlic Bread",
    "4": "Vegan Garlic Bread",
    "5": "Cheesy Scrolls",
    "6": "Green salad",
    "7": "Orange juice",
    "8": "Fizzy drink",
    "9": "Iced coffee",
    "10": "Water Bottle",
    "11": "Chocolate Milk",
    "12": "Energy Drink",
}

# Initialize the flags
order_placed = False
order_summary = {}
menu_displayed = False
consecutive_invalid_responses = 0

# Function to convert numbers to words


while True:
    print("(If you want to hang up, simply say 'hangup')")
    print()
    response = input("Hello, thank you for calling Big Ben's Pizzeria. Would you like to order some pizza?"
                     " (yes/no): ").lower()
    if response == 'hangup':
        print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
        exit()
    if response == 'yes' or response in yes_synonyms.get("yes", []):
        menu_pizza()
    elif response == 'no' or response in no_synonyms.get("no", []):
        print()
        followup_response = input("Sir, please, I'm a minimum wage worker, I don't have time for prank calls."
                                  " Do you want a pizza, yes or no? ").lower()
        if followup_response == 'hangup':
            print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
            exit()
        if followup_response == 'yes' or followup_response in yes_synonyms.get("yes", []):
            menu_pizza()
        elif followup_response == 'no' or followup_response in no_synonyms.get("no", []):
            print("Have a good day, sir")
            print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
            exit()
        else:
            print("Have a good day, sir")
            print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
            exit()
    else:
        print()
        yes_or_no_response = input("Sorry, is that a yes or a no? ").lower()
        if yes_or_no_response == 'hangup':
            print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
            exit()
        if yes_or_no_response == 'yes' or yes_or_no_response in yes_synonyms.get("yes", []):
            menu_pizza()
        elif yes_or_no_response == 'no' or yes_or_no_response in no_synonyms.get("no", []):
            print()
            print("Please don't waste my time sir, have a good rest of your day.")
            print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
            exit()
        else:
            print()
            print("I'm sorry sir I don't understand what you're saying, I hope you find what you're looking elsewhere. "
                  "Have a good day!")
            print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
            exit()
