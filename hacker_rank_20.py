# Students of District College have a subscription to English and French newspapers. 
# Some students have subscribed to only the English newspaper, 
# some have subscribed to only the French newspaper, 
# and some have subscribed to both newspapers.

# You are given two sets of student roll numbers. 
# One set has subscribed to the English newspaper, 
# and one set has subscribed to the French newspaper. 
# Your task is to find the total number of students who have subscribed to only English newspapers.

#Sample Input
# 9
# 1 2 3 4 5 6 7 8 9
# 9
# 10 1 2 3 11 21 55 6 8

# Sample Output
# 4

if __name__ == '__main__':
    n = int(input())
    english_subscribers = set(map(int, input().split()))
    
    m = int(input())
    french_subscribers = set(map(int, input().split()))
    
    only_english = english_subscribers.difference(french_subscribers)
    
    print(len(only_english))