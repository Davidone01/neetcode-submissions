"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key= lambda x:x.start)
        print(intervals)
        res = 1
        i = 0
        m = intervals[0].end
        heap = []
        heapq.heappush(heap,intervals[0].end)
        while i < len(intervals):
            if i < len(intervals) - 1 and intervals[i+1].start < heap[0]:
                #devo aggiungere una stanza
                res += 1
                #aggiungo il nuovo orario di fine nella heap
                heapq.heappush(heap, intervals[i+1].end)
            else:
                #se non aggiungo una nuova stanza aggiorno il tempo di fine della nuova stanza
                heapq.heappop(heap)
                if i < len(intervals)-1:
                    heapq.heappush(heap, intervals[i+1].end)
            i +=1


        return res
