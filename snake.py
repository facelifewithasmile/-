from bug import Bug
# 蛇的类。
class Snake:
    def __init__(self):
        self.__list = [(2, 2)]
        self.__toward = (0, 1)  # 向右走 行不变列加一
        self.__lock = False    # 加操作锁


    #让蛇来控制速度
    @property
    def sleep_time(self):
        x = 10 - len(self.__list) * 1
        if x < 1:
            x = 1
        return x / 10

    # 让蛇来记分
    @property
    def score(self):
        return len(self.__list) * 100 - 100


    # 蛇的转向 可能是UP  DOWN LEFT RIGHT

    def set_toward(self, new_toward):
        if self.__lock:
            return
        dictionary = {
            "UP": (-1, 0),
            "DOWN": (1, 0),
            "LEFT": (0, -1),
            "RIGHT": (0, 1)
        }
        target_toward = dictionary[new_toward]   # target_toward 目标方向
        if (target_toward[0] + self.__toward[0] == 0) and\
                (target_toward[1] + self.__toward[1] == 0):
            return
        self.__toward = dictionary[new_toward]
        self.__lock = True

    #返回蛇的坐标
    @property
    def points(self):
        return self.__list

    # 编写蛇某一帧的行为，帧指的是屏幕一次刷新
    def action(self, bug: Bug, wall_points):
        self.__move()
        self.__eat(bug)
        return self.__dear(wall_points)

    # 走
    def __move(self):
        for i in range(len(self.__list) - 1, 0, -1):
            self.__list[i] = self.__list[i - 1]

        # 蛇头坐标是蛇头原坐标加上方向坐标
        self.__list[0] = (self.__list[0][0] + self.__toward[0],
                          self.__list[0][1] + self.__toward[1])
        self.__lock = False   # 蛇走了一步就解锁

    # 吃
    def __eat(self, bug: Bug):
        # 头的坐标和虫子的坐标一样就发生吃
        if self.__list[0] == bug.point[0]:
            # 虫子瞬移
            bug.quicly_move(self.__list)
            # 蛇加长
            self.__list.append(self.__list[-1])

    # 死
    def __dear(self, points):
        # 判断撞墙
        if self.__list[0] in points:
            return True
        # 判断撞自己
        if self.__list[0] in self.__list[2:]:
            return True
        return False

