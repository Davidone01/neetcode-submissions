class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])
        l = 0
        r = len(values)-1
        if not values:
            return res
        while (r-l)>1:
            mid = (l+r)//2
            if values[mid][1]<timestamp:
                l = mid
            else:
                r = mid
        return values[r][0] if values[r][1] <= timestamp  else values[l][0] if values[l][1] <= timestamp else res

