class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if not piles: 
            return 0
        
        def sum_hours_f(k):
            sum_hours = 0
            for n in piles:
                sum_hours += math.ceil(n/k)
            return sum_hours
        l, r = 0, max(piles)
        while (r-l)>1:
            mid = (l+r)//2
            if sum_hours_f(mid) > h:   
                l = mid
            else: 
                r = mid
        return r

        