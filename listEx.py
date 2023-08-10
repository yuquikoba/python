import pprint
data=[[1,2,3],[4,5,6]]
print(data[1][2]) #6

data=[
	[1,2,3],
	[4,5,6],
]
print(data)

data=list()
for i in range(10):
		temp=list()
		for j in range(10):
				temp.append(0)
		data.append(temp)
pprint.pprint(data)

data=[1,2,3]+[4,5]
print(data) #[1,2,3,4,5]

data=[1,2,3]*3
print(data) #[1,2,3,1,2,3,1,2,3]

data=[None]*10
for i in range(len(data)):
		data[i]=[0]*10
pprint.pprint(data)

#内包表記
data=[[0]*10 for i in range(10)]
pprint.pprint(data)

ls=[n for n in range(1,8)]
print(ls) #[1,2,3,4,5,6,7]

ls=[n**2 for n in range(1,8)]
print(ls) #[1,4,9,16,25,36,49]

ls=[n for n in range(1,8) if n%2==0]
"""
イメージ
for n in range(1,8):
		if n%2==0:
				n
"""
print(ls) #[2,4,6]

ls=[i*10+j for i in range(1,3) for j in range(2,5)]
"""
for i in range(1,3):
		for j in range(2,5):
"""
print(ls) #[12,13,14,22,23,24]

ls=[[i*10+j for j in range(7,10)] for i in range(1,3)]
print(ls) #[[17,18,19],[27,28,29]]

ls=[[0 for j in range(10)] for i in range(10)]
ls=[[0 for j in range(10)] for i in range(10)]
ls=[[0]*10 for i in range(10)]
pprint.pprint(ls)

ls=[[i*10+j for j in range(1,11)] for i in range(0,10)]
pprint.pprint(ls)
