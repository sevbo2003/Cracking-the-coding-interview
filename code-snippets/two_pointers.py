"""
# Find if There is a Pair in A[0..N-1] with Given Sum
# Using Two-pointers Technique

A[] = {10, 20, 35, 50, 75, 80}
X = =70
i = 0
j - 5

A[i] + A[j] = 10 + 80 = 90
Since A[i] + A[j] > X, j--
i = 0
j = 4

A[i] + A[j] = 10 + 75 = 85
Since A[i] + A[j] > X, j--
i = 0
j = 3

A[i] + A[j] = 10 + 50 = 60
Since A[i] + A[j] < X, i++
i = 1
j = 3
m
A[i] + A[j] = 20 + 50 = 70
Thus this signifies that Pair is Found.
"""

def isPairSum(A, N, X):
	# represents first pointer
	i = 0

	# represents second pointer
	j = N - 1

	while(i < j):
	
		# If we find a pair
		if (A[i] + A[j] == X):
			return True

		# If sum of elements at current
		# pointers is less, we move towards
		# higher values by doing i += 1
		elif(A[i] + A[j] < X):
			i += 1

		# If sum of elements at current
		# pointers is more, we move towards
		# lower values by doing j -= 1
		else:
			j -= 1
	return 0

# array declaration
arr = [3, 5, 9, 2, 8, 10, 11]

# value to search
val = 17

print(isPairSum(arr, len(arr), val))
