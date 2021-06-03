from map import Map
from player import Player

rows = 15
cols = 100
arr = []
player = [0, 0]
goal = [rows - 1, cols - 1]
map_ = Map(arr, rows, cols, player, goal)
p = Player(arr, rows, cols, player)

while player != goal:
    map_.display_map()
    opt = input("\n")
    if opt == "x":
        break
    if opt == "w":
        p.move_up()
    if opt == "s":
        p.move_down()
    if opt == "d":
        p.move_right()
    if opt == "a":
        p.move_left()
