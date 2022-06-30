class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        dict={} 
        
        for i in range(len(mat)):
            num=0 
            for j in range(len(mat[i])):
                if mat[i][j]==1:
                    num+=1
            dict[i]=num
        
        sorted_tuple=sorted(dict.items(), key=lambda x:x[1])
        
        result_list=[]
        for i in range(0,k):
            result_list.append(sorted_tuple[i][0])

        return result_list

    

        




