class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        g = math.gcd(len(str1), len(str2))      
        pattern = str1[:g]                     
        ok1 = pattern * (len(str1) // g) == str1  
        ok2 = pattern * (len(str2) // g) == str2
        if ok1 and ok2:
            return pattern
        return ""
        