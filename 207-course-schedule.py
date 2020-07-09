import collections

def canFinish(numCourses, prerequisites):
        forward = {i: set() for i in range(numCourses)}
        backward = collections.defaultdict(set)
        for i, j in prerequisites:
            forward[i].add(j)
            backward[j].add(i)
        stack = [node for node in range(numCourses) if not backward[node]]
        while stack:
            node = stack.pop()
            for neighbor in forward[node]:
                backward[neighbor].remove(node)
                if not backward[neighbor]:
                    stack.append(neighbor)
            backward.pop(node)
        return not backward
