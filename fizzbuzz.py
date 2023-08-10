for i in range(1,20+1):
		if i%3==0 and i%5==0:
				print('FizzBuzz')
		elif i%3==0:
				print('Fizz')
		elif i%5==0:
				print('Buzz')
		else:
				print(i)
				
msg='hello'
ls=list(msg)
print(ls) #文字から配列を作成

word=input('英単語>>')
word_list=list(word)
if len(word)==len(set(ls)):
		print('同じアルファベットは含まれていない')
else:
		print('同じアルファベットは含まれている')
