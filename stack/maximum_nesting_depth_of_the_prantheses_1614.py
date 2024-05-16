class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        opened = "("
        closed = ")"
        maxp = 0
        count = 0
        for c in s:
            if c == opened:
                stack.append(c)
                count += 1
                maxp = max(maxp, count)
            elif c == closed:
                stack.pop()
                count -= 1
            else:
                continue
        return maxp
