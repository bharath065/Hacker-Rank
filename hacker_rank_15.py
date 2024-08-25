def calculate_happiness(n, m, array, A, B):
    set_A = set(A)
    set_B = set(B)
    
    happiness = 0
    
    for number in array:
        if number in set_A:
            happiness += 1
        elif number in set_B:
            happiness -= 1
    
    return happiness

if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    array = list(map(int, data[2:2+n]))
    
    A = list(map(int, data[2+n:2+n+m]))
    B = list(map(int, data[2+n+m:2+n+2*m]))
    
    happiness = calculate_happiness(n, m, array, A, B)
    print(happiness)