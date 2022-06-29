## 접근

입력받은 로마 숫자를 하나하나 변환하여 숫자의 배열로 만들고,

( XIV -> 10, 1, 5 )

숫자의 배열을 index=0 부터 끝까지 조사하여, 앞의 숫자가 뒤의 숫자보다 작은 경우 ( num[i] < num[i+1] ) 에만 그 두 숫자의 차를 구해 다시 집어넣은 후, 마지막에 총 합계를 구했다.

문제에도 쓰여 있듯, IV, IX, XL, XC, CD, CM을 처리해주는 방법만 고민해 본다면 어렵지 않은 문제였던 것 같음.



### 복잡도

시간복잡도 : O(n)

- 첫 `for` 문에서 O(n)

- 두 번째 `for` 문에서 순회하며 조사하므로 O(n)

  (`isReverse` == `true`) 일 시 타고 들어가는 `if` 문의 insert(), erase()가 각각 O(n)이긴 하지만,

  삭제할 개수 자체가 n개에 준하지 않으므로 O(n)에서 그침.

- 세 번째 `for` 문에서 O(n).
- 따라서 O(n)



공간복잡도 : O(n)

- vector\<int\> 가 O(n)
- 나머지는 O(1) 



## 기타

https://leetcode.com/problems/roman-to-integer/discuss/1074149/JS-Python-Java-C%2B%2B-or-Switch-Dictionary-Solution-w-Explanation-or-beats-100

의 풀이가 굉장히 쉽고 깔끔한 것 같다.

문자열을 맨 뒤부터 순회하며 하나씩 더해 나가는데, 

IV 등을 만났을 때의 처리 아이디어가 좋음.

"XXIVII" 를 예시로 들어 보자면,

1. ans = 1
2. ans = 2
3. ans = 7
4. V가 더해진 다음 I가 더해지는 이 순서에, 4 < 7이므로 ans = 6
5. ans = 16
6. ans = 26



로마자 숫자가 1, 5, 10, 50, 100, 500, 1000.. 처럼,

5을 표현할 때는 IIIII가 아닌 V로 표현하게 되기 때문에, 

V보다 먼저 나오는 I의 경우 4를 곱하더라도 무조건 앞의 수보다 작게 됨.

이는 IX, XL, XC, CD, CM의 경우도 마찬가지.

default한 경우에서도

"XXIVII" 에서 맨 앞의 X 뒤의 XIVII 를 보면

절대 X*4인 40을 넘지 않게 됨.

40부터는 표현할 방법이 XXXX가 아닌 XL로 바뀌기 때문에, 

이와 같이 default한 경우에서는 항상 if문에 걸리지 않음.