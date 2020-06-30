def firstBadVersion(n):
        """
        :type n: int
        :rtype: int
        """
        lo, hi = 1, n
        while lo <= hi:
          mid = (lo+hi)//2
          if isBadVersion(mid) and (mid == 1 or not isBadVersion(mid-1)):
            return mid
          elif not isBadVersion(mid):
            lo = mid+1
          else:
            hi = mid
        return n
        