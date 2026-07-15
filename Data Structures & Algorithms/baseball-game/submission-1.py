class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for o in operations:
            try:
                stack.append(int(o))
            except:
                if o == "+":
                    a = stack[-1]
                    b = stack[-2]
                    stack.append(a+b)
                elif o == "D":
                    stack.append( stack[-1] * 2)
                elif o == "C":
                    stack.pop()
        sum = 0
        for e in stack:
            sum += e 
        return sum

