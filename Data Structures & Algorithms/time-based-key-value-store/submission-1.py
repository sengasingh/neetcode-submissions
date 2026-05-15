class TimeMap:

    def __init__(self):
        self.mapp = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mapp:
            self.mapp[key] = [(value,timestamp)]
        else:
            self.mapp[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.mapp or len(self.mapp[key]) == 0:
            return ''

        if timestamp < self.mapp[key][0][1]:
            return ''

        if timestamp > self.mapp[key][-1][1]:
            return self.mapp[key][-1][0]

        l, r, best = 0, len(self.mapp[key])-1, -1
        while l <= r:
            mid = (l+r)//2
            val, ts = self.mapp[key][mid]

            if ts < timestamp:
                best = val
                l = mid + 1
            elif ts > timestamp:
                r = mid - 1
            else:
                return val
        
        return best
            