Solution 1
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
        
Solution 2         
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= pow(-2,31) and x <= (pow(2,31)+1):
            r = 0
            s = abs(x)
            while s > 0:
                d =  s % 10
                r = r * 10 + d
                s //= 10

            if r >= pow(-2,31) and r <= (pow(2,31)+1):
                if x > 0:
                    r = r
                else:
                    r = -r
            else:
                return 0
        else:
            return 0

        if r == x and x > 0:
            return True
        elif r == x and x < 0:
            return False
        elif x == 0:
            return True
