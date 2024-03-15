def solution(A):
    sum_left = A[0]
    sum_right = sum(A) - A[0]
    diff = abs(sum_left - sum_right)
    for i in range ( 1, len(A)):
        pivot = A[i]
        sum_left += pivot
        sum_right -= pivot
        curr_diff = abs(sum_left -  sum_right)
        if(diff > curr_diff):
            diff = curr_diff
    return diff, pivot

print(solution([3,1,2,4,3]))        

