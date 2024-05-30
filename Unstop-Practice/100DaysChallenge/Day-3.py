'''
Problem Statement
Bob is going on a trip to Japan, where he finds a big pudding shop, where he sees a menu and food challenges. Bob accepts the challenge, so here are the game rules:
The pudding shop assigns an integer number to the puddings. The good puddings have a number which when reversed twice remains same.
Bob has to find the good puddings and then for each pudding mark it as 1 or 0.
'''
t = int(input())
for _ in range(t):
    num = input().strip()
    if(num.rstrip("0") == num): print(1)
    else: print(0)


'''
Problem Statement
Once upon a time, a city biker embarked on an exciting road trip. This journey was laid out across a sequence of n+1 points, each with varying altitudes. The biker's adventure commenced at point 0, where the altitude was a humble 0 meters above sea level.

During his expedition, he encountered different terrains. For every segment between points i and i+1, where 0≤i<n, the biker faced varying challenges in altitude. Each segment was represented by an integer array called gain of length n, where gain[i] denoted the net gain in altitude between points i and i+1.

The biker's goal was to find the highest altitude he reached during his journey. This altitude was determined by the net gain in altitude at each point along the way. It could be a thrilling peak or a serene valley, depending on the varying gains between consecutive points.
'''
n = int(input())
altitudes = list(map(int, input().split()))
maxAltitude, temp = 0, 0
for i in range(n):
    temp += altitudes[i]
    maxAltitude = max(maxAltitude, temp )
print(maxAltitude)


'''
Problem Statement
John and Mocha are two friends. Mocha made his dictionary of strings of length n and called it Alien dictionary. John tries to test Mocha's Alien dictionary by giving one string s to Mocha. Help Mocha check if John's string can be segmented into a sequence of one or more words from Mocha's Alien dictionary.

Note: The words in the dictionary contain unique words of lowercase English letters and can be found multiple times in the segmentation.
'''
word = input().strip()
word_len = len(word)
n = int(input())
dictionary = [input().strip() for _ in range(n)]
dp = [0] * (word_len + 1)
dp[0] = 1
for i in range(1, word_len + 1):
    for j in range(i):
        if dp[j] and word[j:i] in dictionary:
            dp[i] += 1
    print(dp[i])
print("true" if dp[-1] >= 1 else "false")


'''
Problem Statement
James has two binary strings, ‘a’ and ‘b’. He asked Jimmy to find the sum of the number of positions at which the corresponding bits are different between a and all contiguous substrings of b of length of a.
'''
a = input().strip()
b = input().strip()
len1, len2 = len(a), len(b)
ones, total = 0, 0
diff = len2 - len1 + 1

for i in range(diff):
    if b[i] == '1': ones += 1

for i in range(len1):
    if a[i] == '0': total += ones
    else: total += (diff - ones)
    if i == len1 - 1: break
    if b[i] == '1': ones -= 1
    if b[i + diff] == '1': ones += 1

print(total)