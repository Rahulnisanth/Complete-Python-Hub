

# TIME REQUIRED TO BUY TICKETS :
def timeRequiredToBuy(tickets, k: int) -> int:
    timeReq = 0
    for i in range(len(tickets)):
        if i <= k:
            timeReq += min(tickets[i], tickets[k])
        else:
            timeReq += min(tickets[i], tickets[k] - 1)
    return timeReq


# COMPARE VERSION NUMBERS :
def compareVersion(version1: str, version2: str) -> int:
    # Helper function to find the load on the string :
    def helper(input, idx):
        num = 0
        while idx < len(input):
            if input[idx] == '.':
                break
            else:
                num = num * 10 + int(input[idx])
            idx += 1
        return [num, idx + 1]
    # Main method defs :
    i = j = 0
    while i < len(version1) or j < len(version2):
        v1, i = helper(version1, i)
        v2, j = helper(version2, j)
        if v1 > v2:
            return 1
        elif v1 < v2:
            return -1
    return 0


# AREA OF THE LARGEST RECTANGLE IN GIVEN HISTOGRAM GRAPH :
def largestRectangle(heights):
    area = [0] * len(heights)
    for i in range(len(heights) - 1):
        area[i] = min(heights[i], heights[i + 1]) * 2
    return max(area)


# SPECIAL ARRAY WITH X ELEMENTS >= X :
def specialArray(nums) -> int:
    nums.sort(reverse=True)
    for x in range(1, len(nums) + 1):
        count = 0
        for num in nums:
            if num >= x:
                count += 1
        if count == x:
            return x
    return -1


# GET EQUAL SUBSTRINGS WITHIN GIVEN BUDGET :
def equalSubstring(s,t,maxCost) -> int:
    def helper(s1, s2):
        return abs(ord(s1) - ord(s2))
    array = []
    for i in range(len(s)):
        array[i] = helper(s[i], t[i])
    
    start, end, answer = 0, 0, 0
    while start < len(s) and end < len(t):
        cost += array[end]
        if cost <= maxCost :
            answer = max(answer, end - start)
        else:
            while cost > maxCost: 
                cost -= array[start]
        start += 1
        end += 1
    return answer


# NUMBER OF STEPS TO REDUCE THE BINARY NUMBER TO 1 :
def numSteps(s) -> int:
    def helper(num, steps):
        if num == 1:
            return steps
        if num % 2 != 0:
            return helper(num + 1, steps + 1)
        if num % 2 == 0:
            return helper(num // 2, steps + 1)
    return helper(int(s, 2), 0)


# MAKE A GOOD STRING :
def makeGood(s: str) -> str:
    if len(s) > 1:
        stack = []
        for ch in s:
            if stack and abs(ord(stack[-1]) - ord(ch)) == 32:
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)
    return s


# MINIMUM REMOVE TO MAKE VALID PARENTHESIS :
def minRemoveToMakeValid(s: str) -> str:
    result = []
    stack, invalidIdx = [], set()
    for i, ch in enumerate(s):
        if ch == '(':
            stack.append(i)
        elif ch == ')':
            if stack:
                stack.pop()
            else:
                invalidIdx.add(i)

    invalidIdx.update(stack)

    for i, ch in enumerate(s):
        if i not in invalidIdx:
            result.append(ch)
    
    return ''.join(result)


# IS VALID STRING :
def checkValidString(s: str) -> bool:
    startP, endP = 0, 0
    for ch in s:
        if ch == '(':
            startP += 1 
            endP += 1
        if ch == ')':
            startP -= 1
            endP -= 1
        if ch == '*':
            startP += 1
            endP -= 1
        if startP < 0:
            return False
        if endP < 0:
            endP = 0
    return endP == 0


# NUMBER OF STUDENTS UNABLE TO EAT LUNCH ;
def countStudents(students, sandwiches) -> int:
    counts = [0, 0]
    for student in students:
        counts[student] += 1
    remain = len(sandwiches)
    for sandwich in sandwiches:
        if counts[sandwich] == 0:
            break
        if remain == 0:
            break
        counts[sandwich] -= 1
        remain -= 1
    return remain


