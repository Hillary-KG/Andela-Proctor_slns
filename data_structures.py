'''Write a function called manipulate_data which will act as follows:

When given a list of integers, return a list, where the first element is the count of positives numbers 
and the second element is the sum of negative numbers.

'''
def manipulate_data(myList):
	newlist = []
	count=0
	sumNeg=0
	if isinstance(myList,list):
		for i in range(0,len(myList)):
			if myList[i]>0:
				count+=1
			if myList[i]<0:
				sumNeg+=myList[i]
	newlist = [count,sumNeg]
	return newlist
mlist = [2,-3,4,6,-4,-1,5,6]

#functional call for testing 
print manipulate_data(mlist)
