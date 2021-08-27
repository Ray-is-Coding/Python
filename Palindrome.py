class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = abs(x)
        s = int(str(a)[::-1])
        
        if x > 0 and s == x:
            return True
        elif x < 0 and s == x:
            return False
        elif x == 0: 
            return True
        
