class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = []
        for i in range(1,n+1):
            friends.append(i)
        print(friends)
        return self.winnercheck(0,friends,k)
        
    def winnercheck(self,start,friends,k):
        if len(friends) == 1:
            return friends[0]
        
        failed = (start + k - 1) % len(friends)
        del friends[failed]
        nextt = failed % len(friends) 
        print(friends)
        return self.winnercheck(nextt,friends,k)
    

