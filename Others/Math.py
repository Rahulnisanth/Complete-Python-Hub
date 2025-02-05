# COMPUTE THE AREA OF TWO RECTANGLES REMOVING THE OVERLAPPING AREA IN A 2D PLANE :
def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
      area1 = (ax2 - ax1) * (ay2 - ay1)
      area2 = (bx2 - bx1) * (by2 - by1)
      left, right = max(ax1, bx1), min(ax2, bx2)
      top, bottom = min(ay2, by2), max(ay1, by1)
      overlap = 0
      if (right > left and top > bottom):
          overlap = (right - left) * (top - bottom)
      return area1 + area2 - overlap
