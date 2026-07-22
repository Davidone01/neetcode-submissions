class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def is_before(w):
            days_count = 1
            _sum = 0

            for n in weights:
                if _sum + n <=  w:
                    _sum +=n
                else:
                    _sum = n
                    days_count += 1
            return days_count > days

        if not weights:
            return 0
        l = max(weights)-1
        r = sum(weights)

        while (r-l)>1:
            mid = (l+r)//2
            if is_before(mid):
                l = mid
            else: 
                r = mid
        return r