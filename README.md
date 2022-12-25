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

        # The module containing the code for quest 2
        quest_2.py

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

            # The module containing the code for the bow item
            bow.py

        # The package containing the code for the game's armor
        armor/
            # Mark this directory as a Python package
            __init__.py

            # The module containing the code for the helmet item
            helmet.py

            # The module containing the code for the chestplate item
            chestplate.py

        # The package containing the code for the game's potions
        potions/
            # Mark this directory as a Python package
            __init__.py

            # The module containing the code for the health potion item
            health_potion.py

            # The module containing the code for the strength potion item
            strength_potion.py

    # The package containing the code for the game's art
    art/
        # Mark this directory as a Python package
        __init__.py

        # The file containing the ASCII art for the player's avatar
        avatar.txt
        # The file containing the ASCII art for an enemy
        enemy.txt

    # The package containing the code for the game's characters
    characters/
        # Mark this directory as a Python package
        __init__.py

        # The module containing the code for the player character
        player.py

        # The module containing the code for enemy 1
        enemy_1.py

        # The module containing the code for enemy 2
        enemy_2.py

    # The package containing the code for handling user input and output
    io/
        # Mark this directory as a Python package
        __init__.py

        # The module containing functions for reading user input
        input.py

        # The module containing functions for displaying messages and prompts to the user
        output.py

    # The package containing the code for saving and loading games
    saved_games/
        # Mark this directory as a Python package
        __init__.py

        # The module containing the function for saving the game
        save_game.py
        # The module containing the function for saving the game
        save_game.py

        # The module containing the function for loading the game
        load_game.py

        # The module containing the function for displaying the list of saved games
        display_saved_games.py

    # The package containing the code for the combat system
    combat/
        # Mark this directory as a Python package
        __init__.py

        # The module containing the function for calculating damage in combat
        calculate_damage.py

        # The module containing the function for applying effects in combat
        apply_effects.py

        # The module containing the function for checking for victory or defeat in combat
        check_victory.py

    # The package containing game-specific configurations
    config/
        # Mark this directory as a Python package
        __init__.py

        # The module containing the game's configurable settings
        game_config.py
```
