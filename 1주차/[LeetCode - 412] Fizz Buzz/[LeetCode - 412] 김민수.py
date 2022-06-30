class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answer_list=list()

        for i in range (1, n+1):
            if i%3==0 and i%5==0:
                answer_list.append("FizzBuzz")
            elif i%3==0:
                answer_list.append("Fizz")
            elif i%5==0:
                answer_list.append("Buzz")
            else:
                answer_list.append(str(i))
        
        return answer_list

    



