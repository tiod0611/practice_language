'''
콤보 박스 (드랍박스)
창을 열어서 여러 목록 중 하나를 선택함.

'''
import tkinter.ttk as ttk # 콤보 박스용 모듈 
from tkinter import *

root = Tk()
root.title('연습용 쥐유아이')
root.geometry('640x480')

values = [str(x) + '일' for x in range(1, 32)]
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()

combobox.set('카드 결제일 선택') # 기본 문구 설정

# 드랍 박스 안에서만 선택할 수 있음, state='readonly'
values1 = [str(x) + '일' for x in range(1, 32)]
ro_combobox = ttk.Combobox(root, height=5, values=values1, state='readonly')
ro_combobox.pack()

ro_combobox.set('카드 결제일 선택') # 기본 문구 설정

def btncmd():
    print(combobox.get()) # 선택된 값을 출력
    print(ro_combobox.get())

btn = Button(root, text='버튼', command=btncmd)
btn.pack()

root.mainloop()