import option
import os
# 显示管理类，根据坐标，显示一个nxn的点阵图
class Displayer:
    # init 方法  把有坐标的打印出来
    def __init__(self):
        # 创建一个装坐标点（x，y）的点的集合
        self.__list = []

    # 导入一个需要显示的坐标点数据
    def extend_point(self,point_list):
        self.__list.extend(point_list)

    # 清空这一帧的数据
    def clear(self):
        self.__list.clear()

    # 打印点阵图
    def draw_graphics(self, score):
        os.system("cls")    # 清屏  然后打印
        print("".center(option.length * 2, "*"))
        print(("score:%d" % score).center(option.width * 2, " "))
        print("".center(option.length * 2, "*"))

        for i in range(option.width):   # i 代表行  j  代表列
            for j in range(option.length):
                if (i, j) in self.__list:
                    print("国", end="")
                else:
                    print("  ", end="")  # 中文字占两个空格
            print()