# REMOVE K DIGITS TO MAKE THE NUMBER SMALLEST :
def removeKdigits(num: str, k: int) -> str:
    stack = []
    for digit in num:
        while k > 0 and stack and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)

    while k > 0:
        stack.pop()
        k -= 1
    
    result = ''.join(stack).lstrip('0')

    return result if result else '0'


# COUNT THE NUMBER OF ATOMS :
def countOfAtoms(self, formula: str) -> str:
    n: int = len(formula)
    result_counter: dict[str, int] = {}
    parenthesis_stack: list[dict[str, int]] = []
    cur_ind = 0

    while cur_ind < n:
        cur_char: str = formula[cur_ind]

        if cur_char == "(":
            cur_ind += 1
            parenthesis_stack.append({})
            continue

        if cur_char == ")":
            mult: str = ""
            cur_ind += 1

            while cur_ind < n and formula[cur_ind].isdigit():
                mult += formula[cur_ind]
                cur_ind += 1

            last_counter: dict[str, int] = parenthesis_stack.pop()
            target: dict[str, int] = parenthesis_stack[-1] if parenthesis_stack else result_counter
            for elem, counter in last_counter.items():
                if elem not in target:
                    target[elem] = 0
                target[elem] += counter * (int(mult) if mult else 1)
            continue

        cur_elem: str = ""
        cur_counter: str = ""
        target: dict[str, int] = parenthesis_stack[-1] if parenthesis_stack else result_counter

        while cur_ind < n and cur_char not in "()":
            if cur_char.isalpha():
                if cur_char.isupper() and cur_elem != "":
                    if not cur_elem in target:
                        target[cur_elem] = 0
                    target[cur_elem] += int(cur_counter) if cur_counter else 1
                    cur_counter = ""
                    cur_elem = ""
                cur_elem += cur_char
            else:
                cur_counter += cur_char
            cur_ind += 1
            if cur_ind != n:
                cur_char = formula[cur_ind]

        target = parenthesis_stack[-1] if parenthesis_stack else result_counter
        if not cur_elem in target:
            target[cur_elem] = 0
        target[cur_elem] += int(cur_counter) if cur_counter else 1

    parts: list[str] = [
        elem + str(counter) if not counter == 1 else elem for elem, counter in result_counter.items()
    ]
    parts.sort()

    return "".join(parts)

# UNREVEALING THE DECK OF CARDS :
from collections import deque
def deckRevealedIncreasing(deck):
    deck.sort()
    n = len(deck)
    result = [0] * n
    indices = deque(range(n))

    for card in deck:
        idx = indices.popleft()
        result[idx] = card
        if indices:
            indices.append(indices.popleft())

    return result


# KTH SMALLEST PRIME FRACTION :
import heapq
def kthsmallestprimefraction(arr, k):
    n = len(arr)
    heap = [(arr[i] / arr[j],arr[i],arr[j]) for i in range(n) for j in range(i + 1, n)]
    heapq.heapify(heap)

    result = None
    for _ in range(k):
        result = heapq.heappop(heap)
    return [int(result[1]), int(result[2])]


# REVERSE THE LINKED LIST WITHIN GIVEN BOUNDARY :
def reverseBetween(self, head, left: int, right: int):
    dummy = ListNode(0, head)

    leftPrev, curr = dummy, head
    for i in range(left - 1):
        leftPrev, curr = curr, curr.next
    
    prev = None
    for i in range(right - left + 1):
        tempNext = curr.next
        curr.next = prev
        prev, curr = curr, tempNext
    
    leftPrev.next.next = curr
    leftPrev.next = prev

    return dummy.next


# DOUBLE THE NUMBER REPRESENTED AS LINKED-LIST :
def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
    stack = []
    value = 0

    while head:
        stack.append(head.val)
        head = head.next
    
    tail = None
    while stack or value != 0 :
        tail = ListNode(0, tail)
        if stack:
            value += stack.pop() * 2
        tail.val = value % 10
        value //= 10
        
    return tail


# WONDERFUL-SUBSTRING :
def wonderfulSubstrings(word: str) -> int:
    count = [0] * 1024
    result, xor, count[xor] = 0, 0, 1
    for char in word:
        idx = ord(char) - ord('a')
        xor ^= 1 << idx
        result += count[xor]
        for i in range(10):
            result += count[xor ^ (1 << i)]
        count[xor] += 1
    return result


