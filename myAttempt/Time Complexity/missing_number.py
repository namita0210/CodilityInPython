def smallest_missing_positive_integer(A):
    # Create a set to store positive integers in A
    positive_set = set()
    
    # Iterate through A and add positive integers to the set
    for num in A:
        if num > 0:
            positive_set.add(num)
    
    # Check for the smallest positive integer not in the set
    smallest_integer = 1
    while smallest_integer in positive_set:
        smallest_integer += 1
    
    return smallest_integer

# Test cases
print(smallest_missing_positive_integer([1, 3, 6, 4, 1, 2]))  # Output: 5
print(smallest_missing_positive_integer([-1, -3]))          # Output: 1
