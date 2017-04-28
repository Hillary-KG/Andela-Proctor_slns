'''You need to design an iterative and a recursive function called replicate_iter and replicate_recur respectively
which will receive two arguments: times which is the number of times to repeat and data 
which is the number or string to be repeated.

The function should return an array containing repetitions of the data argument. 
For instance, replicate_recur(3, 5) or replicate_iter(3,5) should return [5,5,5].
If the times argument is negative or zero, return an empty array. 
If the argument is invalid, raise a ValueError.'''


def replicate_iter(times,data):
    if isinstance(data,(float,int,str)):
    	retValue = []
    	while times>0:
    		retValue.append(data)
    		times = times-1
   		return retValue
    	else:
    		return []
    else:
        raise ValueError("Invalid input")

print replicate_iter(3,5)

def replicate_recur(times,data): 
    if(isinstance(data,(float,int,str))): 
        if(times>0): 
            retValue = replicate_recur(times-1,data)
            retValue.append(data)
            return retValue
        else:
            return []
    else:
        raise ValueError("Invalid input")


# def replicate_iter(times,data):
# 	retValue = []
# 	if not isinstance(data,(float,int,str)):
# 		raise ValueError("Invalid input")
# 	else:
# 		while times>0:
# 			retValue.append(data)
# 			times-=1
# 		else:
# 			return retValue
# 	return retValue

# def replicate_recur(times,data): 
# 	if(isinstance(data,(float,int,str))): 
# 		if(times>0): 
# 			retValue = replicate_recur(times-1,data)
# 			retValue.append(data)
# 			return retValue
# 		else:
# 			return []
# 	else:
# 		raise ValueError("Invalid input")


#+++++++++++++++++++++++++++++++++++++++++++++++++++++FINAL+++++++++++++++++++++++++++++++++++++++++++++++++++

def replicate_iter(times,data):
  if not isinstance(data ,(str, int , float)):
    raise ValueError("Invalid input")
  if not isinstance(times, int):
    raise ValueError("Invalid number of items to repeat")
  return [data for x in range(times)]


def replicate_recur(times,data,myList=None):
  if myList is None: myList=[]
  if not isinstance(data ,(str, int , float)):
    raise ValueError("Invalid input")
  if not isinstance(times, int):
    raise ValueError("Invalid number of items to repeat")
  if times <= 0:
    return myList
  else:
    myList.append(data)
    return replicate_recur(times-1,data,myList)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++FINAL+++++++++++++++++++++++++++++++++++++++++++++++++++
#function calls for the testing 
print replicate_recur(3,'j')
 print replicate_iter(3,5)