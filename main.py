import random
import time

def roll_dice():
    # Visual ASCII faces for the terminal dice
    dice_faces = {
        1: " -----\n|     |\n|  o  |\n|     |\n -----",
        2: " -----\n|o    |\n|     |\n|    o|\n -----",
        3: " -----\n|o    |\n|  o  |\n|    o|\n -----",
        4: " -----\n|o   o|\n|     |\n|o   o|\n -----",
        5: " -----\n|o   o|\n|  o  |\n|o   o|\n -----",
        6: " -----\n|o   o|\n|o   o|\n|o   o|\n -----"
    }
    
    print("\nRolling the dice...")
    time.sleep(0.5)  # Creates a slight processing delay effect
    
    result = random.randint(1, 6)
    print(dice_faces[result])
    print(f"You rolled a {result}!")

def main():
    print("Welcome to the Python Dice Rolling Simulator!")
    
    while True:
        user_choice = input("\nPress [Enter] to roll, or type 'q' to quit: ").strip().lower()
        if user_choice == 'q':
            print("Thanks for playing!")
            break
        roll_dice()

if __name__ == "__main__":
    main()
