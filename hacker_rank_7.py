#Given the participants' score sheet for your University Sports Day, 
#you are required to find the runner-up score.
# You are given n scores.
# Store them in a list and find the score of the runner-up.

#Sample Input 0:
# 5
# 2 3 6 6 5

#Sample Output 0:
# 5

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    scores = set(arr)
sorted_scores = list(scores)
sorted_scores.sort(reverse=True)
if len(sorted_scores) > 1:
    runner_up_score = sorted_scores[1]
    print(runner_up_score)
else:
    print("Not enough distinct scores to determine a runner-up.")