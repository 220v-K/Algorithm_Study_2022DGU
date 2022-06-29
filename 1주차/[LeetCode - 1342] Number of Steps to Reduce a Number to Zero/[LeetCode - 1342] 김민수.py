class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        step=0 #step 개수

        while num>0:
            if(num%2==0):
                num/=2
                step+=1

            elif(num%2==1):
                num-=1
                step+=1
        
        return step

