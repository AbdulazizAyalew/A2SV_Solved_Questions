class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        x = 0
        y = 0

        sec_set = Counter(secret)
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                x += 1
                sec_set[secret[i]] -= 1
        
        for j in range(len(secret)):
            if guess[j] != secret[j]:
                if sec_set[guess[j]] != 0:
                    y += 1
                    sec_set[guess[j]] -= 1
    
        return f"{x}A{y}B"
