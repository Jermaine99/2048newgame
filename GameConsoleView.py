from GameController import GameController
from Model import DirectionModel


class GameConsoleView:
    def __init__(self):
        self.__controller = GameController()

    def main(self):
        self.__start()
        self.__update()

    def __start(self):
        self.__controller.generate_number()
        self.__controller.generate_number()
        self.__draw()

    def __draw(self):
        for line in self.__controller.map:
            for item in line:
                print(item, end=" ")
            print()

    def __update(self):
        while True:
            self.__move_map()
            self.__controller.generate_number()
            self.__draw()
            if self.__controller.is_game_over():
                print("游戏结束")
                break

    def __move_map(self):
        dir = input("请输入方向：wsad:\n")
        dict_dir ={
            "w": DirectionModel.UP,
            "s": DirectionModel.DOWN,
            "a": DirectionModel.LEFT,
            "d": DirectionModel.RIGHT
        }

        if dir in dict_dir:
            self.__controller.run(dict_dir[dir])



game1 = GameConsoleView()
if __name__ == '__main__':
    game1 = GameConsoleView()
    game1.main()
