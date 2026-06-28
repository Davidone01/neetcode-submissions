class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent_item = {}

        for n in nums:
            frequent_item[n] = frequent_item.get(n, 0) + 1
        out = []
        

        ordered = sorted(frequent_item.items(), key = lambda item: item[1], reverse =True)

        return [ item[0] for item in ordered[:k]]