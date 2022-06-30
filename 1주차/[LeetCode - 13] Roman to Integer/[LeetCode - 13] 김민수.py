class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        result=0

        for i in range(len(s)):
            result+=dict[s[i]]
            print(s[i],result)
            if i>0 and dict[s[i-1]]<dict[s[i]]: 
                result-=2*dict[s[i-1]]
                print(s[i],result)
                
        return result
