'''
텍스트를 입력할 수 있는 텍스트와 entry
'''

from tkinter import *

root = Tk()
root.geometry("640x580")

# 텍스트 위젯 생성
txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END, '글자를 입력하세요.')

e = Entry(root, width=30) # 한줄로 입력받을 때 사용.
e.pack()
e.insert(0, "한줄만 입력해요.")

def btncmd():
    print(txt.get("1.2", END)) # 1.0 의미: 1은 LINE 위치, 0은 column 위치
    print(e.get())

    # 값 삭제
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text='click', command=btncmd)
btn.pack()

root.mainloop()