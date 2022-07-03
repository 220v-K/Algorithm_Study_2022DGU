class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ## 리스트로 저장
        mag_list = list(magazine)
        
        for i in range(0,len(ransomNote)):
            if(ransomNote[i] not in mag_list): 
                return False
            else:
                mag_list.remove(ransomNote[i]) ## 리스트에 있으면 제거 
        return True