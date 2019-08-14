import tkinter
import time
import wall

window = tkinter.Tk()  # 打开一个窗口
# 设置标题
window.title("贪吃蛇")
# 设置大小
window.geometry('600x600')

# 字符串变量
var = tkinter.StringVar()


# 通过Label(标签)在窗口中添加文字

# 说明： bg为背景，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高
l = tkinter.Label(window, textvariable=var, bg='black', font=('黑体', 2), width=2, height=2)

# 相当于start，将标签显示到屏幕上
l.pack()

count = 0
def print_hello_world():
    global count
    count += 1
    var.set("点击了{}次".format(count))
    l.place(x=50, y=300)        # 修改了l的位置


# 创建button
w = tkinter.Button(window, text='上', font=('Arial', 12), width=5, height=2, command=print_hello_world)
w.pack()
w.place(x=450, y=500)
s = tkinter.Button(window, text='下', font=('Arial', 12), width=5, height=2, command=print_hello_world)
s.pack()
s.place(x=450, y=550)
a = tkinter.Button(window, text='左', font=('Arial', 12), width=5, height=2, command=print_hello_world)
a.pack()
a.place(x=380, y=550)
d = tkinter.Button(window, text='右', font=('Arial', 12), width=5, height=2, command=print_hello_world)
d.pack()
d.place(x=520, y=550)
m = tkinter.Button(window, text='开始游戏', font=('Arial', 12), width=10, height=1, command=print_hello_world)
m.pack()
m.place(x=25, y=510)
n = tkinter.Button(window, text='结束游戏', font=('Arial', 12), width=10, height=1, command=print_hello_world)
n.pack()
n.place(x=25, y=560)

# 进入消息循环
window.mainloop()

# 创建墙
















# 创建定时器，1秒钟执行print_hello_world一次



# 作业:
# 通过图形介面，贪食蛇，扫雷
# https://blog.csdn.net/ahilll/article/details/81531587
# 查字典