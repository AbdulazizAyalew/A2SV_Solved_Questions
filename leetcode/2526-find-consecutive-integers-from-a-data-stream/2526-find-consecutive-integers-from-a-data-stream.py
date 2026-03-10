class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.datas = deque()
        self.vals = {value:0}

    def consec(self, num: int) -> bool:
        self.datas.append(num)
        if len(self.datas) < self.k:
            if num not in self.vals:
                self.vals[num] = 1
            else:
                self.vals[num] += 1
            return False
        else:
            if num not in self.vals:
                self.vals[num] = 1
                self.vals[self.datas[0]] -= 1
                self.datas.popleft()
                return  False
            else:
                self.vals[num] += 1
                counted = self.vals[self.value]
                self.vals[self.datas[0]] -= 1
                self.datas.popleft()
                return counted == self.k
    
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)