class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)

        maxlength = 0

        for i in nums:
            j = i + 1
            k = i
            tempMax = 0
            Fin = False

            while not Fin:
                if j in s:
                    s.remove(j)
                    j += 1
                elif k in s:
                    s.remove(k)
                    k -= 1
                else:
                    maxlength = max(maxlength, j - k - 1)
                    Fin = True
        
        return maxlength