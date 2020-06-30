import bisect
import collections

class TopVotedCandidate:

    def __init__(self, persons, times):
        self.persons = persons
        self.times = times

    def q(self, t):
        slice_idx = bisect.bisect_right(self.times, t)
        persons = self.persons[:slice_idx]
        tally = sorted(collections.Counter(persons).items(), key=lambda x: x[1], reverse=True)
        return self.break_tie(persons, tally)

    def break_tie(self, cands, tally):
        if len(tally) == 1 or tally[0][1] != tally[1][1]:
            return tally[0][0]
        tied_cands = [cand[0] for cand in tally if cand[1] == tally[0][1]]
        for cand in reversed(cands):
            if cand in tied_cands:
                return cand

persons = [0,1,2,1,2,1,1,2,2]
times   = [0,5,10,15,20,25,30,35,40]
candidate = TopVotedCandidate(persons, times)
print(candidate.q(40))
