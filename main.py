import sys
import random
import requests

API_KEY = 'zly3l2mBsLfAurF0WeMgPikzVwRptld3fxgdfTa3twh0TMVEXshF1305'
potential_words = ["tree", "dog", "cat", "human", "whale", "fire", "water", "house", "barrel", "car", "truck", "mountain", "hamburger"]


# Main Menu
def main_menu():
    while True:
        print("# # # W E L C O M E # # #")
        user_input = input("Would you like to play a game? (Y/N): ").lower()
        if user_input == "y":
            print("Let's begin!")
            print("Generating Word...")
            generate_word()
            break
        elif user_input == "n":
            sys.exit()
        else:
            print("INVALID CHOICE: Please input either Y for Yes or N for No")

# Generate a word to search
def generate_word():
    round_word = random.choice(potential_words)
    SEARCH_TERM = round_word
    URL = f'https://api.pexels.com/v1/search?query={SEARCH_TERM}&per_page=1'
    
    headers = {'Authorization': API_KEY}

    response = requests.get(URL, headers=headers)
    data = response.json()

    image_url = data['photos'][0]['src']['original']
    print(image_url)

# Search the word online for images

# Convert images to grayscale

# Assign grayscale values to ASCII characters

# Display converted image as ASCII characters for the user in terminal

# Await User Guesses

# Calculate User Score

# Increment Round #

# Check if Round is last round

# Calculate Final User Score

# Provide Victory Dialgoue based on final score range

# Play again?

# Quit Program

# Main Loop

if __name__ == '__main__':
    main_menu()