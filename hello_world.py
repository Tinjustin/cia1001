import time
import random
from colorama import init, Fore, Back, Style

# Initialize colorama
init()

def print_slow(text, delay=0.03):
    """Print text slowly for dramatic effect"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def display_title():
    """Display the game title with ASCII art"""
    title = """
    ╔═══════════════════════════════════════╗
    ║  THE MAGICAL CRYSTAL OF DESTINY       ║
    ╚═══════════════════════════════════════╝
    """
    print(Fore.CYAN + title + Style.RESET_ALL)

def make_choice(options):
    """Handle player choices"""
    for i, option in enumerate(options, 1):
        print(f"{Fore.YELLOW}{i}. {option}{Style.RESET_ALL}")
    
    while True:
        try:
            choice = int(input(f"{Fore.GREEN}Enter your choice (1-{len(options)}): {Style.RESET_ALL}"))
            if 1 <= choice <= len(options):
                return choice
            print(f"{Fore.RED}Invalid choice. Please try again.{Style.RESET_ALL}")
        except ValueError:
            print(f"{Fore.RED}Please enter a number.{Style.RESET_ALL}")

def game():
    display_title()
    print_slow(f"{Fore.CYAN}Welcome, brave adventurer, to a magical journey!{Style.RESET_ALL}")
    time.sleep(1)
    
    # Player stats
    health = 100
    inventory = []
    
    # First choice
    print_slow(f"\n{Fore.WHITE}You stand at the entrance of a mysterious cave. Strange lights flicker within...{Style.RESET_ALL}")
    print_slow(f"{Fore.MAGENTA}What do you do?{Style.RESET_ALL}")
    
    choice = make_choice([
        "Enter the cave cautiously",
        "Look around for supplies first",
        "Call out to see if anyone's inside"
    ])
    
    if choice == 1:
        print_slow(f"\n{Fore.BLUE}You carefully step into the cave...{Style.RESET_ALL}")
        inventory.append("torch")
        print_slow(f"{Fore.GREEN}You found a torch!{Style.RESET_ALL}")
    elif choice == 2:
        print_slow(f"\n{Fore.BLUE}You search the area and find some useful items.{Style.RESET_ALL}")
        inventory.extend(["healing potion", "rope"])
        print_slow(f"{Fore.GREEN}You found a healing potion and a rope!{Style.RESET_ALL}")
    else:
        print_slow(f"\n{Fore.BLUE}Your voice echoes through the cave...{Style.RESET_ALL}")
        print_slow(f"{Fore.RED}A small rock falls, dealing 10 damage!{Style.RESET_ALL}")
        health -= 10
    
    print_slow(f"\n{Fore.YELLOW}Health: {health}{Style.RESET_ALL}")
    print_slow(f"{Fore.YELLOW}Inventory: {', '.join(inventory)}{Style.RESET_ALL}")
    
    # Second choice
    print_slow(f"\n{Fore.WHITE}Deep in the cave, you discover a glowing crystal on a pedestal.{Style.RESET_ALL}")
    print_slow(f"{Fore.MAGENTA}What do you do?{Style.RESET_ALL}")
    
    choice = make_choice([
        "Take the crystal",
        "Examine it more closely",
        "Leave it alone"
    ])
    
    if choice == 1:
        print_slow(f"\n{Fore.GREEN}Congratulations! You've obtained the Magical Crystal of Destiny!{Style.RESET_ALL}")
        print_slow(f"{Fore.CYAN}However, the cave begins to shake...{Style.RESET_ALL}")
    elif choice == 2:
        print_slow(f"\n{Fore.BLUE}You notice ancient writings warning of a curse...{Style.RESET_ALL}")
        print_slow(f"{Fore.GREEN}Your wisdom has saved you from a terrible fate!{Style.RESET_ALL}")
    else:
        print_slow(f"\n{Fore.YELLOW}Sometimes the wisest choice is to walk away...{Style.RESET_ALL}")
        print_slow(f"{Fore.GREEN}You feel at peace with your decision.{Style.RESET_ALL}")
    
    print_slow(f"\n{Fore.CYAN}Thank you for playing The Magical Crystal of Destiny!{Style.RESET_ALL}")

if __name__ == "__main__":
    try:
        game()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Game terminated by player.{Style.RESET_ALL}") 