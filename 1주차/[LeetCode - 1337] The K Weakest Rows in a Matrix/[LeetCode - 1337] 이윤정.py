class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        tmp = []
        res = []
        cnt = 0

        ## 군인(1)은 무조건 민간인(0)보다 앞에 있으므로 민간인 index-1 = 마지막 군인 index (index 메소드는 중복 값 있어도 가장 작은 인덱스 return)
        for i in mat:
            try:
                tmp.append([i.index(0)-1, cnt])  ## 마지막 군인 index랑 행 번호 저장 
                cnt += 1
            except: ## 민간인(0)이 없는 경우 예외 처리
                tmp.append([len(i)-1, cnt])
                cnt += 1
                
        tmp.sort()  ## 각 리스트의 첫번째 원소(: 마지막 군인 index) 기준으로 정렬
        tmp = tmp[:k]
        
        for i in tmp:
            res.append(i[1])
        
        return res