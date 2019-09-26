""""
    directions to move - all 8 directions
    number of rooms - 8
    room 1 - blue room - directions to move: east - hall, south - dungeon
    room2 - hall - dtm: ne - store, e- king's chamber, se- knight room, sw - garden, w - dungeon, nw - blue room
    room 3 - store - directions to move: west - hall, south - king's chamber
    room 4 - king's chamber - directions to move: north  - store, west - hall, south - knight room
    room 5 - knight room - dtm - north - king's chamber, nw - hall, west - garden,
    room 6 - garden - dtm - ne - hall, nw - dungeon, south - kitchen
    room 7 - dungeon - dtm - n - blue room, s - garden, e - hall,
    room 8 - kitchen - end...
"""

room_dict = {
    1: "blue room",
    2: "hall",
    3: "store",
    4: "king's chamber",
    5: "knight room",
    6: "garden",
    7: "dungeon",
    8: "kitchen"
}

directions_to_move = {
    "blue room": {"e": 2, "s": 7},
    "hall": {"ne": 3, "e": 4, "se": 5, "sw": 6, "w": 7, "nw": 1},
    "store": {"w": 2, "s": 4},
    "king's chamber": {"n": 3, "w": 2, "s": 5},
    "knight room": {"n": 4, "nw": 2, "w": 6},
    "garden": {"ne": 2, "nw": 7, "s": 8},
    "dungeon": {"n": 1, "s": 6, "e": 2},
    "kitchen": {}
}

directions = {
    'n': 'North',
    'ne': 'North East',
    'e': 'East',
    'se': 'South East',
    's': 'South',
    'sw': 'South West',
    'w': 'West',
    'nw': 'North West'
}

room_desc = {
    "blue room": "You have entered the Blue Room",
    "hall": "You have entered the Hall",
    'store': "You have entered the Store Room",
    "king's chamber": "You have entered the King's Chamber",
    "knight room": "You have entered the Knight's Room",
    "garden": "You have entered the Garden",
    "dungeon": "You have entered the Dungeon",
    "kitchen": "You have reached the end!!!!!!!"
}
print("Welcome to Azeem's adventure game! Your aim is to reach the kitchen....\n You are in a blue room")
current_room: int = 1
direction = None
while current_room != 8:
    dtm_print = []
    dtm = [dir for dir, room in directions_to_move[room_dict[current_room]].items()]
    for direc in dtm:
        dtm_print.append(directions[direc])
    print("To exit press 0")
    print("{}.\n Directions to move: {}".format(room_desc[room_dict[current_room]], dtm_print))
    direction = input("What direction do you want to move: ")
    if direction == "0":
        break
    if direction not in dtm:
        print("Cannot move in this direction.")
        continue
    current_room = directions_to_move[room_dict[current_room]][direction]

if direction == '0':
    print("You have successfully exited.")
else:
    print("Congratulations, you have reached the kitchen, eat away")