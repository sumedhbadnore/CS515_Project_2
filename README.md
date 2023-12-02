# CS515 Project-2 : Text Based Adventure Game

## Author Information
Sumedh Badnore 
sbadnore@stevens.edu

[Github Repository](https://github.com/sumedhbadnore/CS515_Project_2)

## Estimation of hours spent on the project
I have put approximately 22 hours into this project.

## To execute the program, follow these steps
- Install Python 3 on your system.
- Download or clone this repository to your local machine.
- Navigate to the repository folder.
- Run the following command in the terminal: `python3 adventure.py [mapfile]`

## Overview
In this CS 515-A project, I have worked on a text-based video game where players navigate a world through textual commands. These games, known as text adventures, represent an early form of computer gaming, immersing players in a narrative-rich environment filled with puzzles, riddles, and mystery.

### Game Mechanics
This game contains several verbs that function as commands:
- go: This verb attempts to move the player in a specified direction. Utilize the command by typing `go [direction]` with the direction being a valid exit.

- look: The look command revisits the description of the current room. Use the command by simply typing `look`.

- get: The get verb enables the player to pick up items within the room. Typing `get [ITEM]` will add the item to the player's inventory, removing it from the room.

- drop: The drop verb allows the player to discard items from their inventory into the current room. Typing `drop [ITEM]` removes the item from the inventory.

- inventory: The `inventory` verb displays the list of items currently carried by the player.

- help: The help verb provides the player with a list of all available commands.

- quit: The `quit` verb concludes the game and exits the program.

- win: To assess the winning condition and declare win if true.

## Testing of the code
- Initially, I conducted thorough code testing by executing each command across all provided map files.
  
- Next, I created a custom map to ensure the proper functioning of all functions.

## Unresolved Bugs or Issues
No unresolved bugs or issues were identified.


## Examples of bugs resolved
--write here--


## Extensions Implemented
- **Help Command**: The 'help' extension introduces a dynamic command that gives a complete list of all valid actions in the game. Functions that require parameters are denoted by `[verb] ...` for example:

```
> A white room

You are in a simple room with white walls.

Exits: north east

What would you like to do? help
You can run the following commands:
 drop ...
 get ...
 go ...
 help
 inventory
 look
 quit
 win
What would you like to do?
```
- **Drop Command**: The 'drop' extension improves the gameplay by allowing the player to drop an item in the room. Drop requires one parameter specifying the item to drop for example `drop [item]`. Executing this command removes the specified item from the player's inventory and adds it to the room's item list. For example:
```
> The Enchanted Library

Ancient books line the shelves, and mystical symbols decorate the walls.

Items: books, pen

Exits: east west

What would you like to do? get books
You pick up the books.     
What would you like to do? go east
You go east.

> The Egyptian Tomb

Mummies and mysterious artifacts surround you

Exits: west south north

What would you like to do? drop books
You drop the books.
What would you like to do? look
> The Egyptian Tomb

Mummies and mysterious artifacts surround you

Items: books

Exits: west south north

What would you like to do?
```

- **Win Condition**: I have added a winning condition into the game. If the player reaches the 'finalroom' and possesses the key, they can use the `win` verb to check if they have successfully won the game.

- **To trigger win condition**: 
1. You will be spawned in "The Enchanted Library", from there `go west`
2. You will reach "A Movie Theater", from there `go south`
3. Now you are in "The Haunted Manor", now you have to `get key`
4. After getting key, you will have to `go north`
5. Once again you will be in "A Movie Theater", this time `go north`
5. Now you have reached "The Secret Agent Hideout", it is the ultimate stage. enter `win` to win the game.

For example:
```
> The Secret Agent Hideout

Briefcases, gadgets, and hidden passages set the stage for espionage.

You've reached the ultimate stage of the game.
To successfully exit and claim victory, acquiring a key is essential.

Exits: west

What would you like to do? inventory
Inventory:
 key
What would you like to do? win
Congratulations! You've conquered the escape room and emerged victorious!
Goodbye!
```