from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""

        target = Counter(t)
        window = defaultdict(int)

        required = len(target)   # Number of unique characters we need
        formed = 0               # Number of characters currently satisfied

        left = 0

        min_len = float("inf")
        start = 0

        for right in range(len(s)):
            char = s[right]
            window[char] += 1

            # This character's required frequency has just been met
            if char in target and window[char] == target[char]:
                formed += 1

            # Try to shrink the window while it remains valid
            while formed == required:

                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left

                left_char = s[left]
                window[left_char] -= 1

                # Removing this character breaks the requirement
                if left_char in target and window[left_char] < target[left_char]:
                    formed -= 1

                left += 1

        if min_len == float("inf"):
            return ""

        return s[start:start + min_len]