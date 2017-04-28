# def calculate_tax(**data):
# 	taxOne=0
# 	taxTwo=0
# 	taxThree=0
# 	taxFour=0
# 	taxFive=0
# 	taxSix=0
# 	for key in data:
# 		salary = data[key]
# 		if salary > 0 and salary <= 1000:
# 			taxOne = 0
# 		elif salary > 1000 and salary <= 10000:
# 			taxTwo = 9000*0.1
# 			# salary -= 9000
# 		elif salary > 10000 and salary <= 20200:
# 			taxThree = 10200*0.15
# 			# salary -= 10200
# 		elif salary > 20200 and salary <= 30750:
# 			taxFour = 10550*0.2
# 			# salary -= 10550
# 		elif salary > 30750 and salary <= 50000:
# 			taxFive = 19250*0.25
# 			# salary -= 19250
# 		elif salary > 50000:
# 			taxSix = (salary-50000)*0.3
# 		total_tax = taxOne+taxTwo+taxThree+taxFour+taxFive+taxSix
# 		data[key]=total_tax
# 	return data
	
# myData = {'Alex':500,
# 		'James':20500,
# 		'Kinuthia':70000
# 		}
# print(calculate_tax(**myData))
def calculate_tax(myDict):
	try:
		for person in myDict:
			income_need_to_pay_tax = myDict[person]
			tax = 0
			while income_need_to_pay_tax > 1000:
				if income_need_to_pay_tax > 50000:
					income_in_tax_base = income_need_to_pay_tax - 50000
					income_need_to_pay_tax -= income_in_tax_base
					tax += income_in_tax_base*0.3
				elif income_need_to_pay_tax > 30750:
					income_in_tax_base = income_need_to_pay_tax - 30750
					income_need_to_pay_tax -= income_in_tax_base
					tax += income_in_tax_base*0.25
				elif income_need_to_pay_tax > 20200:
					income_in_tax_base = income_need_to_pay_tax - 20200
					income_need_to_pay_tax -= income_in_tax_base
					tax += income_in_tax_base*0.2
				elif income_need_to_pay_tax > 10000:
					income_in_tax_base = income_need_to_pay_tax - 10000
					income_need_to_pay_tax -= income_in_tax_base
					tax += income_in_tax_base*0.15
				elif income_need_to_pay_tax > 1000:
					income_in_tax_base = income_need_to_pay_tax - 1000
					income_need_to_pay_tax -= income_in_tax_base
					tax += income_in_tax_base * 0.1
			    	myDict[person]=tax
			else:
				myDict[person] = tax
		return myDict
	except (AttributeError,TypeError):
		raise ValueError('The provided input is not a dictionary')

#myData = {'Alex':500,'James':20500,'Kinuthia':70000}
#FUNCTION CALL 
print(calculate_tax({'Alex':500,'James':20500,'Kinuthia':70000}))

# def bubble_sort(*myList):
# 	i=0
# 	while i <=2:
# 		for i in myList:
# 			if myList[i] > myList[i+1]:
# 				temp = myList[i+1]
# 				mList
# 			print(myList)
# mList = [19, 1, 9, 7, 3, 10, 13, 15, 8, 12]
# bubble_sort(mList)