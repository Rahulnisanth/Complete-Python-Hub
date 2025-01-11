# NUMBER OF RECENT CALLS :
class RecentCounter:
    def __init__(self):
        self.count = []
    def ping(self, t: int) -> int:
        self.count.append(t)
        while self.count[0] < t - 3000:
            self.count.pop(0)
        return len(self.count)


# Dota2Senate :
def predictPartyVictory(self, senate: str) -> str:
    radi, dire = deque([]), deque([])
    N = len(senate)
    for i in range(N):
        if senate[i] == "R":
            radi.append(i)
        else:
            dire.append(i)

    while radi and dire:
        r_idx = radi.popleft()
        d_idx = dire.popleft()
        if r_idx < d_idx:
            radi.append(r_idx + N)
        else:
            dire.append(d_idx + N)
    return "Radiant" if radi else "Dire"
