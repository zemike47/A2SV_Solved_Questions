class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity

        self.key_val_freq = {}
        self.freq_key = defaultdict(OrderedDict)

        self.min_freq = 0
    
    def _increase(self,freq,key):
        self.freq_key[freq].pop(key)

        if not self.freq_key[freq]:
            del self.freq_key[freq]

            if freq == self.min_freq:
                self.min_freq += 1
        
        self.freq_key[freq+1][key] = None


    def get(self, key: int) -> int:
        if key not in self.key_val_freq:
            return -1
        
        val,freq = self.key_val_freq[key]
        self._increase(freq,key)
        self.key_val_freq[key] = (val,freq+1)
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.key_val_freq:
            val,freq = self.key_val_freq[key]

            self.key_val_freq[key] = (value,freq+1)
            self._increase(freq,key)

            return
        
        if len(self.key_val_freq) == self.capacity:
            lfu_key,_ = self.freq_key[self.min_freq].popitem(last=False)


            if not self.freq_key[self.min_freq]:
                del self.freq_key[self.min_freq]
            
            del self.key_val_freq[lfu_key]

            
        self.key_val_freq[key] = (value,1)
        self.min_freq = 1
        self.freq_key[self.min_freq][key] = None








   





# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)