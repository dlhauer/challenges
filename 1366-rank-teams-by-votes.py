import collections
def rankTeams(votes):
    ranks = [collections.defaultdict(int) for _ in range((len(votes[0])+1))]
    for vote in votes:
        for i, char in enumerate(vote):
            ranks[i+1][char] += 1
    teams = sorted(votes[0])
    for i in range(len(ranks)-1, 0, -1):
        teams.sort(reverse=True, key=lambda char: ranks[i].get(char, 0))
    return ''.join(teams)
