# IBM Interview Questions
# No.of Collisions that occurred during the given speed traveling period of the particles...
def collisionParticles(speed, pos):
    count = 0
    # First half:
    for i in range(pos):
        if speed[i] > speed[pos]: count += 1
    # Second half :
    for i in range(pos + 1, len(speed)):
        if speed[i] < speed[pos]: count += 1
    return count

# Find the first occurrence of the word that has tha even maximum length among the given sentence, if not even 
# length word occurs return '00':
def longestEvenWord(sentence):
    mapper = {}
    max_len = 0
    for word in sentence.split():
        temp = len(word)
        if temp % 2 == 0:
            if temp not in mapper:
                mapper[temp] = [word]
            else:
                mapper[temp].append(word)
            max_len = max(max_len, temp)
    if len(mapper) <= 0:
        return '00'
    for k, v in mapper.items():
        if k == max_len:
            return v[0]