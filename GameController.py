from Model import DirectionModel
import random


class GameController:
    def __init__(self):
        self.__list_merge = None
        self.__map = [[0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0]]
        self.__list_empty_location = []
    @property
    def map(self):
        return self.__map

    def __zero_to_end(self):
        for i in range(-1, -len(self.__list_merge) - 1, -1):
            if self.__list_merge[i] == 0:
                del self.__list_merge[i]
                self.__list_merge.append(0)

    def __merge(self):
        self.__zero_to_end()
        for i in range(len(self.__list_merge) - 1):
            if self.__list_merge[i] == self.__list_merge[i+1]:
                self.__list_merge[i] += self.__list_merge[i+1]
                del self.__list_merge[i+1]
                self.__list_merge.append(0)

    def move_left(self):
        for line in self.__map:
            self.__list_merge = line
            self.__merge()

    def move_right(self):
        for line in self.__map:
            self.__list_merge = line[::-1]
            self.__merge()
            line[::-1] = self.__list_merge

    def move_up(self):
        self.matrix_reverse()
        self.move_left()
        self.matrix_reverse()

    def move_down(self):
        self.matrix_reverse()
        self.move_right()
        self.matrix_reverse()

    def matrix_reverse(self):
        for i in range(len(self.__map)):
            for j in range(i, len(self.__map)):
                self.__map[i][j], self.__map[j][i] = self.__map[j][i], self.__map[i][j]

    def run(self, dir):
        if dir == DirectionModel.UP:
            self.move_up()
        elif dir == DirectionModel.DOWN:
            self.move_down()
        elif dir == DirectionModel.LEFT:
            self.move_left()
        elif dir == DirectionModel.RIGHT:
            self.move_right()

    def get_empty_location(self):
        for i in range(len(self.__map)):
            for j in range(len(self.__map)):
                if self.__map[i][j] == 0:
                    self.__list_empty_location.append((i, j))

    def generate_number(self):
        self.get_empty_location()
        if len(self.__list_empty_location) == 0:
            return
        else:
            index = random.choice(self.__list_empty_location)

            self.__map[index[0]][index[1]] = 4 if random.randint(1, 10) > 9 else 2
            self.__list_empty_location.remove(index)

    def is_game_over(self):
        if len(self.__list_empty_location) > 0:
            return False

        for c in range(len(self.__map)):
            for r in range(self.__map[c]-1):
                if self.__map[c][r] == self.__map[c][r+1] or self.__map[r][c] == self.__map[r+1][c]:
                    return False
        return True


