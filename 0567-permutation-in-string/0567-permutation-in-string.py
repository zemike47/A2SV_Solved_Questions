class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cntr_s1 = Counter(s1)

        left = 0
        window = ""

        for right in range(len(s2)):
            window += s2[right]

            cntr_window = Counter(window[left:right+1])

            if cntr_s1 == cntr_window:
                return True
            
            while (right - left + 1) >= len(s1):
                left += 1
            
        return False




