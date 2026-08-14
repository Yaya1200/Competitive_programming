class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        j = 0
        output = ""
        while i < len(name) or  j < len(typed):
            if i < len(name) and j< len(typed) and name[i] == typed[j]:
                i+=1
                j+= 1
            elif j-1 >= 0 and j < len(typed) and  typed[j] == typed[j-1]:
                j+= 1
            else:
                break
        if i == len(name) and j == len(typed):
            return True
        else:
            return False
        