def analyze_scores(sansu,kokugo,rika,syakai,eigo=None,*others):
		scores=[sansu,kokugo,rika,syakai]
		if eigo!=None:
				scores.append(eigo)
		scores=scores+list(others)
		max_score=max(scores)
		min_score=min(scores)
		avg_score=sum(scores)/len(scores)
		return[max_score,min_score,avg_score]

print(analyze_scores(80,80,80,80,80,80,70,70,45,12))
