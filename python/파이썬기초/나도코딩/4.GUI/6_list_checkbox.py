'''
체크박스
'''

from tkinter import *

root = Tk()
root.title("test gui")
root.geometry("690x450")

ckvar = IntVar() # 체크바에 int형을 값을 저장
ckbox = Checkbutton(root, text='오늘 하루 보지않기', variable=ckvar)
ckbox.select() # 기본으로 선택으로 만들기
ckbox.deselect() # 기본으로 선택 해제됨
ckbox.pack()

ckvar2 = IntVar()
ckbox2 = Checkbutton(root, text='일주일 동안 보지 않기', variable=ckvar2)
ckbox2.pack()

def btncmd():
    print(ckvar.get()) # 0: 체크해제, 1: 체크

btn = Button(root, text='클릭', command=btncmd)
btn.pack()

root.mainloop()