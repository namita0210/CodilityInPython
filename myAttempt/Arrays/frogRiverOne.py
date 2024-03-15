def solution( A , x):
    river_positions = [False] * (x+1)
    for i in range (len(A)):
        pos = A[i]
        if river_positions[pos] == False :
            river_positions[pos] = True
            x-=1
            if x == 0 : return i
    return -1

print(solution([1,2,1], 3))
print(solution([1,1,1],1))
# x = width of the river
# A = position of leaves 