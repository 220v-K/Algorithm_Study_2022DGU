class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ##"IV":4, "IX":9,"XL":40, "XC":90, "CD":500,"CM":900
        symbol = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        
        i = 0
        tmp1 = 0
        tmp2 = 0
        res = 0
        
        while i < len(s):
            tmp1 = symbol.get(s[i])
            if i+1 == len(s): ## 마지막 글자일때 
                res += tmp1
                i += 1
                break;
            tmp2 = symbol.get(s[i+1]) ## 그외 
            if tmp1 < tmp2:
                res -= tmp1
                res += tmp2
                i += 2
            else :
                res += tmp1
                i += 1
        return res
            
            