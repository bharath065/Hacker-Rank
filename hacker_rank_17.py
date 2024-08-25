# .remove(x)
# This operation removes element  from the set.
# If element  does not exist, it raises a KeyError.
# The .remove(x) operation returns None.

# Example

# s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
# s.remove(5)
# print s
# set([1, 2, 3, 4, 6, 7, 8, 9])
# print s.remove(4)
# None
# print s
# set([1, 2, 3, 6, 7, 8, 9])
# s.remove(0)
# KeyError: 0
# .discard(x)
# This operation also removes element  from the set.
# If element  does not exist, it does not raise a KeyError.
# The .discard(x) operation returns None.

# Example

# s = set([1, 2, 3, 4, 5, 6, 7, 8, 9]
# s.discard(5)
# print s
# set([1, 2, 3, 4, 6, 7, 8, 9])
# print s.discard(4)
# None
# print s
# set([1, 2, 3, 6, 7, 8, 9])
# s.discard(0)
# print s
# set([1, 2, 3, 6, 7, 8, 9])
# .pop()
# This operation removes and return an arbitrary element from the set.
# If there are no elements to remove, it raises a KeyError.

# Example

# s = set([1])
# print s.pop()
# 1
# print s
# set([])
# print s.pop()
# KeyError: pop from an empty set

# Sample Input
# 9
# 1 2 3 4 5 6 7 8 9
# 10
# pop
# remove 9
# discard 9
# discard 8
# remove 7
# pop 
# discard 6
# remove 5
# pop 
# discard 5

# Sample Output
# 4

if __name__ == '__main__':
    n = int(input())
    s = set(map(int, input().split()))
    num_commands = int(input())
    
    for _ in range(num_commands):
        command = input().split()
        if command[0] == 'pop':
            if s:
                s.pop()
        elif command[0] == 'remove':
            if int(command[1]) in s:
                s.remove(int(command[1]))
        elif command[0] == 'discard':
            s.discard(int(command[1]))
    
    print(sum(s))