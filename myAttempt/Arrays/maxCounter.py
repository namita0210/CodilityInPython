# n -> num of counters
# A-> Array of instructions
def solution(n , A):

    counters = [0] * n
    start_line = 0
    current_max = 0

    for i in A:

        x = i-1

        if i > n:
            start_line = current_max

        elif counters[x] < start_line:    
            counters[x] = start_line + 1

        else:
            counters[x] += 1

        if i <= n and counters[x] > current_max:
            current_max = counters[x]

    for i in range (0, len(counters)):

        if counters[i] < start_line:
            counters[i] = start_line
            
    return counters                        

