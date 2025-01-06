# Using Prefix Tree (or) Trie
def suggestedProducts(
      self, products: List[str], searchWord: str
  ) -> List[List[str]]:
      results = []
      products.sort()
      left, right = 0, len(products) - 1
      for i in range(len(searchWord)):
          searchChar = searchWord[i]
        
          while left <= right and (
              len(products[left]) <= i or searchChar != products[left][i]
          ):
              left += 1
            
          while left <= right and (
              len(products[right]) <= i or searchChar != products[right][i]
          ):
              right -= 1
  
          results.append([])
          remains = right - left + 1
          for idx in range(min(3, remains)):
              results[-1].append(products[left + idx])

      return results


# Using binary serach
def suggestedProducts(
      self, products: List[str], searchWord: str
  ) -> List[List[str]]:
      N = len(products)
      products.sort()
      left, results = 0, []
      prefix = ""
      for searchChar in searchWord:
          prefix += searchChar
          left = bisect.bisect_left(products, prefix, lo=left)
          suggestions = [
              products[i]
              for i in range(left, min(left + 3, N))
              if products[i].startswith(prefix)
          ]
          results.append(suggestions)
      return results
