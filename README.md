# Control flow task
We were given the following pseudo code:

## Movie Ratings!
As a user I should be able to ask the user for the a rating, and receive back the appropriate response:

- check for rating for this movie:
    - universal -> everyone can watch
    - pg --> General viewing, but some scenes may be unsuitable for young children
    - 12 -->  Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.
    - 15 --> No one younger than 15 may see a 15 film in a cinema.
    - 18 --> No one younger than 18 may see an 18 film in a cinema.

## `control_flow.py`
The code is based around the `while` loop which will keep the program running forever or until the user enters `exit` when `break` is used to exit the loop!

First we'll ask the user what rating of film they want to see information on:
```python
rating = str(input("What film rating do you want more information on?\nPlease select from\nUniversal\nPG\n12\n15\n18\nOr choose 'exit' to quit\n"))
```
We force it in to a string to make the loop easier to deal with.

Then we start the loop:
```python
while rating.strip().lower() != exit:
```
This simply keeps the code running until the user wants to exit

Then the program simply checks what the user has typed against each one of the `if` statements and these will supply them with the required information:
```python
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

```
I've also included an error statement so if the user enters in an invalid option, they're forced to try again until they enter a valid option, this is done just below the `if` statements
```python
 rating = str(input("What film rating do you want more information on?\nPlease select from\nUniversal\nPG\n12\n15\n18\nOr choose 'exit' to quit\n"))
```
After the user types `exit` the program will simply quit because there is nothing outside