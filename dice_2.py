import random
print('サイコロ振ったよ')
num=list()
for i in range(2):
		num.append(random.randint(1,6))
		print(f'{i+1}回目: {num[i]}')
		
diff=num[0]-num[1]
if diff==0:
		print('2回目は1回目と同じです')
elif diff >0:
		print(f'2回目は1回目より{diff}大きいです')
else:
		print(f'2回目は1回目より{abs(diff)}小さいです')
