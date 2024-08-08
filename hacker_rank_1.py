#The included code stub will read an integer,'n' from STDIN. 
#Without using any string methods, try to print the following:
#123..n

#Sample Input:
# 5
#Sample Output:
# 12345

if __name__ == '__main__':
    n = int(input())
    for i in range(1, n + 1):
        print(i, end="")