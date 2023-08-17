import random
scores=[random.randint(0,100) for i in range(100)]
scores.sort(reverse=True)
result=scores[:10] #スライス
print(result)

"""
100人分の点数をランダムに生成
上位10件のデータを
降順に出力する
"""
scores=sorted([random.randint(0,100) for i in range(100)],reverse=True)[:10]
print(scores)

