if __name__ == '__main__':
    n = int(input())
    s = set(map(int, input().split()))
    
    m = int(input())
    
    for _ in range(m):
        operation, _ = input().split()
        other_set = set(map(int, input().split()))
        
        if operation == 'update':
            s.update(other_set)
        elif operation == 'intersection_update':
            s.intersection_update(other_set)
        elif operation == 'difference_update':
            s.difference_update(other_set)
        elif operation == 'symmetric_difference_update':
            s.symmetric_difference_update(other_set)
    
    print(sum(s))

# Sample Input
# 16
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
# 4
# intersection_update 10
# 2 3 5 6 8 9 1 4 7 11
# update 2
# 55 66
# symmetric_difference_update 5
# 22 7 35 62 58
# difference_update 7
# 11 22 35 55 58 62 66

# Sample Output
# 38