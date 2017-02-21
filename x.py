A = [4,2,9,7,2,3]
B = [3,2,1,5,6,3]
def computing(a,b):
	for i in range(0,len(A)):
		a = 0
		b = 0
		if (A[i] > B[i]):
			a += 1
		else:
			b += 1
	if (a<b):
		return "Alice menang"
	elif (a>b):
		return "bob menang"
	else:
		return "seri"
print (computing(A,B))
	
	
	