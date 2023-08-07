scores={'network':60,'database':80,'security':60}
members=['松田','浅木','工藤']
tp1=tuple(members) #リストmembersを使用してタプルを生成(タプルコンストラクタ)
print(tp1)
ls1=list(scores) #scoresのキーを集めたlistを生成(listコンストラクタ)
print(ls1)
set1=set(scores.values()) #scoresのvalueを使用してsetを生成(セットコンストラクタ)
print(set1)

codes=['#ff0000','#00ff00','F0000ff']
colors=['red','blue','green']
dict1=dict(zip(codes,colors))
print(dict1)
