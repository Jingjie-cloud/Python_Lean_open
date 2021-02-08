import tkinter as tk
from tkinter.messagebox import *
import random
import threading
import time
import sys


aaa = '电脑崩溃中...'
def boom():

    window = tk.Tk()
    width = window.winfo_screenwidth()
    heigh = window.winfo_screenheight()
    w = random.randrange(0, width)
    h = random.randrange(0, heigh)
    window.title('严君泽真香警告！')
    window.geometry('250x100+'+str(w)+'+'+str(h))
    tk.Label(window, text=aaa, fg='red', bg='white', font=('宋体', 16),
             width=20, heigh=4).pack()
    window.mainloop()

def mess():
    ask = askyesno('警告！', '是男人就点是！')
    global aaa
    if ask == True:
        showinfo('牛批！', '继续！')
        aaa = '电脑放假中...'


    elif ask == False:
        showinfo('TMD', '你这也算男人？！')
        aaa = '电脑觉得你是个娘炮！'


def thread(tar):
    threads = []
    for i in range(random.randint(5, 10)):
        t = threading.Thread(target=tar)
        threads.append(t)
        time.sleep(0.5)
        threads[i].start()



if __name__ == '__main__':
    try:
        while True:
            thread(boom)
            mess()
    except KeyboardInterrupt:
        sys.exit()


