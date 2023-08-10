s1='Hello'
s2=s1[1:3]
print(s2) #el 部分文字列を切り出す(1以上3未満)

for c in s1:
		print(c)
# 文字列は配列同様

l1=[10,20,30,40,50]
l2=l1[1:4]
print(l2) #[20,30,40]

l2=l1[3:]
print(l2) #[40,50] (3以上)

l2=l1[:3]
print(l2) #[10,20,30] (3未満)

l2=l1[:] #l2の複製
print(l2) #[10,20,30,40,50]

l2=l1[-2:]
print(l2) #[40,50] (後ろから2番目から)

l2=l1[2:100]
print(l2) #[30,40,50] #添字の範囲外という概念はない

l1=[10,20,30,40,50,60,70,80]
l2=l1[1::2] #[20,40,60,80]

l2=l1[::-1]
print(l2) #[80,70,60,50,40,30,20,10] リバース


