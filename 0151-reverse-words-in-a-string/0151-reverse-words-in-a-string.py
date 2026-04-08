class Solution:
    def reverseWords(self, s: str) -> str:
        list_of_words = s.split()
        # print(list_of_words)
        list_of_words = reversed(list_of_words)
        # print(list(list_of_words))

        return " ".join(list(list_of_words))


