def kidsWithCandies(candies, extraCandies):
    max_candies = max(candies)
    for i, candy in enumerate(candies):
        if candy+extraCandies >= max_candies:
            candies[i] = True
        else:
            candies[i] = False
    return candies

candies = [4,2,1,1,2]
extraCandies = 1
print(kidsWithCandies(candies, extraCandies))