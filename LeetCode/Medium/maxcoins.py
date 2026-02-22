class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()

        no_coins = 0
        i = len(piles) - 2
        count = 0

        while count < (len(piles) // 3):
            no_coins += piles[i]
            i -= 2
            count += 1
        

        
        return no_coins