'''
진행 상태를 보여주는 상태바
프로그래스바도 ttk를 통해서 만들 수 있다.
'''

import tkinter.ttk as ttk
from tkinter import *

import time

root = Tk()
root.title('연습용 gui')
root.geometry('640x480')

# progressbar = ttk.Progressbar(root, maximum=100, mode='indeterminate') # 100%를 최대값으로 함 # indeterminate는 끝을 알수 없는 상태
# progressbar = ttk.Progressbar(root, maximum=100, mode='indeterminate') # 100%를 최대값으로 함 # determinate는 왼쪽부터 쭉~ 체워감

# progressbar.start(10) # 단위는 ms
# progressbar.pack()

# def btncmd():
#     progressbar.stop() # 작동 중지

# btn = Button(root, text='클릭', command=btncmd)
# btn.pack()
p_var2 = DoubleVar() # 실수형 변수
progressbar_2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2) # length는 진행바 크기
progressbar_2.pack()

def btncmd2():
    for i in range(101):
        time.sleep(0.05)

        p_var2.set(i)
        progressbar_2.update() # 변화 상태를 즉시 반영함. 함수안에 있기 때문에 사용해야함.
        print(p_var2.get())

btn = Button(root, text='시작', command=btncmd2)
btn.pack()

root.mainloop()
