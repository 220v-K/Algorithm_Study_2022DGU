class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ListA = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                ListA.append("FizzBuzz")
            elif i % 3 == 0:
                ListA.append("Fizz")
            elif i % 5 == 0:
                ListA.append("Buzz")
            else:
                ListA.append(str(i))
                
        return ListA