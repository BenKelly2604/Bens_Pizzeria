# Initialize the flags
order_summary = {}
yes_synonyms = {
    "yes": ["sure", "absolutely", "okay", "fine", "yea", "yeah", "yep", "yup", "totally", "of course", "indeed",
            "mhm", "ok", "alright", "y"]
}
no_synonyms = {
    "no": ["nope", "nah", "never", "nay", "n"]
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


# Function to convert numbers to words
def number_to_words(num):
    units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve"]

    if 1 <= num <= 12:
        return units[num]


def sides_order():
    while True:
        print()
        yes_no_response = input("Lastly, would you like any sides or drinks today? ").lower()

        if yes_no_response == "hangup":
            print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
            exit()
        if yes_no_response == 'no' or yes_no_response in no_synonyms.get("no", []):
            print()
            print("Awesome, can I get a name..")
            print()
            print("Program continues...")
            exit()

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
                    print(f"{quantity_words} {item}")
                print()
                total_items = sum(order_summary.values())
                print(f"For a total of {number_to_words(total_items)} items")

                while True:
                    confirmation = input("\nIs that correct? ").lower()
                    if confirmation == 'hangup':
                        print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
                        exit()
                    elif confirmation == 'yes' or confirmation in yes_synonyms.get("yes", []):
                        print("\nCool, can I get a name for your order?...")
                        print()
                        print("Program continues...")
                        exit()
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
                            print("\nCool, can I get a name for your order?...")
                            print()
                            print("Program continues...")
                            exit()
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
                print("Awesome, can I get a name..")
                print()
                print("Program continues...")
                exit()
            else:
                print()
                print("I'm sorry, I don't understand what you're saying, ")
                print("I hope you find what you're looking elsewhere. Have a good day!")
                print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
                exit()

# Call the sides_order function to start the process


sides_order()
