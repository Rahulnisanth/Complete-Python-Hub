# Pre-defined dictionary :
dictionary = [  "mobile", "it", "vac", 
                "itvac", "man", "mango", 
                "icecream", "and", "go", 
                "i", "love", "ice", "cream" ]

# Word breaking function using combinations :
def word_break(word, dict):
    buffer = []
    def helper(word, start, current):
        if start == len(word):
            buffer.append(" ".join(current))
        for i in range(start, len(word)):
            if word[start : i + 1] in dict:
                current.append(word[start : i + 1])
                helper(word, i + 1, current)
                current.pop()
    helper(word, 0, [])
    return buffer

# Input stream:
N = int(input())
for _ in range(N):
    word = input()
    result = word_break(word, dictionary)
    for word in result:
        print(word)