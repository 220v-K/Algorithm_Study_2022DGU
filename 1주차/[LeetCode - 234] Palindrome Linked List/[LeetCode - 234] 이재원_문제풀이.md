## 접근

Linked List를 순회하며, Reverse된 Linked List를 하나 만듬.

그리고, 뒤집어놓은 리스트와 원본 리스트를 처음부터 순회하며 하나씩 Node의 value를 비교함.



## 복잡도

시간복잡도 : O(n)

- getEnd에서 O(n)
- getReverse_ 자체에서 재귀를 제외하고는 O(1)
- getReverse_ 호출이 n회이므로 O(n)
- 따라서 getReverse() 에서 O(n)
- isPalindrome() 에서 getReverse를 제외하고 O(n)이므로
- 전체 시간복잡도는 효율성은 떨어지지만 어쨌든 O(n).



공간복잡도 : O(n)

- getEnd 에선 O(1)
- getReverse 에서 Reverse Linked List를 만드므로 O(n)
- 전체 O(n)



## 평가

굉장히 단순한 풀이법으로 너무 깊게 생각하지 않고 풀었다.

시간복잡도와 공간복잡도 자체는 O(n)이지만, 효율성을 따져본다면 좋지는 않은 코드이다.

다만 어떻게 개선할 지는 생각해 봐도 잘 모르겠다. 다른 사람의 코드를 보아야 할 듯.



** 