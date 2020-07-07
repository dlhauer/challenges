import math

def kClosest(points, K):
    points = sorted(points, key=lambda x: math.sqrt(sum([i**2 for i in x])))
    return points[:K]

points = [[-2,2],[1,3]]
print(kClosest(points, 1))
