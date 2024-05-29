''' 
Problem Statement :
You wish to help Ashish, who possesses a collection of N strings, some of which may be duplicated, and has been assigned the task of finding the kth unique string. If the number of unique strings is less than k, he needs to display an empty string. Considering you are Ashish's best friend can you assist him with this challenge?
'''
n = int(input())
letter = {}
for _ in range(n):
    ch = input()
    if ch in letter:
        letter[ch] += 1
    else:
        letter[ch] = 0
k = int(input())

result = ''
for key, value in letter.items():
    if value < k and k > 0:
        result = key
        k -= 1
print(result)


'''
Problem Statement :
One day jack finds a string of characters. He is very keen to arrange the characters in reverse order, i.e., first characters become the last characters, second characters become the second-last characters, and so on. Now he wants your help  to find the kth character from the new string formed after reverse the original string.
'''
n, k = list(map(int, input().split()))
word = input()
print(word[n - k])


'''
Problem Statement :
Once upon a time, a city biker embarked on an exciting road trip. This journey was laid out across a sequence of n+1 points, each with varying altitudes. The biker's adventure commenced at point 0, where the altitude was a humble 0 meters above sea level.

During his expedition, he encountered different terrains. For every segment between points i and i+1, where 0≤i<n, the biker faced varying challenges in altitude. Each segment was represented by an integer array called gain of length n, where gain[i] denoted the net gain in altitude between points i and i+1.

The biker's goal was to find the highest altitude he reached during his journey. This altitude was determined by the net gain in altitude at each point along the way. It could be a thrilling peak or a serene valley, depending on the varying gains between consecutive points.
'''
n = int(input())
altitudes = list(map(int, input().split()))
maxx, temp = 0, 0
for i in range(n):
    temp += altitudes[i]
    maxx = max(maxx, temp)
print(maxx)


'''
Problem Statement
A machine could be fed with queries of type (a,b).
Where (a b) means we have a number ‘b’ ‘a’ times. 
Output the absolute difference between the number that appears most number of times and least number of times (least number of times must be at-least once. If there are multiple possible answers print the maximum possible absolute difference.
'''
n = int(input())
mapper = {}
for _ in range(n):
    count, num = list(map(int, input().split()))
    if num in mapper:
        mapper[num] += count
    else:
        mapper[num] = count

maxFreq = -1
minFreq = float('inf')
maxNum = None
minNum = None
for k, v in mapper.items():
    if v > maxFreq:
        maxFreq = v
        maxNum = k
    if v < minFreq:
        minFreq = v
        minNum = k

print(abs(maxNum - minNum))

