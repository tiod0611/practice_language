'''
리스트 박스

여러줄에 거쳐 목록을 관리하는 위젯
'''

from tkinter import *

root = Tk()
root.title("practice GUI")
root.geometry("680x540") # 가로세로 크기 지정

listbox = Listbox(root, selectmode='extended', height=0) # height는 보여지는 목록 개수. 0은 모두 보기
# selectmode
# extended : 여러개 선택 가능
# single : 하나만 선택 가능

listbox.insert(0, '1')
listbox.insert(1, '2')
listbox.insert(2, '3')
listbox.insert(END, '4') # END로 지정하면 무조건 마지막에 추가함.
listbox.insert(END, '5')
listbox.pack()

def btncmd():
    # 삭제하는 버튼
    # listbox.delete(END) #맨 뒤를 삭제, 숫자를 넣으면 INDEX 번호로 삭제

    # 갯수 확인 버튼
    # print(listbox.size())

    #항목 확인(시작, 끝)
    print("항목 범위를 지정해서 확인", listbox.get(0, 2)) # 반환은 tuple

    # 사용자가 선택한 항목 확인
    print('선택된 항목: ', listbox.curselection())


btn = Button(root, text='클릭', command=btncmd)
btn.pack()


root.mainloop()