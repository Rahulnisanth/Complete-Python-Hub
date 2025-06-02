# HAMMING DISTANCE BETWEEJ TWO INTEGERS :
def hammingDistance(self, x: int, y: int) -> int:
      return bin(x ^ y).count('1')


# PERFECT NUMBER :
def checkPerfectNumber(self, num: int) -> bool:
  if num <= 0:
      return False
  total_sum = 0
  for i in range(1, int(num**0.5) + 1):
      if num % i == 0:
          total_sum += i
          if i * i != num:
              total_sum += num // i
  return total_sum - num == num
