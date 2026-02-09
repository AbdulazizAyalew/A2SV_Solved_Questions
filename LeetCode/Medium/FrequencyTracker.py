class FrequencyTracker:

    def __init__(self):
        self.list = []
        self.dictt = {}
        self.freq = {}

    def add(self, number: int) -> None:
        self.list.append(number)
        
        if number in self.dictt:
            freqq = self.dictt[number]
            if freqq in self.freq:
                self.freq[freqq] -= 1
            self.dictt[number] += 1
            new_freq = self.dictt[number]
            if new_freq in self.freq:
                self.freq[new_freq] += 1
            else:
                self.freq[new_freq] = 1
        
        else:
            self.dictt[number] = 1
            if 1 in self.freq:
                self.freq[1] += 1
            else:
                self.freq[1] = 1
        

    def deleteOne(self, number: int) -> None:

        if number in self.dictt and self.dictt[number] != 0:
            num_occr = self.dictt[number]
            if num_occr in self.freq:
                self.freq[num_occr] -= 1
            # self.list.remove(number)
            self.dictt[number] -= 1
            if num_occr - 1 in self.freq:
                self.freq[num_occr-1] += 1
            else:
                self.freq[num_occr-1] = 1
        elif number in self.dictt and self.dictt[number] == 0:
            del self.dictt[number]
        
            
        

    def hasFrequency(self, frequency: int) -> bool:
        if frequency in self.freq and self.freq[frequency] > 0:
            return True
        return False


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
