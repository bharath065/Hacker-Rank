# Consider a list (list = []). You can perform the following commands:

# 1.insert i e: Insert integer  at position i.
# 2.print: Print the list.
# 3.remove e: Delete the first occurrence of integer e.
# 4.append e: Insert integer  at the end of the list.
# 5.sort: Sort the list.
# 6.pop: Pop the last element from the list.
# 7.reverse: Reverse the list.

# Initialize your list and read in the value of n followed by n lines of commands 
# where each command will be of the 7 types listed above. 
# Iterate through each command in order and perform the corresponding operation on your list.

# Sample Input 0:
# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print

# Sample Output 0:
# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]

if __name__ == '__main__':
    N = int(input())
    lst = []

    for _ in range(N):
        command = input().split()
        cmd = command[0]

        if cmd == "insert":
            lst.insert(int(command[1]), int(command[2]))
        elif cmd == "print":
            print(lst)
        elif cmd == "remove":
            lst.remove(int(command[1]))
        elif cmd == "append":
            lst.append(int(command[1]))
        elif cmd == "sort":
            lst.sort()
        elif cmd == "pop":
            lst.pop()
        elif cmd == "reverse":
            lst.reverse()