class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        if not(event2[1] < event1[0] or event2[0] > event1[1]):
            return True
        else:
            return False
        