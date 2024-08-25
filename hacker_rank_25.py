# Sample Input 0
# 1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
# 2
# 1 2 3 4 5
# 100 11 12

# Sample Output 0
# False

if __name__ == '__main__':
    # Read the main set
    set_A = set(map(int, input().split()))
    
    # Read the number of other sets
    n = int(input())
    
    # Initialize a flag to check if set_A is a strict superset
    is_strict_superset = True
    
    # Process each of the other sets
    for _ in range(n):
        other_set = set(map(int, input().split()))
        # Check if set_A is a superset of the other set
        if not (set_A > other_set):
            is_strict_superset = False
            break
    
    # Output the result
    print(is_strict_superset)