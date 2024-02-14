class TimeMap:

    def __init__(self):
        self.key_dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_dict[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.key_dict[key]
        if arr is None:
            return None
        else:
            res = ""
            l,r=0,len(arr)-1
            while r>=l:
                mid = (l+r)//2
                if arr[mid][1] <= timestamp:
                    res = arr[mid][0]
                    l = mid + 1
                else:
                    r = mid - 1
            return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)