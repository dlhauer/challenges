import collections
import heapq
def topKFrequent(words, k):
        count = collections.Counter(words)
        heap = [(-frequency, word) for word, frequency in count.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]
    
words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
topKFrequent(words, 2)
