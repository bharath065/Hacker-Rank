import numpy as np

def compute_products():
    # Read input arrays
    A = np.array(list(map(int, input().strip().split())))
    B = np.array(list(map(int, input().strip().split())))
    
    # Compute inner product
    inner_product = np.inner(A, B)
    
    # Compute outer product
    outer_product = np.outer(A, B)
    
    # Print the results
    print(inner_product)
    print(outer_product)

# Call the function to execute
compute_products()


# Sample Input
# # 0 1
# 2 3

# Sample Output
# 3
# [[0 0]
#  [2 3]]