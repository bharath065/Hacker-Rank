# Sample Input
# 3
# 5
# 1 2 3 5 6
# 9
# 9 8 5 6 3 2 1 4 7
# 1
# 2
# 5
# 3 6 5 4 1
# 7
# 1 2 3 5 6 8 9
# 3
# 9 8 2

# Sample Output
# True 
# False
# False

if __name__ == '__main__':
    t = int(input())  # Number of test cases
    results = []

    for _ in range(t):
        # Read set A
        n_A = int(input())
        set_A = set(map(int, input().split()))
        
        # Read set B
        n_B = int(input())
        set_B = set(map(int, input().split()))
        
        # Check if set_A is a subset of set_B
        results.append(set_A.issubset(set_B))
    
    for result in results:
        print(result)