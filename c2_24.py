matsuda_scores={'network':60,'database':80,'security':50}
asagi_scores={'network':80,'database':75,'security':92}
member_scores={
	'松田':matsuda_scores,
	'浅木':asagi_scores
}
#松田のdatabaseの点数を出力
print(member_scores['松田']['database'])
