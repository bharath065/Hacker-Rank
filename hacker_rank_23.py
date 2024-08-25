# Sample Input
# 5
# 1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 

# Sample Output
# 8

from collections import Counter

if __name__ == '__main__':
    k = int(input())
    room_numbers = list(map(int, input().split()))
    
    count = Counter(room_numbers)
    
    for room, cnt in count.items():
        if cnt % k != 0:
            print(room)
            break
