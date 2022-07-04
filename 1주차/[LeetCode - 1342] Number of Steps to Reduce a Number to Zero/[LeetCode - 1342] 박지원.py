class Solution:
    def numberOfSteps(self, num: int) -> int:
        
        cnt = 0
        i = 0
        while(num != 0):
            cnt += 1
            if num == 1:
                break;
            elif num % 2 == 0:
                num = int(num / 2)
            else:
                num -= 1 
            print(num)
           
        return cnt 