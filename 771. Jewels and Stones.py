class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        output = 0
        for word in list(jewels):
                output += stones.count(word)
        return output
