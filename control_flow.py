# Control flow task
rating = str(input("What film rating do you want more information on?\nPlease select from\nUniversal\nPG\n12\n15\n18\nOr choose 'exit' to quit\n")) # Asks the user what rating they want to view and writes it as a string, this prevents any errors from occurring if an unexpected character makes its way in to the input

while rating.strip().lower() != exit: # This will loop through the code below while exit has not been entered by the user
    if rating.strip().lower() == "universal": # The strip() removes white spaces and the lower() makes it so that user input is formatted to match our list
        print("Everyone can watch")
    elif rating.strip().lower() == "pg":
        print("General viewing, but some scenes may be unsuitable for young children")
    elif rating.strip().lower() == "12":
        print(" Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.")
    elif rating.strip().lower() == "15":
        print("No one younger than 15 may see a 15 film in a cinema.")
    elif rating.strip().lower() == "18":
        print("No one younger than 18 may see an 18 film in a cinema.")
    elif rating.strip().lower() == "exit":
        break # Exits out the loop
    else:
        print("Invalid input, please try again")

    rating = str(input("What film rating do you want more information on?\nPlease select from\nUniversal\nPG\n12\n15\n18\nOr choose 'exit' to quit\n"))

# Since there's nothing outside the loop, the program will quit