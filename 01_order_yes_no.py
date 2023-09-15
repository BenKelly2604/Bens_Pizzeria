while True:
    print("( 𝘐𝘧 𝘺𝘰𝘶 𝘸𝘢𝘯𝘵 𝘵𝘰  𝘩𝘢𝘯𝘨 𝘶𝘱 𝘵𝘩𝘦 𝘤𝘢𝘭𝘭, 𝘴𝘪𝘮𝘱𝘭𝘺 𝘴𝘢𝘺 '𝘩𝘢𝘯𝘨𝘶𝘱' ) ")
    print()
    response = input("Hello, thank you for calling Big Ben's Pizzeria. Would you like to order some pizza? (yes/no): "
                     "").lower()

    if response == 'hangup':
        print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
        break

    if response == 'yes':

        print()
        print()
        print()
        print("Program continues...")
        break

    elif response == 'no':
        print()
        followup_response = input("Sir, please, I'm a minimum wage worker, I don't have time for prank calls."
                                  " Do you want a pizza, yes or no? ").lower()
        if followup_response == 'hangup':
            print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
            break

        if followup_response == 'yes':
            print()
            print()
            print("Program continues...")
            break
        elif followup_response == 'no':
            print("Have a good day, sir")
            print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
            break
        else:
            print("Have a good day, sir")
            print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
            break

    else:
        print()
        yes_or_no_response = input("Sorry, is that a yes or a no? ").lower()

        if yes_or_no_response == 'hangup':
            print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
            break
        if yes_or_no_response == 'yes':
            print()
            print("Program continues...")
            break

        elif yes_or_no_response == 'no':
            print()
            print("Please don't waste my time sir, have a good rest of your day.")
            print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
            break
        else:
            print()
            print("I'm sorry sir I don't understand what you're saying, I hope you find what you're looking elsewhere. "
                  "Have a good day!")
            print("*𝘊𝘢𝘭𝘭 𝘦𝘯𝘥𝘦𝘥*")
            break
