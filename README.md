# THIS IS STILL IN PROGRESS AND DOESN'T WORK!

# CLI-Game-Maker
CLI Game Maker is a modular Python program that enables the creation of quests, items, and art to be easily added. It is made to be simple and easy to use with a simple structure. The combat and levelling system are 'static' in a sense that I don't expect people to be changing this side of the code. However, you're free to do as you please! The file structure is as follows:

```
# The main script containing the main game loop and handling the flow of the game
main.py

# The package containing the code for the entire game
game/
    # Mark this directory as a Python package
    __init__.py

    # The package containing the code for the game's quests
    quests/
        # Mark this directory as a Python package
        __init__.py

        # The module containing the code for quest 1
        quest_1.py
            # This module should define a function or class representing quest 1,
            # including any necessary attributes (e.g. quest name, description, objectives)
            # and methods (e.g. start quest, complete quest).

        # The module containing the code for quest 2
        quest_2.py
            # This module should define a function or class representing quest 2,
            # including any necessary attributes (e.g. quest name, description, objectives)
            # and methods (e.g. start quest, complete quest).

    # The package containing the code for the game's items
    items/
        # Mark this directory as a Python package
        __init__.py

        # The package containing the code for the game's weapons
        weapons/
            # Mark this directory as a Python package
            __init__.py

            # The module containing the code for the sword item
            sword.py
                # This module should define a function or class representing the sword item,
                # including any necessary attributes (e.g. item name, description, damage)
                # and methods (e.g. use item, equip item).

            # The module containing the code for the bow item
            bow.py
                # This module should define a function or class representing the bow item,
                # including any necessary attributes (e.g. item name, description, damage)
                # and methods (e.g. use item, equip item).

        # The package containing the code for the game's armor
        armor/
            # Mark this directory as a Python package
            __init__.py

            # The module containing the code for the helmet item
            helmet.py
                # This module should define a function or class representing the helmet item,
                # including any necessary attributes (e.g. item name, description, defense)
                # and methods (e.g. use item, equip item).

            # The module containing the code for the chestplate item
            chestplate.py
                # This module should define a function or class representing the chestplate item,
                # including any necessary attributes (e.g. item name, description, defense)
                # and methods (e.g. use item, equip item).

        # The package containing the code for the game's potions
        potions/
            # Mark this directory as a Python package
            __init__.py

            # The module containing the code for the health potion item
            health_potion.py
                # This module should define a function or class representing the health potion item,
                # including any necessary attributes (e.g. item name, description, healing effect)
                # and methods (e.g. use item).

            # The module containing the code for the strength potion item
            strength_potion.py
                # This module should define a function or class representing the strength potion item,
                # including any necessary attributes (e.g. item name, description, strength effect)
                # and methods (e.g. use item).

    # The package containing the code for the game's art
    art/
        # Mark this directory as a Python package
        __init__.py

        # The file containing the ASCII art for the player's avatar
        avatar.txt
            # This file should contain the ASCII art for the player's avatar as a string.

        # The file containing the ASCII art for an enemy
        enemy.txt
            # This file should contain the ASCII art for an enemy as a string.

    # The package containing the code for the game's characters
    characters/
        # Mark this directory as a Python package
        __init__.py

        # The module containing the code for the player character
        player.py
            # This module should define a function or class representing the player character,
            # including any necessary attributes (e.g. name, avatar, inventory, stats)
            # and methods (e.g. update attributes, equip item).

        # The module containing the code for enemy 1
        enemy_1.py
            # This module should define a function or class representing enemy 1,
            # including any necessary attributes (e.g. name, avatar, stats)
            # and methods (e.g. attack, defend).

        # The module containing the code for enemy 2
        enemy_2.py
            # This module should define a function or class representing enemy 2,
            # including any necessary attributes (e.g. name, avatar, stats)
            # and methods (e.g. attack, defend).

    # The package containing the code for handling user input and output
    io/
        # Mark this directory as a Python package
        __init__.py

        # The module containing functions for reading user input
        input.py
            # This module should define functions for reading user input, such as text input or menu selections.

        # The module containing functions for displaying messages and prompts to the user
        output.py
            # This module should define functions for displaying messages and prompts to the user,
            # such as prompts for character creation or quest objectives.

    # The package containing the code for saving and loading games
    saved_games/
        # Mark this directory as a Python package
        __init__.py

        # The module containing the function for saving the game
        save_game.py
            # This module should define a function for saving the game, including the player character,
            # current quest, and any other relevant data. The saved game data should be stored in a file
            # in the saved_games folder.

        # The module containing the function for loading the game
        load_game.py
            # This module should define a function for loading a saved game from a file in the saved_games folder.
            # The function should return the player character and any other relevant data.

        # The module containing the function for displaying the list of saved games
        display_saved_games.py
            # This module should define a function for displaying a list of saved games stored in the saved_games folder.

    # The package containing the code for the combat system
    combat/
        # Mark this directory as a Python package
        __init__.py

        # The module containing the function for calculating damage in combat
        calculate_damage.py
            # This module should define a function for calculating the damage dealt by an attack or ability
            # based on the attacker's stats and the type of attack or ability being used.

        # The module containing the function for applying effects in combat
        apply_effects.py
            # This module should define a function for applying any effects (e.g. debuffs, healing) to a character
            # during combat.

        # The module containing the function for checking for victory or defeat in combat
        check_victory.py
            # This module should define a function for checking if a character has won or lost a combat encounter,
            # based on their health and any other relevant factors.

    # The package containing game-specific configurations
    config/
        # Mark this directory as a Python package
        __init__.py

        # The module containing the game's configurable settings
        game_config.py
            # This module should define variables or constants representing the game's configurable settings,
            # such as the maximum number of items in the player's inventory or the starting stats of enemies.
```
