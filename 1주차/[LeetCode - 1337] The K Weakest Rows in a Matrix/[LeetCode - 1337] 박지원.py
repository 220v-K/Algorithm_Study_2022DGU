class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        list_len = len(mat)
        a = []
        
        for i in range(0, list_len): 
            b = []
            b.append(i)
            b.append(sum(mat[i]))
            a.append(b)
        print(a)    ## [[행, 모두더한값]]
        a.sort(key = lambda x:x[1]) 
        print(a)
        
        res_list = []
        for i in range(0,k):
            res_list.append(a[i][0])
            
        return res_list