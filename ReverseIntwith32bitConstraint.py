class Solution:
    def reverse(self, x: int) -> int:
        if x >= pow(-2,31) and x <= (pow(2,31)+1):
            r = 0
            s = abs(x)
            while s > 0:
                d =  s % 10
                r = r * 10 + d
                s //= 10

            if r >= pow(-2,31) and r <= (pow(2,31)+1):
                if x > 0:
                    return r
                else:
                    return -r
            else:
                return 0
        else:
            return 0
       

       
        
        
        
        
            
            
            
        
