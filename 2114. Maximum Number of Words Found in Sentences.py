class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_len = 0
        for i in sentences:
             a = i.split(' ')
        if len(a) > max_len:
             max_len = len(a)
        return(max_len)
