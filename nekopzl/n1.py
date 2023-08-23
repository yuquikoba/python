import tkinter as tk
mouse_x=0
mouse_y=0
mouse_c=0

def mouse_move(e):
		global mouse_x,mouse_y
		mouse_x=e.x
		mouse_y=e.y

def mouse_press(e):
		global mouse_c
		mouse_c=1

def mouse_release(e):
		global mouse_c
		mouse_c=0

def game_main():
		fnt=('Arial',30)
		txt=f'mouse({mouse_x},{mouse_y}){mouse_c}'
		cvs.delete('TEST') #文字を消去
			#文字を出力
		cvs.create_text(456,384,text=txt,fill='black',font=fnt,tag='TEST')
		root.after(100,game_main)

root=tk.Tk()
root.title('マウス入力')
root.resizable(False,False)
root.bind('<Motion>',mouse_move) #マウスが動いたときのイベント
root.bind('<ButtonPress>',mouse_press) #マウクリックしたときのイベント
root.bind('<ButtonRelease>',mouse_release) #マウスボタンを離したときのイベント
cvs=tk.Canvas(root,width=912,height=768)
cvs.pack()
game_main()
root.mainloop()
