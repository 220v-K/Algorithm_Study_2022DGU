## 접근

그냥 두 string을 vector\<char>에 담고,

ransomNote를 처음부터 순회하며 magazine에서 find하고 있으면 제거, 없으면 return `false`.



## 복잡도

시간 복잡도 : O(n<sup>2</sup>)

- vector에 넣을 때 O(n)
- `for` 문 내의 `find` 함수 때문에 O(n<sup>2</sup>)
- erase()도 O(n)이 걸리므로, for문 안에 있는걸 감안하여 O(n<sup>2</sup>)
- 따라서, O(n<sup>2</sup>)



공간 복잡도 : O(n)

- ransomNote, magazine을 담을 vector\<char> : O(n)



## 평가

이것도 복잡도를 신경쓰지 않고 간단하게 생각해서 그냥 find를 사용했는데,

각 string에 들어 있는 알파벳의 개수를 세서 비교한다면, 시간복잡도 O(n)으로 풀어낼 수 있다.