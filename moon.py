dist=384400*1000*1000
thickness=1
count=0

while thickness < dist:
		thickness *=2
		count +=1
		print(count,'回折り曲げた','厚み:',thickness)
