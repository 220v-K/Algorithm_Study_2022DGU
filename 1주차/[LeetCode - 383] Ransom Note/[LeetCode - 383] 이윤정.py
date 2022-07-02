class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ran = list(ransomNote)
        
        for i in ran:
            if i not in magazine:
                return False
            else:
                magazine = magazine.replace(i, "", 1)  ## 동일한 문자 하나 삭제(동일 값 존재해도 1개만)
        return True