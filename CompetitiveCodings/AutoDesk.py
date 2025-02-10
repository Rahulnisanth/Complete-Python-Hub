# AUTO DESK INTERVIEW QUESTIONS :

# [1] Find and return the peak elements in the list
def solution(target):
    N, result = len(target), []
    for i in range(N):
        if i > 0 and i < (N - 1) and target[i] > max(target[i - 1], target[i + 1]):
            result.append(target[i])
        elif i == 0 or i == N - 1:
            result.append(target[i])
    return result

# Testcase
print(solution([4, 3, 2, 4]))

# [2] Sort the given words based on the difference of vowel count & consonant count
from heapq import heappush, heappop

def sortByDiff(text):
    minHeap, vowels = [], "aeiou"
    for word in text.split():
        VCount = sum([1 for ch in word if ch in vowels])
        CCount = len(word) - VCount
        diff = abs(VCount - CCount)
        heappush(minHeap, (diff, word))
    
    result = []
    while minHeap:
        diff, word = heappop(minHeap)
        result.append(word)
    return result

# Testcase
print(sortByDiff("ae aabc penelope rahul"))

# [3] Inventory shop 
from collections import defaultdict, deque

def manageInventoryShop(logs):
    mainMap = defaultdict(deque)
    returnMap = defaultdict(deque)
    result = []
    for log in logs:
        term = log[0]
        # supply
        if term == 'supply':
            item, count, price = log[1:]
            count, price = int(count), int(price)
            # All supplies except returned should go into the mainMap
            if item in mainMap and mainMap[item][-1][1] == price:
                mainMap[item][-1][0] += count
            else:
                mainMap[item].append([count, price])
            print(f"mainMap: {mainMap}")
        
        # sell
        elif term == 'sell':
            item, count = log[1:]
            count = int(count)
            profit = 0
            # First check the item in returnMap
            while count > 0 and returnMap[item]:
                available, price = returnMap[item][0]
                if available <= count:
                    count -= available
                    profit += (available * price)
                    returnMap[item].popleft()
                else:
                    returnMap[item][0][0] -= count
                    profit += (count * price)
                    count = 0
                    
            # Then go for the main maps
            while count > 0 and mainMap[item]:
                available, price = mainMap[item][0]
                if available <= count:
                    count -= available
                    profit += (available * price)
                    mainMap[item].popleft()
                else:
                    mainMap[item][0][0] -= count
                    profit += (count * price)
                    count = 0
                
            if profit > 0: result.append(profit)
                
        # return 
        elif term == 'return':
            item, count, old_price, new_price = log[1:]
            count, old_price, new_price = int(count), int(old_price), int(new_price)
            # Add the returned items to returnMap
            if mainMap[item] and (mainMap[item][0][1] == old_price):
                if returnMap[item] and (returnMap[item][-1][1] == new_price):
                    returnMap[item][-1][0] += count
                else:
                    returnMap[item].append([count, new_price])
        
    return result
    
# Testcase
logs = [
        ["supply", "item1", "2", "100"],
        ["supply", "item2", "2", "120"],
        ["sell", "item1", "1"],
        ["sell", "item2", "2"],
        ["return", "item1", "1", "100", "80"],
        ["sell", "item1", "1"],
        ["sell", "item1", "1"],
        ["sell", "item1", "1"],
    ]
print(manageInventoryShop(logs))
      
