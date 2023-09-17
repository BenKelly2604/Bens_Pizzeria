def words_to_numbers(word):
    # Define a dictionary to map word representations to numbers
    number_dict = {
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

    # Check if the input word is in the dictionary, if not, return 0
    return number_dict.get(word, 0)

# Define the pizza menu and prices
pizza_menu = {
    "1": "Ham and cheese",
    "2": "Margherita",
    "3": "Pepperoni",
    "4": "Vegetarian",
    "5": "Beef and Onion",
    "6": "Meat Lovers",
}

# Define the extra toppings menu and prices
extra_toppings_menu = {
    "1": "Extra cheese",
    "2": "Stuffed crust",
    "3": "Aioli",
    "4": "BBQ sauce",
    "5": "Tomato sauce",
}

# Define the drinks menu and prices
drinks_menu = {
    "1": "Coke",
    "2": "Pepsi",
    "3": "Sprite",
    "4": "Iced Tea",
    "5": "Lemonade",
}

# Define a dictionary to store synonyms for "yes" and "no" responses
yes_synonyms = {
    "yes": ["yes", "yeah", "yep"],
}

no_synonyms = {
    "no": ["no", "nope"],
}

order_summary = {}  # Initialize an empty dictionary to store the order

print("Welcome to Ben's Pizzeria!")
print("You can order pizzas, extra toppings, and drinks.")
print("At any time, you can type 'hangup' to exit the order process.")
print("Let's get started!")

menu_displayed = False  # Variable to track if the menu has been displayed
order_placed = False  # Variable to track if an order has been placed

while True:
    print()
    quantity_response = input("How many items would you like to order (1-10 or one to ten)? ").lower()

    if quantity_response == 'hangup':
        print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
        break

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
                print("┃ 4. Vegetarian       $12  ┃")
                print("┃ 5. Beef and Onion   $13  ┃")
                print("┃ 6. Meat Lovers      $13  ┃")
                print("┃                        ┃")
                print("┃ - Type the numbers to - ┃")
                print("┃  add pizza to order  -  ┃")
                print("┃                        ┃")
                print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━┙")
                print()

                print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━┑")
                print("┃       𝓓𝓻𝓲𝓷𝓴𝓼             ┃")
                print("┃        ▔▔▔▔▔▔            ┃")
                print("┃ 1. Coke             $2.50  ┃")
                print("┃ 2. Pepsi            $2.50  ┃")
                print("┃ 3. Sprite           $2.50  ┃")
                print("┃ 4. Iced Tea         $2.00  ┃")
                print("┃ 5. Lemonade         $2.00  ┃")
                print("┃                        ┃")
                print("┃ - Type the numbers to - ┃")
                print("┃  add drink to order  -  ┃")
                print("┃                        ┃")
                print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━┙")
                print()

                menu_displayed = True

            while True:
                print()
                item_response = input("Now tell me which item you'd like (pizza/drink): ").lower()

                if item_response == 'hangup':
                    print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
                    break

                if item_response == 'pizza':
                    print()
                    pizza_response = input("Choose a pizza from the menu (1-6): ").lower()

                    if pizza_response == 'hangup':
                        print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
                        break

                    if pizza_response in pizza_menu:
                        if pizza_response in order_summary:
                            order_summary[pizza_response] += 1
                        else:
                            order_summary[pizza_response] = 1

                        print(f"Alright, {pizza_menu[pizza_response]} added to your order.")
                        order_placed = True
                    else:
                        print("\nI'm sorry, I don't think we have that pizza. Could you please choose from the menu?")
                elif item_response == 'drink':
                    print()
                    drink_response = input("Choose a drink from the menu (1-5): ").lower()

                    if drink_response == 'hangup':
                        print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
                        break

                    if drink_response in drinks_menu:
                        if drink_response in order_summary:
                            order_summary[drink_response] += 1
                        else:
                            order_summary[drink_response] = 1

                        print(f"Alright, {drinks_menu[drink_response]} added to your order.")
                        order_placed = True
                    else:
                        print("\nI'm sorry, I don't think we have that drink. Could you please choose from the menu?")
                else:
                    print("\nI'm sorry, I didn't understand. Please specify 'pizza' or 'drink' for your order.")

                if order_placed:
                    print()
                    more_items_response = input("Would you like to order more items (yes/no)? ").lower()
                    if more_items_response in yes_synonyms:
                        continue
                    elif more_items_response in no_synonyms:
                        break
                    else:
                        print("I'm sorry, I didn't understand your response. Assuming you don't want more items.")
                        break

    else:
        # Try to convert the word to a number using the function
        quantity = words_to_numbers(quantity_response)

        if quantity > 0:
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
                print("┃ 4. Vegetarian       $12  ┃")
                print("┃ 5. Beef and Onion   $13  ┃")
                print("┃ 6. Meat Lovers      $13  ┃")
                print("┃                        ┃")
                print("┃ - Type the numbers to - ┃")
                print("┃  add pizza to order  -  ┃")
                print("┃                        ┃")
                print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━┙")
                print()

                print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━┑")
                print("┃       𝓓𝓻𝓲𝓷𝓴𝓼             ┃")
                print("┃        ▔▔▔▔▔▔            ┃")
                print("┃ 1. Coke             $2.50  ┃")
                print("┃ 2. Pepsi            $2.50  ┃")
                print("┃ 3. Sprite           $2.50  ┃")
                print("┃ 4. Iced Tea         $2.00  ┃")
                print("┃ 5. Lemonade         $2.00  ┃")
                print("┃                        ┃")
                print("┃ - Type the numbers to - ┃")
                print("┃  add drink to order  -  ┃")
                print("┃                        ┃")
                print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━┙")
                print()

                menu_displayed = True

            while True:
                print()
                item_response = input("Now tell me which item you'd like (pizza/drink): ").lower()

                if item_response == 'hangup':
                    print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
                    break

                if item_response == 'pizza':
                    print()
                    pizza_response = input("Choose a pizza from the menu (1-6): ").lower()

                    if pizza_response == 'hangup':
                        print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
                        break

                    if pizza_response in pizza_menu:
                        if pizza_response in order_summary:
                            order_summary[pizza_response] += quantity
                        else:
                            order_summary[pizza_response] = quantity

                        print(f"Alright, {quantity} {pizza_menu[pizza_response]}(s) added to your order.")
                        order_placed = True
                    else:
                        print("\nI'm sorry, I don't think we have that pizza. Could you please choose from the menu?")
                elif item_response == 'drink':
                    print()
                    drink_response = input("Choose a drink from the menu (1-5): ").lower()

                    if drink_response == 'hangup':
                        print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
                        break

                    if drink_response in drinks_menu:
                        if drink_response in order_summary:
                            order_summary[drink_response] += quantity
                        else:
                            order_summary[drink_response] = quantity

                        print(f"Alright, {quantity} {drinks_menu[drink_response]}(s) added to your order.")
                        order_placed = True
                    else:
                        print("\nI'm sorry, I don't think we have that drink. Could you please choose from the menu?")
                else:
                    print("\nI'm sorry, I didn't understand. Please specify 'pizza' or 'drink' for your order.")

                if order_placed:
                    print()
                    more_items_response = input("Would you like to order more items (yes/no)? ").lower()
                    if more_items_response in yes_synonyms:
                        continue
                    elif more_items_response in no_synonyms:
                        break
                    else:
                        print("I'm sorry, I didn't understand your response. Assuming you don't want more items.")
                        break
        else:
            print("\nI'm sorry, I didn't understand your quantity. Please enter a number between 1 and 10.")

# Display the final order summary
print("\nOrder Summary:")
for item, quantity in order_summary.items():
    if item in pizza_menu:
        print(f"{quantity} {pizza_menu[item]}(s)")
    elif item in drinks_menu:
        print(f"{quantity} {drinks_menu[item]}(s)")

print("\nThank you for ordering from Ben's Pizzeria!")