# SINGLE NUMBER III :
def singleNumber(nums):
    xor = 0
    for num in nums:
        xor ^= num
    xor & -xor
    result = [0, 0]
    for num in nums:
        if num & xor == 0:
            result[0] ^= num
        else:
            result[1] ^= num
    return result


# FIND THE COMMON CHARACTERS :
from typing import Counter
def commonChars(words):
    min_freq = Counter(words[0])
    for word in words:
        min_freq &= Counter(word)
    return list(min_freq.elements())


# THE NUMBER OF BEAUTIFUL SUBSETS :
from collections import defaultdict
def beautifulSubsets(nums, k):
    count = 0
    def explore(index):
        nonlocal count
        if len(nums) == index:
            count += 1
            return
        num = nums[index]
        if not num - k in map and not num + k in map :
            map[num] += k
            explore(index + 1)
            map[num] -= k
            if map[num] == 0:
                del map[num]
        explore(index + 1)
    map = defaultdict(int)
    explore(0)
    return count - 1


# WORD BREAK - II :
def wordBreak(self, s: str, wordDict ) :
    def backtrack(s, start, current):
        if len(s) == start:
            result.append(" ".join(current))
        for i in range(start, len(s)):
            if s[start:i+1] in setter:
                current.append(s[start:i+1])
                backtrack(s, i + 1, current)
                current.pop(-1)
    result = []
    setter = set(wordDict)
    backtrack(s, 0, [])
    return result


# STUDENT ABSENTS RECORD - II :
def checkRecord(n: int) -> int:
    MOD = (10 ** 9) + 7
    bool_cache = [[[False] * 3 for _ in range(2)] for _ in range(n)]
    value_cache = [[[None] * 3 for _ in range(2)] for _ in range(n)]
    # Utility function for recursive call :
    # Day => No.of days [N]
    # Absent => No.of consecutive absents [0, 1]
    # Late => No.of consecutive lates [0, 1, 2]
    def count(day, absent, late):
        if day == n:
            return 1
        if bool_cache[day][absent][late]:
            return value_cache[day][absent][late]
        total = 0
        # Present ->
        total += count(day + 1, absent, 0)
        # Add absent if consecutive absent < [0,1] ->
        if absent < 1:
            total += count(day + 1, absent + 1, 0)
        # Add late if consecutive late < [0,1,2] ->
        if late < 2:
            total += count(day + 1, absent, late + 1)
        # Adding bool_cache & value_cache ->
        bool_cache[day][absent][late] = True
        value_cache[day][absent][late] = total % MOD
        return value_cache[day][absent][late]
    return count(0, 0, 0)


# MAXIMAL RECTANGLE :
def maximalRectangle(matrix) -> int:
    if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
        return 0
    else:
        row, col = len(matrix), len(matrix[0])
        heights = [0] * col
        maxArea = 0
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            maxArea = max(maxArea, largestArea(heights))
        return maxArea

def largestArea(heights):
    stack, n = [], len(heights)
    maxArea = 0
    for i in range(n + 1):
        h = 0 if i == n else heights[i]
        while stack and h < heights[stack[-1]]:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            maxArea = max(maxArea, height * width)
        stack.append(i)
    return maxArea


# FIND THE SAFEST PATH IN GRID :
from collections import deque
import heapq
def maximumSafenessFactor(grid) -> int:
        n = len(grid)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visits = [[float('inf')] * n for _ in range(n)]
        queue = deque()

        for row in range(n):
            for col in range(n):
                if grid[row][col] == 1:
                    queue.append((row, col))
                    visits[row][col] = 0

        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < n and 0 <= nc < n and visits[nr][nc] == float('inf'):
                    visits[nr][nc] = visits[row][col] + 1
                    queue.append((nr, nc))

        max_heap = [(-visits[0][0], 0, 0)]
        max_safeness = [[-1] * n for _ in range(n)]
        max_safeness[0][0] = visits[0][0]

        while max_heap:
            d, row, col = heapq.heappop(max_heap)
            d = -d
            if row == n - 1 and col == n - 1:
                return d  

            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < n and 0 <= nc < n:
                    new_safe = min(d, visits[nr][nc])
                    if new_safe > max_safeness[nr][nc]:
                        max_safeness[nr][nc] = new_safe
                        heapq.heappush(max_heap, (-new_safe, nr, nc))
        return -1  
