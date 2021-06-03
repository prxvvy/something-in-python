from random import random


class Map:
    def __init__(self, arr: list, n_rows: int, n_cols: int, player: list[int], goal: list[int]):
        self.arr = arr
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.player = player
        self.goal = goal
        self.__create_map()

    def __create_map(self) -> None:
        for i in range(self.n_rows):
            self.arr.append([])
            for j in range(self.n_cols):
                item = 0
                if random() > 0.8:
                    item = 1
                self.arr[i].append(item)

    def display_map(self) -> None:
        for i in range(len(self.arr)):
            for j in range(len(self.arr[i])):
                item = " "
                if self.arr[i][j] == 1:
                    item = "*"
                if self.player[0] == i and self.player[1] == j:
                    item = "P"
                if self.goal[0] == i and self.goal[1] == j:
                    item = "G"
                print(item, end="")
            print()
