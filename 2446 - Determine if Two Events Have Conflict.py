class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        return True if event1[0] <= event2[1] and event2[0] <= event1[1] else False
