## 접근 방식

mod 연산을 통해 나눌 수 있는 지 판정.

if-elif-else로 처리. 

List.append() 로 리스트에 담아 return.



## 복잡도

시간 복잡도 : O(n)

- `for i in range(1, n+1)` 에서 매 반복마다 `if-elif-else` 에서의 비교 1~4회, `append()` 시간복잡도 O(1).

공간 복잡도 : O(n)

- n 크기의 리스트에 담아 return하므로 공간복잡도 O(n).



## 기타

복잡도 면에서는 따로 더 개선할 사항은 없을 것 같음.

다만 Python의 List Comprehension을 이용해 짧고 간결하게 처리할 수는 있어 보인다.