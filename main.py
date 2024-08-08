import sys
import random
import requests
from PIL import Image
from io import BytesIO


API_KEY = 'zly3l2mBsLfAurF0WeMgPikzVwRptld3fxgdfTa3twh0TMVEXshF1305'
potential_words = ["tree", "dog", "cat", "human", "whale", "fire", "water", "house", "barrel", "car", "truck", "mountain", "hamburger", "heart", "triangle", "square", "bird"]
GAME_ROUND = 0
PLAYER_POINTS = 0
MAX_ROUNDS = 10

# Main Menu
def main_menu():
    global GAME_ROUND, PLAYER_POINTS
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
    global GAME_ROUND, PLAYER_POINTS
    round_word = random.choice(potential_words)
    SEARCH_TERM = round_word

    # Search the word online for images
    URL = f'https://api.pexels.com/v1/search?query={SEARCH_TERM}&per_page=1'
    
    headers = {'Authorization': API_KEY}

    response = requests.get(URL, headers=headers)
    data = response.json()

    image_url = data['photos'][0]['src']['original']
    print(image_url)

    convert_to_ascii(image_url, round_word)


def convert_to_ascii(image_url, round_word):
    global GAME_ROUND, PLAYER_POINTS
    # Download the image
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    
    # Convert images to grayscale
    grayscale_img = img.convert('L')

    # Resize image for better terminal compatibility
    width, height = grayscale_img.size
    aspect_ratio = height/float(width)
    new_width = 100
    new_height = int(aspect_ratio * new_width * 0.55)
    grayscale_img = grayscale_img.resize((new_width, new_height))

    # Assign grayscale values to ASCII characters
    ascii_str = ''
    pixels = grayscale_img.getdata()
    ascii_chars = ['@', '8', 'B', 'M', 'E', 'H', 'W', 'K', '#', 'S', '%', '?', '7', '5', '3', 'i', 'x', 'a', 's', '*', '+', ';', ':', '-', '"', ',', '.']
    for pixel in pixels:
        ascii_str += ascii_chars[pixel // 10] # Map pixel value to ASCII character

    # Split ASCII string into lines
    ascii_str_len = len(ascii_str)
    ascii_img = "\n".join([ascii_str[index:(index+new_width)] for index in range(0, ascii_str_len, new_width)])

    # Display converted image as ASCII characters for the user in terminal
    print(ascii_img)

    # Await User Guesses
    print("\nGuess the image. 3 chances. 1 word.")
    user_guess1 = input("\nGuess 1: ")
    if user_guess1 == round_word:
        GAME_ROUND += 1
        PLAYER_POINTS += 3
        print("Congratulations! First Guess :)\n")
    else:
        print("\nWRONG - Try again")
        user_guess2 = input("\nGuess 2: ")
        if user_guess2 == round_word:
            GAME_ROUND += 1
            PLAYER_POINTS += 2
            print("Nicely done\n")
        else:
            print("\nStill not correct, last chance")
            user_guess3 = input("\nGuess 3: ")
            if user_guess3 == round_word:
                GAME_ROUND += 1
                PLAYER_POINTS += 1
                print("Good\n")
            else:
                print("Nope, sorry. No points")

    if GAME_ROUND == MAX_ROUNDS:
        print(f"\n STARTING ROUND {GAME_ROUND} NOW")
        generate_word()
    else:
        print("Calculating Final Score...")


# Calculate Final User Score
def calculate_final_score(PLAYER_POINTS):
    score_percentage = (PLAYER_POINTS / (MAX_ROUNDS * 3)) * 100

    if score_percentage >= 100:
        print("\nWOW! A PERFECT SCORE!")
        if score_percentage >= 81 and score_percentage < 100:
            print("\n Very good! Almost perfect :)")
            if score_percentage >= 61 and score_percentage < 81:
                print("\n A little more practice and you are going to crush it!")
                if score_percentage >= 41 and score_percentage < 61:
                    print("\nOof, well, ASCII is hard to read anyway")
                    if score_percentage >= 21 and score_percentage < 41:
                        print("\nYou probably wouldn't enjoy classic Dwarf Fortress...")
                        if score_percentage >= 0 and score_percentage < 21:
                            print("\nWanna play something else? Maybe?")

    user_choice1 = input("\n\n\nWanna play again? (Y/N): ").lower()

    if user_choice1 == 'y':
        print("Good luck!")
        restart_game()

        print("Initializing New Game...")
        generate_word()


def restart_game():
    global GAME_ROUND, PLAYER_POINTS
    GAME_ROUND == 0
    PLAYER_POINTS == 0


# Main Loop

if __name__ == '__main__':
    main_menu()