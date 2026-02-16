from collections import defaultdict

class FrequencyTracker:

    def __init__(self):
        self.num_freq = defaultdict(int)
        self.freq_count = defaultdict(int)

    def add(self, number: int) -> None:
        old_freq = self.num_freq[number]
        
        if old_freq > 0:
            self.freq_count[old_freq] -= 1
        
        new_freq = old_freq + 1
        self.num_freq[number] = new_freq
        self.freq_count[new_freq] += 1

    def deleteOne(self, number: int) -> None:
        old_freq = self.num_freq[number]
        
        if old_freq == 0:
            return
        
        self.freq_count[old_freq] -= 1
        
        new_freq = old_freq - 1
        self.num_freq[number] = new_freq
        
        if new_freq > 0:
            self.freq_count[new_freq] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq_count[frequency] > 0
