import json

with open ("loop.map", 'r') as f:
    game_map = json.load(f)

current_room = 3
room = game_map[current_room]

print(list(room['items']))