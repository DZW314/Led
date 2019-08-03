#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'DZW'
__mtime__ = '2019/8/1'
# code is far away from bugs with the god animal protecting
    I love animals. They are so funny. 
             ┏┓   ┏┓
            ┏┛┻━━━┛┻┓
            ┃   *   ┃
            ┃ ┳┛ ┗┳ ┃
            ┃   ┻   ┃
            ┗━┓   ┏━┛
              ┃   ┗━━━┓
              ┃ Bless ┣┓
              ┃ NoBUG ┏┛
              ┗┓┓┏━┳┓┏┛
               ┃┫┫ ┃┫┫
               ┗┻┛ ┗┻┛
"""
import tkinter
global num
num = 0
def func():
    print("Hello,world!")
#    num += 1
    print(num)
    return num

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("LED SHOW!")
#设置大小和位置
win.geometry("1000x500+20+50")
#进入消息循环

# Label参数定义
# win：父窗体
# text：显示的文本内容
# bg：背景色
# fg：字体颜色
# font：字体
# wraplength：指定text文本中多宽之后换行
# justify：设置换行后的对齐方式
# anchor：位置 n北，e东，w西，s南，center居中；还可以写在一起：ne东北方向
label = tkinter.Label(win,
                      text="The number is " + str(num),
                      bg="pink", fg="red",
                      font=("黑体",8),
                      width=20,
                      height=10,
                      wraplength=100,
                      justify="left",
                      anchor="nw")
label.pack()

#Button控件
button1 = tkinter.Button(win, text="按钮", command=func(), width=5, height=2)
button1.pack()

button2 = tkinter.Button(win, text="按钮", command=lambda: print("hahahahaha"))
button2.pack()

button3 = tkinter.Button(win, text="退出", command=win.quit)
button3.pack()

#Entry控件
#密文显示
entry1 = tkinter.Entry(win, show="*")
entry1.pack()

#绑定变量
e = tkinter.Variable()
entry2 = tkinter.Entry(win, textvariable=e)
entry2.pack()

e.set(num)
print(e.get())
print(entry2.get())

#点击按钮输入输出框中的内容
def showinfo():
    print(entry.get())

entry = tkinter.Entry(win)
entry.pack()

button = tkinter.Button(win, text = "按钮", command=showinfo)
button.pack()


#Text控件
#height表示的是显示的行数
# text = tkinter.Text(win, width=30, height=10)
# text.pack()
# str = "希，望，一，切，顺，利！"
# text.insert(tkinter.INSERT, str)
#
# #创建菜单
# menubar = tkinter.Menu(win)
# win.config(menu=menubar)
# menu1 = tkinter.Menu(menubar, tearoff=False)
# #给菜单选项添加内容
# for item in ['python','c','java','quit']:
#     if item == 'quit':
#         menu1.add_separator()
#         menu1.add_command(label=item, command=win.quit)
#     else:
#         menu1.add_command(label=item, command=func)
# menu1.add_cascade(label='语言', menu=menu1)



win.mainloop()
