def merge (A, p, q, r):
	n1 = q - p + 1
	n2 = r - q
	
	L = []
	R = []
	for i in range (1, n1+1):
		L.append(A[p+i-1])
	for j in range (1, n2+1):
		R.append(A[q+j])

	i = 0
	j = 0
	for k in range (p, r+1):
		if i>n1-1 and j<=n2-1:
			A[k] = R[j]
			j = j + 1			
		elif i<=n1-1 and j>n2-1:
			A[k] = L[i]
			i = i + 1			
		elif L[i] <= R[j]:
			A[k] = L[i]
			i = i + 1
		else:
			A[k] = R[j]
			j = j + 1

def merge_sort(A, p, r):
	if p<r:
		q = (p + r) // 2
		merge_sort(A, p, q)
		merge_sort(A, q+1, r)
		merge(A, p, q, r)