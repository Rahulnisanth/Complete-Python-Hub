# SENTENCE SIMILARITY III
def areSentencesSimilar(sentence1: str, sentence2: str) -> bool:
    words1 = sentence1.split()
    words2 = sentence2.split()
    if len(words1) > len(words2):
        words1, words2 = words2, words1
    i, j = 0, 0
    N1, N2 = len(words1), len(words2)
    # Prefix
    while i < N1 and i < N2 and words1[i] == words2[i]:
        i += 1
    # Suffix
    while j < N1 - i and j < N2 - i and words1[N1 - j - 1] == words2[N2 - j - 1]:
        j += 1
    return (i + j) == N1 or (i + j) == N2


# REVERSE LETTERS ONLY :
def reverseOnlyLetters(self, s: str) -> str:
    right = len(s) - 1
    answer = ""
    for i, ch in enumerate(s):
        if ch.isalpha():
            while not s[right].isalpha():
                right -= 1
            answer += s[right]
            right -= 1
        else:
            answer += ch
    return answer
