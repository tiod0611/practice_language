'''
레이블

글자나, 이미지를 보여준다. 동작은 없다.
'''


from tkinter import *

root = Tk()
root.title("Gyeul GUI")

label1 = Label(root, text='안녕하세요')
label1.pack() 

photo = PhotoImage(file='img.png')
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text='Good bye')

    # 전역변수로 설정해줘야 함.
    global photo2
    photo2 = PhotoImage(file='img2.png')
    label2.config(image=photo2)
btn = Button(root, text='click', command=change)
btn.pack()

root.mainloop()