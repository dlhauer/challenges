def maxScore(cardPoints, k):
    max_points = 0
    n = len(cardPoints)-k
    for i in range(k+1):
        if i == 0:
            cur_sum = sum(cardPoints[0:i] + cardPoints[i+n:])
        else:
            cur_sum += cardPoints[i-1]
            cur_sum -= cardPoints[i+n-1]
        max_points = max(cur_sum, max_points)
    return max_points

arr = [1,79,80,1,1,1,200,1]

print(maxScore(arr, 4))