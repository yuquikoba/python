import random
import pprint
#内包表記
ls=[i for i in range(1,11)] #1~10までの値でリストを作成
print(ls)

ls=[i**2 for i in range(1,11)] #iを二乗した値でリストを作成

#サイコロを3回振ったときの出目をリストにする
dices=[random.randint(1,6) for i in range(3)]
print(dices) 

ls=[str(i) for i in range(1,11)] #文字列としてリストを作成
print(ls) #['1','2','3'.......'10']

#文字列のリストをintに変換
ls=[int(i) for i in ls]
ls=[i for i in range(1,10) if i%2==0] #偶数のみでリストを作成
print(ls)

"""
ls=[]
for i in range(1,10):
		if i%2==0:
				ls.append(i)
"""

ls=[i*j for i in range(1,3) for j in range(1,3)]
print(ls) #[1,2,2,4]

ls=[i*j for i in range(5,9) for j in range(1,3)]
print(ls)
ls=[i*j for i in range(1,3) for j in range(5,9)]
print(ls)

ls=[[i]*3 for i in range(1,4)]
print(ls) #[1,1,1],[2,2,2].[3,3,3]
"""
ls=[]
for i in range(3):
		ls.append([i]*3)
"""
ls=[[i*j for j in range(3)] for i in range(3)]
print(ls) #[[0,0,0],[0,1,2],[0,2,4]]
"""
ls=[]
for i in range(3):
		temp=[]
		for j in range(3):
				temp.append(i*j)
		ls.append(temp)
"""
ls=[[i*j for j in range(1,9+1)] for i in range(1,9+1)]
pprint.pprint(ls)

# 3 5を受け取る
st1=input()
st1=st1.split(' ')
nums=[int(i) for i in ls1]
a,b=[int(i) for i in ls1] #a=3,B=5

data=[int(i) for i in input().split(' ')]
n1,n2=[int(i) for i in input().split(' ')]






