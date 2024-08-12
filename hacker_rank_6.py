#Let's learn about list comprehensions! 
#You are given three integers x,y and z representing the dimensions of a cuboid along with an integer n. 
#Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k is not equal to n.
#Here,(0<=i<=x;0<=j<=y;0<=k<=z). Please use list comprehensions.

#Sample Input 0:
#1
#1
#1
#2

#Sample Output 0:
#[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

import itertools
def generate_combinations(x, y, z, n):
    combinations = list(itertools.product(range(x+1), range(y+1), range(z+1)))
    valid_combinations = [list(comb) for comb in combinations if sum(comb) != n]
    return valid_combinations
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    result = generate_combinations(x, y, z, n)
    print(result)