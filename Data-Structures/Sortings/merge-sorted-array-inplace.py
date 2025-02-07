# MERGE THE SORTED ARRAYS IN-PLACE WITHOUT USING AUXILARY SPACE
def mergeSorted(a, b):
  m, n = len(a), len(b)
  for i in range(n - 1, -1, -1):
      if a[-1] > b[i]:
          L_Ele = a[-1]
          j = m - 2
          while j >= 0 and a[j] > b[i]:
              a[j + 1] = a[j]
              j -= 1
          a[j + 1] = b[i]
          b[i] = L_Ele
