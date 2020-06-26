def nextLargerNodes(head: ListNode) -> List[int]:
      stack = []
      res = []
      i = 0
      while head:
        res.append(0)
        while stack and head.val > stack[-1][0]:
          node_i = stack.pop()
          res[node_i[1]] = head.val
        stack.append((head.val, i))
        i += 1
        head = head.next
          
      return res
      