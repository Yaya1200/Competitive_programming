class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        total_area = ((ay2-ay1)*(ax2-ax1))+ ((by2-by1)*(bx2-bx1))
        inner_y2 =  min(by2, ay2)
        inner_y1 = max(ay1, by1)
        inner_x2 = min(bx2, ax2)
        inner_x1 =  max(bx1, ax1)
        total_inner = 0
        if inner_y2 > inner_y1 and inner_x2 > inner_x1:
            total_inner = (inner_y2-inner_y1)*(inner_x2-inner_x1)

        return total_area-total_inner


        