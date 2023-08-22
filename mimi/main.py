import tkinter as tk
key=''
#引数にイベントオブジェクトが渡される イベントリスナー
def key_down(e):
		global key
		#e.keysymで押したボタンの名前を取得
		key=e.keysym

def key_up(e):
		global key
		key=''

cx=400
cy=300
#移動処理
def main_proc():
		global cx,cy
		if key=='Up':
				cy=cy-20
		if key=='Down':
				cy=cy+20
		if key=='Left':
				cx=cx-20
		if key=='Right':
				cx=cx+20
		#coordsは表示中の画像を新しい位置へ移動する
		canvas.coords('MYCHR',cx,cy)
		#afterは指定時間後に処理を実行する(ms,処理)
		root.after(100,main_proc)

root=tk.Tk()
root.bind('<KeyPress>',key_down) #キーを押したときのイベントをバインド
root.bind('<KeyRelease>',key_up) #キーを話したときのイベントをバインド
canvas=tk.Canvas(width=800,height=600,bg='Lightgreen')
canvas.pack()
img=tk.PhotoImage(file='mimi.png')
#作った画像にMYCHRというタグを付与
canvas.create_image(cx,cy,image=img,tag='MYCHR')
main_proc()
root.mainloop()
