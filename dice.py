import random
#空のリスト作成 dice_list=[]も可
dice_list=list()
num=int(input('何回振る?>>'))
#ループの回数のみが必要なので_がbetter
for _ in range(num):
		dice=random.randint(1,6)
		dice_list.append(dice)
		#dice_list.append(random.randint(1,6))
print(dice_list)
print(f'合計は{sum(dice_list)}でした')
print(f'最大は{max(dice_list)}でした')
print(f'最小は{min(dice_list)}でした')

num=int(input('何回振る?>>'))
dice_list=[random.randint(1,6) for _ in range(num)]
print(dice_list)
print(f'合計は{sum(dice_list)}でした')

