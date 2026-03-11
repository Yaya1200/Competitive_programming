class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        count = 0
        for i in range(len(colors)):
            a = colors[i]
            if i+1 >= len(colors):
                middlenum = (i+1) % len(colors)
            else:
                middlenum = i+1
            b = colors[middlenum]
            if i+2 >= len(colors):
                lnum = (i+2) % len(colors)
            else:
                lnum = i+2
            c = colors[lnum]
            if a == c and a != b:
                count += 1
        return count

        