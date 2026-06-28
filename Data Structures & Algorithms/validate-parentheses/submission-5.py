class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return False
        queue = deque()
        for c in s:
            if c == "(" or c == "{" or c == "[":
                queue.append(c)
            else:
                if not queue:
                    return False
                tmp = queue.pop()
                if tmp == "(" and c == ")":
                    continue
                if tmp == "[" and c == "]":
                    continue
                if tmp == "{" and c == "}":
                    continue
                return False
        return len(queue)==0

        