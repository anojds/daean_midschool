import tkinter # tkinter 모듈물러오기

window=tkinter.Tk() # tk 선언


text=tkinter.Text(window) # 텍스트 담을 변수 선언

text.insert(tkinter.CURRENT, "안녕하세요.\n") # 방금 만든 text 변수에 텍스트값 삽입

text.pack() # 프로그램에 text 띄우기
window.mainloop() # 프로그램이 종료되지 않게 
