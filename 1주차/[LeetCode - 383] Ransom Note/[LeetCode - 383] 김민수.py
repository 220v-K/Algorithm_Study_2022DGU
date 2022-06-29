class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        isCanConstruct=True
        dict={} #알파벳 개수 있는 딕셔너리
        for alph in magazine:
            if alph in dict:
                dict[alph]+=1
            else:
                dict[alph]=1
        
        for ralpha in ransomNote:
            if ralpha in dict:
                if dict[ralpha]>0:
                    dict[ralpha]-=1
                else:
                    isCanConstruct=False
                    return False
            else:
                isCanConstruct=False
                return False

        return isCanConstruct


ransomNote = "ab"
magazine = "aab"
result=Solution()
print(result.canConstruct(ransomNote, magazine))
                