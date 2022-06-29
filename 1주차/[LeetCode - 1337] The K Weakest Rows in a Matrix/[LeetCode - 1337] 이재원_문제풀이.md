## 접근

한 열의 리스트의 합계 = 한 열의 병사의 수

이므로, 모든 열의 병사 수를 담은 리스트를 일단 생성.

리스트 index 번호를 key값, 병사 수를 value값으로 하는 dictionary를 생성.

이후 dictionary를 병사 수를 1순위, 병사 수가 같다면 index를 기준으로 하여 정렬하고,

정렬한 dictionary에서 index값만 가져와 다시 return해줌.



## 복잡도

시간 복잡도 : O(n)

공간 복잡도 : O(n<sup>2</sup>)

- dictionary 에서 S(2n)이므로
- 입력받는 mat 이중 리스트에서 O(n<sup>2</sup>)