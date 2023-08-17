num=int(input('正の整数を入力してください'))
total=0
for i in range(1,num+1):
		total+=i
print(f'{num}までの整数の和は{total}です')

print(sum(range(1,num+1)))
