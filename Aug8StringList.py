# def alternatingSum(myList): 
# 	answer = 0 
# 	for i in range(0, len(myList)): 
# 		if i % 2 == 0: 
# 			answer += myList[i]
# 		else: 
# 			answer -= myList[i]
# 	return answer

# # print(alternatingSum([5,3,8,4]))

# def alternatingSum2(myList): 
# 	positives = myList[::2] 
# 	negatives = myList[1::2]
# 	return sum(positives) - sum(negatives)


# myList = [1,2,3,4,5,6,7]
# # myList.insert(1, 'a')
# # print(myList)

# print(myList[2: :2])



# import copy 
# def median(a):
# 	b = copy.copy(a)
# 	List = sorted(a)
# 	index = len(List)//2

# 	if len(List) % 2 == 1:
# 		return List[index]
# 	else:
# 		return (List[index -1] + List[index]) / 2
# print(median([5,3,1,9,7]))




# def median2(b): 
# 	a = copy.copy(b)
# 	for i in range(0, len(a) - 1): 		# 1st 
# 		for j in range(i + 1, len(a)): 		# 2nd 
# 			if a[i] > a[j]: 
# 				a[i],a[j] = a[j], a[i]		# switching the order 


# def smallestDifference(a): 
# 	minDiff = 10 ** 2000 
# 	for i in range(0, len(a) - 1): 
# 		for j in range(i + 1, len(a)): 
# 			if abs(a[i] - a[j]) < minDiff: 
# 				minDiff = abs(a[i] - a[j])
# 	return minDiff


# print( smallestDifference([19,2,83,6,27]))



def removeRepeat(L): 
	newList = []
	for i in range(0, len(L)): 
		if L[i] not in newList: 
			newList.append(L[i])
	return newList

# print(removeRepeat([1,2,4,4,2,9,76]))


def removeRepeat2(L): 
	for i in range(len(L) - 1, - 1, - 1): 
		if L.count(L[i]) > 1:
			L.pop(i)	
	return L 

print(removeRepeat2([1,2,4,4,2,9,76]))



print("abc" + "d")
list1 = ["a", "b", "a", "c", "d"]
print(list1.count("a"))



## Sets/Dictionaries ## 

s = set()
print(s)     # prints set(), the empty set

s = set(["cat", "cow", "dog"])
print(s)     # prints {'cow', 'dog', 'cat'}




