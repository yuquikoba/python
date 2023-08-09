import random
count=0
LUCKY_NUM=7777
while True:
		count +=1
		num=random.randint(1,9999)
		print(f'{count}: {num}')
		if num==LUCKY_NUM:
				break
print(f'{count}回目に{LUCKY_NUM}が出ました')
