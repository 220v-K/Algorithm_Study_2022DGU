class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        matSum = [ sum(ListA) for ListA in mat ]
        rangeList = [ i for i in range(len(matSum))]
        dic = dict( zip(rangeList, matSum) )
        sort_dic = sorted(dic.items(), key = lambda x : (x[1], x[0]))
        order = [ i[0] for i in sort_dic ]
        order = order[:k]
        return order
