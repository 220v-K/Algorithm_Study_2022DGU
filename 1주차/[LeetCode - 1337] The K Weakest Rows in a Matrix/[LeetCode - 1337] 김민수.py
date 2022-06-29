class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        dict={} # 1 개수 담는 dict key는 row 번호, value는 1 개수
        for i in range(len(mat)):
            num=0 #num는 1개수
            for j in range(len(mat[i])):
                if mat[i][j]==1:
                    num+=1
            dict[i]=num
        
        #dictonary value로 sorted 정렬
        sorted_tuple=sorted(dict.items(), key=lambda x:x[1])

        #k까지 첫 번째 원소만 리스트로 반환
        result_list=[]
        for i in range(0,k):
            result_list.append(sorted_tuple[i][0])

        return result_list

    

        




