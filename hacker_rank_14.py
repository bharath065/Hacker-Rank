m = int(input())
a = set(map(int, input().split()))
n = int(input())
b = set(map(int, input().split()))
sym_diff = a.symmetric_difference(b)

for num in sorted(sym_diff):
    print(num)