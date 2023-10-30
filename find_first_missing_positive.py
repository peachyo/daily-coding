def find_first_missing_positive(A):
    for i in range(len(A)):
        while 1 <= A[i] <= len(A) and A[i] != A[A[i]-1]:
            A[A[i]-1], A[i] = A[i], A[A[i]-1]
    return next((i+1 for i, a in enumerate(A) if a != i + 1), len(A) + 1)
