import random
import option

# 虫子类
class Bug:
    def __init__(self, points):
        self.__point = None
        self.quicly_move(points)

    # 随机生成一个坐标
    def quicly_move(self,points: list):
        while True:
            row = random.randint(1, option.width - 3)
            col = random.randint(1, option.length- 3)
            if (row, col) not in points:
                break
        self.__point =  (row, col)

    # 返回虫子的坐标
    @property
    def point(self):
        return [self.__point]  # 因为displayer传入需要列表，故把点放列表里