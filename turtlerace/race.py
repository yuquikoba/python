import random
import turtle
#亀配列
ts=['blue','red','yellow','pink','green',]

def setup():
		global ts
	#画面生成
		screen=turtle.Screen()
	#画面サイズ
		screen.setup(1290,720)
	#背景画像設定
		screen.bgpic('pavement.gif')
	#スタートのx座標
		startline=-620

		for i in range(len(ts)):
				t=turtle.Turtle() #亀インスタンスの生成
				t.shape('turtle')
				t.color(ts[i]) #亀の色設定
				t.penup() #最初は線の描画はしない
				t.setpos(startline,(len(ts)//2)*-40+40*i) #亀のスタート位置
				t.pendown() #以降は線を描画
				ts[i]=t #リストを更新

def race():
	global ts
	finishline=540

	while True:
			for current_t in ts:
					move=random.randint(0,20) #亀のx座標取得
					current_t.forward(move)
					#ゴールしたかの判定
					x=current_t.xcor()
					if x>=finishline:
							winner_color=current_t.color() #色取得
							#文字の描画(内容,font(種類,大きさ,ウエイト))
							current_t.write('Win!'+winner_color[0],font=('Arial',16,'bold'))
							return #いずれかがゴールしたら関数を抜ける

setup()
race()
turtle.mainloop()
