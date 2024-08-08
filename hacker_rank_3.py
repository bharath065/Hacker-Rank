#Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:
#Mat size must be N*M. ( is an odd natural number, and M  is 3 times N.)
#The design should have 'WELCOME' written in the center.
#The design pattern should only use |, . and - characters.

#Sample Input:
# 9 27
#Sample Output:

# ------------.|.------------
# ---------.|..|..|.---------
# ------.|..|..|..|..|.------
# ---.|..|..|..|..|..|..|.---
# ----------WELCOME----------
# ---.|..|..|..|..|..|..|.---
# ------.|..|..|..|..|.------
# ---------.|..|..|.---------
# ------------.|.------------

def print_door_mat(n, m):
    for i in range(1, n, 2):
        pattern = ".|." * i
        print(pattern.center(m, "-"))
    print("WELCOME".center(m, "-"))
    for i in range(n-2, -1, -2):
        pattern = ".|." * i
        print(pattern.center(m, "-"))

if __name__ == '__main__':
    n, m = map(int, input().split())
    print_door_mat(n, m)