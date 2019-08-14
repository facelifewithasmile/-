# 入口模块
from wall import Wall
from displayer import Displayer  # 前面是包名  后面是类名
from snake import Snake
import time
import threading
import msvcrt
from bug import Bug

displayer =Displayer()         # 创建显示管理类的对象
wall = Wall()                 # 创建墙的对象
snake = Snake()               # 创建蛇的对象
bug = Bug(snake.points)       # 创建虫子的对象



running = True
class InputThread(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        global running, snake
        while running:
            c = str(msvcrt.getch())   # 输入读取  无需回车
            if c == "b'q'":
                running = False
            elif c == "b'w'":
                snake.set_toward("UP")
            elif c == "b's'":
                snake.set_toward("DOWN")
            elif c == "b'a'":
                snake.set_toward("LEFT")
            elif c == "b'd'":
                snake.set_toward("RIGHT")



input_thread = InputThread()
input_thread.start()      # 启动子线程，负责输入读取


while running:
    death = snake.action(bug, wall.points)
    if death:
        print("小蛇死了，\n按Q键退出")
        break

    displayer.extend_point(wall.points)
    displayer.extend_point(snake.points)
    displayer.extend_point(bug.point)

    # 绘制图像
    displayer.draw_graphics(snake.score)
    displayer.clear()    # 清空这一帧的数据
    time.sleep(snake.sleep_time)

