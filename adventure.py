import json
import sys
import inspect

class Adventure:

    def __init__(self, filename):
        self.current_room = 0
        self.player_inventory = []
        self.load_map(filename)
        self.flag = True

    def load_map(self, filename):
        try:
            with open (filename, 'r') as f:
                self.game_map = json.load(f)
        except FileNotFoundError:
            print(f"Error: file '{filename}' not found.")
            sys.exit(1)
        except json.JSONDecodeError:
            print("Error: Invalid JSON format")
            sys.exit(1)

    def look(self):
        self.room = self.game_map[self.current_room]
        if "finalroom" in self.room:
            print(f"> {self.room['name']}\n\n{self.room['desc']}\n")
            print("You are in the final room of the game,\nYou need to have a key to leave this room and win the game")
            exits = ' '.join(self.room['exits'].keys())
            print(f"Exits: {exits}\n")
        else:
            print(f"> {self.room['name']}\n\n{self.room['desc']}\n")
            if "items" in self.room and len(self.room['items']) > 0:
                print("Items: ", end="")
                all_items = self.room['items']
                if(len(all_items) > 1):
                    for i in range(0,len(all_items)-1):
                        print(all_items[i], end=", ")
                print(f"{all_items[-1]}\n")
            exits = ' '.join(self.room['exits'].keys())
            print(f"Exits: {exits}\n")

    def go(self, direction, exits):
        if direction in exits:
            print(f"You go {direction}.\n")
            self.current_room = self.room['exits'][direction]
            self.look()
        else:
            print(f"There's no way to go {direction}.")

    def quit(self):
        print("Goodbye!")
        self.flag = False

    def get(self, item, items):
        if item in items:
            print(f"You pick up the {item}.")
            self.player_inventory.append(item)
            self.room['items'].remove(item)

        else:
            print(f"There's no {item} anywhere.")

    def inventory(self):
        if len(self.player_inventory) > 0:
            print("Inventory:")
            for i in self.player_inventory:
                print(" " + i)
        else:
            print("You're not carrying anything.")

    def drop(self, item):
        if item in self.player_inventory:
            print(f"You drop the {item}.")
            self.player_inventory.remove(item)
            if 'items' in self.room:
                self.room['items'].append(item)
            else:
                self.room['items'] = f"{item}"

        else:
            print(f"You don't have {item}.")

    def win(self):
        if "finalroom" in self.room:
            if "key" in self.player_inventory:
                print("Congratulations, You Won!")
                self.quit()
            else:
                print("You don't have the key.")
        else:
            print("You are not in the finalroom.")

    def help(self):
        attributes = dir(Adventure)
        my_functions = [i for i in attributes if not i.startswith("__")]
        my_functions.remove('load_map')
        my_functions.remove('run_game')
        print("You can run the following commands:")
        for func_name in my_functions:
            func = getattr(Adventure, func_name)
            signature = inspect.signature(func)
            
            if len(signature.parameters) > 1:
                print(f" {func_name} ...")
            else:
                print(f" {func_name}")

    def run_game(self):
        self.look()
        while self.flag:
            try:
                player_choice = input("What would you like to do? ").lower().strip().split(" ")

                if player_choice[0] == "quit":
                    self.quit()

                if player_choice[0] == "go":
                    if len(player_choice) >= 2:
                        self.go(player_choice[1], list(self.room['exits'].keys()))
                    else:
                        print("Sorry, you need to 'go' somewhere.")

                if player_choice[0] == "look":
                    self.look()

                if player_choice[0] == "help":
                    self.help()

                if player_choice[0] == "inventory":
                    self.inventory()
                
                if player_choice[0] == "get":
                    if len(player_choice) >= 2:
                        if len(player_choice) >= 3:                                   
                            for i in range(2,len(player_choice)):
                                player_choice[1] = f"{player_choice[1]} {player_choice[i]}"
                        try:
                            items = list(self.room['items'])
                            self.get(player_choice[1], items)
                        except Exception as e:
                            print(f"There's no {player_choice[1]} anywhere.")
                            continue
                    else:
                        print("Sorry, you need to 'get' something.")    

                if player_choice[0] == "drop":
                    if len(player_choice) >= 2:
                        if len(player_choice) >= 3:
                            for i in range(2, len(player_choice)):
                                player_choice[1] = f"{player_choice[1]} {player_choice[i]}"
                        self.drop(player_choice[1])
                    else:
                        print("Sorry, you need to 'drop' something.")

                if player_choice[0] == "win":
                    self.win()

            except EOFError:
                print("Use 'quit' to exit.")
                continue

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 adventure.py [map file]")
        sys.exit(1)

    map_file = sys.argv[1]
    game = Adventure(map_file)
    game.run_game()