class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        indici = range(len(names))

        ordered_indici = sorted(indici, key= lambda i: heights[i], reverse= True)

        return [names[i] for i in ordered_indici]