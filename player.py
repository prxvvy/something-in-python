class Player:
    def __init__(self, arr: list, n_rows: int, n_cols: int, player: list[int]) -> None:
        self.arr = arr
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.player = player

    def move_up(self):
        if self.player[0] > 0 and self.arr[self.player[0] - 1][self.player[1]] == 0:
            self.player[0] -= 1

    def move_down(self):
        if self.player[0] < self.n_rows - 1 and self.arr[self.player[0] + 1][self.player[1]] == 0:
            self.player[0] += 1

    def move_right(self):
        if self.player[1] < self.n_cols - 1 and self.arr[self.player[0]][self.player[1] + 1] == 0:
            self.player[1] += 1

    def move_left(self):
        if self.player[1] > 0 and self.arr[self.player[0]][self.player[1] - 1] == 0:
            self.player[1] -= 1
