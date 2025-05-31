# HAMMING DISTANCE BETWEEJ TWO INTEGERS :
def hammingDistance(self, x: int, y: int) -> int:
      return bin(x ^ y).count('1')
