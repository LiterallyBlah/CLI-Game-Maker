# Import necessary libraries
import curses
import random
import json

# Import the game's quests and items packages
import game.quests as quests
import game.items as items

# Initialize curses
stdscr = curses.initscr()
curses.noecho()
cursed.cbreak()
stdscr.keypad(True)

# Initialize game variables
player_name = ""
player_stats = {"health": 100, "strength": 10, "defense": 5}
player_inventory = []
current_quest = None

# Main game loop
while True:
    # Print the game screen
    stdscr.clear()
    stdscr.addstr(f"Welcome to the game, {player_name}!\n\n")
    stdscr.addstr(f"Health: {player_stats['health']}\n")
    stdscr.addstr(f"Strength: {player_stats['strength']}\n")
    stdscr.addstr(f"Defense: {player_stats['defense']}\n\n")
    stdscr.addstr("1. Start a new quest\n")
    stdscr.addstr("2. View inventory\n")
    stdscr.addstr("3. Quit game\n\n")
    stdscr.addstr("Enter your choice: ")

    # Get the player's choice
    choice = stdscr.getch()

    # Start a new quest
    if choice == ord("1"):
        # Select a random quest from the available quests
        current_quest = random.choice(quests.all_quests)
        current_quest.start_quest()

    # View inventory
    elif choice == ord("2"):
        stdscr.addstr("\nInventory:\n")
        for item in player_inventory:
            stdscr.addstr(f"- {item.name}\n")
        stdscr.addstr("\nPress any key to continue...\n")
        stdscr.getch()

    # Quit game
    elif choice == ord("3"):
        # Save game data to a JSON file
        game_data = {
            "player_name": player_name,
            "player_stats": player_stats,
            "player_inventory": [item.to_dict() for item in player_inventory],
            "current_quest": current_quest.to_dict() if current_quest else None,
        }
        with open("save.json", "w") as f:
            json.dump(game_data, f)

        # End the game loop and clean up curses
        break

curses.echo()
cursed.nocbreak()
stdscr.keypad(False)
curses.endwin()
