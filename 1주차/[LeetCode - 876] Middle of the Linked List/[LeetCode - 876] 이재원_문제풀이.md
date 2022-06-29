## 접근

모든 노드를 순회하며 node의 개수 저장.

이후 middle node의 index를 계산하여 middle node까지 순회 후 return.



## 복잡도

시간 복잡도 : O(n)

- 첫 순회에서 T(n)
- 두 번째 순회에서 T(n/2)



공간 복잡도 : O(n)

- 노드의 개수 O(n)