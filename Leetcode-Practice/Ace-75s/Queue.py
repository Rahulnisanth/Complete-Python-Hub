# NUMBER OF RECENT CALLS :
class RecentCounter:
    def __init__(self):
        self.count = []
    def ping(self, t: int) -> int:
        self.count.append(t)
        while self.count[0] < t - 3000:
            self.count.pop(0)
        return len(self.count)

