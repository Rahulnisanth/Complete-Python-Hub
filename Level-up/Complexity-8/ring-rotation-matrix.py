MAX = 100

def fillSpiral(mat, m, n, temp): 
	i, k, l = 0, 0, 0
	tIdx = 0 # Index in temp array 
	while k < m and l < n: 
		# first row from the remaining rows 
		for i in range(l, n): 
			mat[k][i] = temp[tIdx] 
			tIdx += 1
		k += 1

		# last column from the remaining columns 
		for i in range(k, m): 
			mat[i][n-1] = temp[tIdx] 
			tIdx += 1
		n -= 1

		# last row from the remaining rows 
		if k < m: 
			for i in range(n-1, l-1, -1): 
				mat[m-1][i] = temp[tIdx] 
				tIdx += 1
			m -= 1

		# first column from the remaining columns 
		if l < n: 
			for i in range(m-1, k-1, -1): 
				mat[i][l] = temp[tIdx] 
				tIdx += 1
			l += 1

def spiralRotate(mat, M, N, k): 
	# Create a temporary array to store the result 
	temp = [0] * (M*N) 

	m, n, s, l = M, N, 0, 0
	start = 0 # Start position of current ring 
	tIdx = 0 # Index in temp 
	while s < m and l < n: 
		# Initialize end position of current ring 
		end = start 

		# copy the first row from the remaining rows 
		for i in range(l, n): 
			temp[tIdx] = mat[s][i] 
			tIdx += 1
			end += 1
		s += 1

		# copy the last column from the remaining columns 
		for i in range(s, m): 
			temp[tIdx] = mat[i][n-1] 
			tIdx += 1
			end += 1
		n -= 1
		# copy the last row from the remaining rows 
		if s < m: 
			for i in range(n-1, l-1, -1): 
				temp[tIdx] = mat[m-1][i] 
				tIdx += 1
				end += 1
			m -= 1
		# copy the first column from the remaining columns 
		if l < n: 
			for i in range(m-1, s-1, -1): 
				temp[tIdx] = mat[i][l] 
				tIdx += 1
				end += 1
			l += 1
		# if elements in current ring greater than k then rotate elements of current ring 
		if end-start > k: 
			# Rotate current ring using reversal algorithm for rotation 
			temp[start:start+k], temp[start+k:end] = reversed(temp[start:start+k]), reversed(temp[start+k:end]) 
			temp[start:end] = reversed(temp[start:end]) 

			# Reset start for next ring 
			start = end 

	fillSpiral(mat, M, N, temp) 

# Driver program 

M, N, k = list(map(int, input().split()))
matrix = [list(map(int, input().split())) for _ in range(M)]
spiralRotate(matrix, M, N, k) 
# Printing :
for i in range(M): 
    for j in range(N): 
        print(matrix[i][j], end=" ") 
    print() 
    
