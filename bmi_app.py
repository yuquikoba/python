height=input('身長(cm)を入力してください >>')
weight=input('体重(kg)を入力してください >>')
height=float(height)/100
weight=float(weight)
bmi=weight/(height**2)
print(f'BMI: {bmi:.1f}')
if bmi>=25:
		result='肥満'
elif bmi>=18.5:
		result='標準'
else:
		result='痩せ'
print(result)
