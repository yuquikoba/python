import pprint

q1=[[i*10+j for j in range(10,0,-1)] for i in range(9,-1,-1)]
pprint.pprint(q1)

q2=[[1 if i==j or i+j==4 else 0 for j in range(5)] for i in range(5)]
pprint.pprint(q2)

q3=[[i*10-j*10 for j in range(10)] for i in range(10)]
pprint.pprint(q3)
