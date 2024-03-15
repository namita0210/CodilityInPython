from numpy import *

def solution(arr):
    n = len(arr)+1
    actual_sum = 0
    for i in arr:
        actual_sum += i
    expected_sum =  ((n * (n+1))//2)
    return expected_sum - actual_sum

print(solution([2,3,1,5]))
print(solution(array([1,2,3,4,5,6,7,8,9])))
print(solution([]))
