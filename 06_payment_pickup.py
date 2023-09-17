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
            print(f"Okay, {name_response}, your order will be ready in about 15-20 minutes")
            print("See you soon!")
            print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
            break  # Exit the loop once the order is confirmed
        else:
            final_payment_response = input("Sorry, is that cash or card that you'll be paying for the pizza with? ")

            if final_payment_response == 'cash' or final_payment_response == 'card':
                print()
                print("Awesome,")
                print(f"Okay, {name_response}, your order will be ready in about 15-20 minutes")
                print("See you soon!")
                print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
                break  # Exit the loop once the order is confirmed
            else:
                print()
                print("I'm very sorry, I don't understand what you're saying, ")
                print("I hope you find what you're looking for elsewhere. Have a good day!")
                print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
                exit()

# Call the name_payment function to start the process


name_payment()
