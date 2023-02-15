'''
라디오 버튼 : 여러 리스트 중 택 1
'''

from tkinter import *

root = Tk()
root.title('test gui')
root.geometry('680x450')

Label(root, text='메뉴를 선택하세요').pack()

# 라디오 버튼 변수
burger_var = IntVar()
btn_burger1 = Radiobutton(root, text='햄버거', value=1, variable=burger_var)
btn_burger2 = Radiobutton(root, text='치킨버거', value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text='새우버거', value=3, variable=burger_var)

btn_burger1.select() # 기본으로 선택값 설정

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

drink_var = StringVar()
btn_drink1 = Radiobutton(root, text='콜라',  value='1', variable=drink_var)
btn_drink2 = Radiobutton(root, text='사이다',  value='2', variable=drink_var)
btn_drink3 = Radiobutton(root, text='환타',  value='3', variable=drink_var)

btn_drink1.select()

btn_drink1.pack()
btn_drink2.pack()
btn_drink3.pack()

def btncmd():
    print(burger_var.get()) # 선택된 값을 반환(value)
    print(drink_var.get())

btn = Button(root, text='주문', command=btncmd)
btn.pack()

root.mainloop()
