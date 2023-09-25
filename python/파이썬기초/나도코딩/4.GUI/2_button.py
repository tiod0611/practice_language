from tkinter import *

root = Tk()
root.title("Gyeul GUI")

btn1 = Button(root, text="버튼1") # 버튼 속성
btn1.pack() # 버튼 생성

# 버튼 크기 지정
# pad : 내용에 따른 상대적 크기
btn2 = Button(root, padx=5, pady=10, text='버튼2')
btn2.pack()

btn2 = Button(root, padx=20, pady=30, text='버튼버튼버튼버튼버튼버튼버튼버튼버튼버튼')
btn2.pack()

# 절대적으로 크기 수정
btn4 = Button(root, width=10, height=3, text='버튼4')
btn4.pack()

btn4 = Button(root, width=10, height=3, text='버튼버튼버튼버튼버튼버튼') # 크기가 절대값이기 때문에 넘어가는 글자는 그냥 잘림
btn4.pack()

# 버튼 색상 입히기
btn5= Button(root, fg='red', bg='yellow', text='버튼5')
btn5.pack()

# 이미지로 버튼 만들기
photo = PhotoImage(file='img.png')
btn6 = Button(root, image=photo)
btn6.pack()

def btncmd():
    print("버튼이 클릭되었습니다.")

# 버튼 동작시키기
btn7 = Button(root, text='동작하는 버튼', command=btncmd)
btn7.pack()


root.mainloop()