import tkinter
import time
import wall
import option


class Displayer:
    def __init__(self):
        # 创建一个装标签坐标点（x，y）的点的集合
        self.__list = []
        self.__window = None
        self.__label = None

    def add_window(self, title,length=option.length, width=option.width):
        self.__window = tkinter.Tk()  # 打开一个窗口
        self.__window.title("{}".format(title))  # 设置标题
        self.__window.geometry('{}x{}'.format(length, width))   # 设置大小
        self.add_label()
        self.__window.mainloop()  # 进入消息循环

    var = tkinter.StringVar()
     # 创建墙的按钮
    def add_label(self, point=wall.Wall().points, ):
        global var
        a, b = point[1][0], point[1][1]
        l = tkinter.Label(self.__window, textvariable=var, bg='black', font=('黑体', 2), width=2, height=2)

        # 相当于start，将标签显示到屏幕上
        l.pack()

        count = 0

        def print_hello_world():
            global count
            count += 1
            var.set("点击了{}次".format(count))
            l.place(x=50, y=300)  # 修改了l的位置

        # 创建button
        w = tkinter.Button(self.__window, text='上', font=('Arial', 12), width=5, height=2, command=print_hello_world)
        w.pack()
        w.place(x=450, y=500)
        s = tkinter.Button(self.__window, text='下', font=('Arial', 12), width=5, height=2, command=print_hello_world)
        s.pack()
        s.place(x=450, y=550)
        a = tkinter.Button(self.__window, text='左', font=('Arial', 12), width=5, height=2, command=print_hello_world)
        a.pack()
        a.place(x=380, y=550)
        d = tkinter.Button(self.__window, text='右', font=('Arial', 12), width=5, height=2, command=print_hello_world)
        d.pack()
        d.place(x=520, y=550)
        m = tkinter.Button(self.__window, text='开始游戏', font=('Arial', 12), width=10, height=1, command=print_hello_world)
        m.pack()
        m.place(x=25, y=510)
        n = tkinter.Button(window, text='结束游戏', font=('Arial', 12), width=10, height=1, command=print_hello_world)
        n.pack()
        n.place(x=25, y=560)




displayer = Displayer()
displayer.add_window("【游戏】贪吃蛇")
displayer.add_label()





# 创建墙
















# 创建定时器，1秒钟执行print_hello_world一次



# 作业:
# 通过图形介面，贪食蛇，扫雷
# https://blog.csdn.net/ahilll/article/details/81531587
# 查字典