class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        wealthSum_list=[]
        for i in accounts:
            sum=0
            for j in i:
                sum+=j
                wealthSum_list.append(sum)

        #오름차순 정렬
        sorted_list=sorted(wealthSum_list)

        #가장 뒤에 값 return
        return sorted_list[-1]

