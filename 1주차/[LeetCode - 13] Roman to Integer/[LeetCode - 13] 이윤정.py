class Solution:
    def romanToInt(self, s: str) -> int:
        ## 만들 수 있는 코드
        code = {'M' : 1000, 'CM' : 900, 'D' : 500, 'CD' : 400, 'C' : 100, 'XC' : 90, 'L' : 50, 'XL' : 40, 'X' : 10, 'IX' : 9, 'V' : 5, 'IV' : 4, 'I' : 1}
        res = 0
        i = 0
        
        while i < len(s):
            ## dict에서 key 존재 여부 확인 = 문자열 포함 여부 확인과 동일
            if i+1 < len(s) and s[i] + s[i+1] in code: 
                res += code[s[i] + s[i+1]]
                i += 2
            else:
                res += code[s[i]]
                i += 1
        
        return res