import option
# 墙的类，创建墙的类
class Wall:
    def __init__(self):
        self.__list = []
        self.__wall_piont()

    # 创建代表墙的一组坐标
    def __wall_piont(self):
        for i in range(option.length):
            # 创建第一行
            self.__list.append((0, i))
            self.__list.append((option.width - 1, i))
        for j in range(option.width):
            self.__list.append((j, 0))
            self.__list.append((j, option.length - 1))

     # 返回墙的坐标
    @property
    def points(self):
        return self.__list


