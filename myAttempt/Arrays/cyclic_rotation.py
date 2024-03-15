# (i + k )% n
def solution(A , k):
    n = len(A)
    B = [None] * n
    idx = 0
    for i in range ( 0 , n):
        B[(i+k)%n] = A[i]
    return print(B)    
   

solution([7,2,8,3,5],2)    