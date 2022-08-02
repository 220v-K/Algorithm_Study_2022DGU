# Algorithm_Study_2022DGU

## 세부사항

- 기간 : 2022년 6월 27일 ~ 진행중
- 정기 모임 시간 : 매주 월요일 오후 2시 (방학 중)
- 문제 풀이 사이트 :
  - 백준 - https://www.acmicpc.net/
  - 릿코드 - https://leetcode.com/
  - 프로그래머스 - https://programmers.co.kr/learn/challenges
- 사용 언어 : Python, C++



## 참가 인원

- 이재원 (Python, C++)
- 김민석 (C++)
- 김민수 (Python)
- 박지원 (Python)
- 이윤정 (Python)



## 진행 방식

- 매 모임 마지막에 주제, 다음 주까지 풀어올 문제와 발표할 문제 지정.
- 모임 시간때 랜덤으로 발표할 문제 지정, 각자 돌아가며 자신의 풀이 설명(발표)
- 발표를 듣고 난 후 나머지 인원은 질문 or 더 나은 코드 제안.
- 모든 인원의 발표와 질답이 끝난 후에는 다음 주에 풀 주제에 대한 개념 공부 (+ 간단한 예제풀이)
- 다음 모임까지 지정한 문제 풀이 (+ 지난 주에 풀었던 문제 중 개선할 수 있을 것 같은 문제 코드 개선해보기)



#### 풀이 발표 방식 (ex)

1. 어떤 방식으로 접근했는지
2. 그에 따라 어떤 알고리즘을 사용했는지
3. 자신의 풀이 Code에 대한 간단한 설명
4. 시간, 공간 복잡도는 어떠한지
5. 흔치 않은 내장 함수나 라이브러리를 사용했다면, 어떤 것을 사용했고 어떻게 사용하는 것인지
6. 풀이 시 생각해내기 어려웠던 점 or 힘들었던 점이 있는지
7. 최선의 풀이일 것 같은지, 개선한다면 어떻게 할 수 있을 것 같은지, 코드를 개선했다면 어떻게 개선하였는지, 다른 사람의 코드를 보니 이렇게 하는 것이 더 좋은 것 같다.... 기타등등



#### 질문 방식 (ex)

1. 이런 방식으로 접근하면 더 쉬워요!
2. 그거 말고 이 알고리즘 쓰는 것도 괜찮아요!
3. 시/공간 복잡도가 그거 아니고 이거 아닌가요?
4. 이렇게 하면 시간 / 공간 복잡도를 개선할 수 있을 것 같아요!
5. 이런 라이브러리 / 함수도 있어요! 이거 쓰면 편해요!
6. 여기 코드 이렇게 바꾸는 게 더 간단해요!
7. 기타 등등



#### 주제 선정, 문제 선정, 개념 공부

일단은 이재원이 진행.

혹시 ''이번주는 이 주제에 대해 문제 풀고 싶다'' 하는 의견 환영

''이런 문제 풀어보는 건 어떠냐, 이 사이트에서 이런 문제 모음집 풀어보자'' 대환영



## Pull Request & Commit 규칙

#### 기본 규칙

- `master` 브랜치에는 `commit` 하지 않음.
- 각자 `branch` 를 생성하여 문제 풀이 시 마다 `commit`
- 모든 문제를 풀고, 모임 시간 전까지 `Pull Request` 요청 보내기.
- 문제 풀이에 대한 설명 등을 `markdown` 형식으로 작성하여 같이 `commit` 해도 좋음
- **자신이 직접 풀기 전에 다른 사람 코드 보지 않기! 풀고 `commit` 한 후에는 보고 비교해가며 자유롭게 공부.**

- \+ 귀찮으면 그냥 `master` 브랜치에 `commit`-`push` 하세요  



#### Commit Message

- [문제 사이트 - 문제 번호] 문제명
- 귀찮으면 대충 모든 문제 푼다음에 `[N주차] 이름` 써서 한번에 커밋해도 됩니다..^ㅁ^

ex) [LeetCode - 234] Palindrome Linked List



#### PR Message

- [N주차] 이름

ex) [1주차] 이재원



## 파일 구조

- **N주차**
  - [문제 사이트 - 문제 번호] 문제명1
    - [문제 사이트 - 문제 번호] 이름1
    - [문제 사이트 - 문제 번호] 이름2
  - [문제 사이트 - 문제 번호] 문제명2

> 프로그래머스의 경우 문제 번호가 문제 URL의 path에 적혀 있음.



#### 예시

- 1주차
  - [LeetCode - 234] Palindrome Linked List
    - [LeetCode - 234] 이재원.py
    - [LeetCode - 234] 이재원_문제풀이.md
    - [LeetCode - 234] 김민수.cpp
    - [LeetCode - 234] 박지원.py
  - [BOJ - 2557] Hello World
    - [BOJ - 2557] 이재원.py
    - [BOJ - 2557] 김민수.cpp
- 2주차
  - [Programmers - 42576] 완주하지 못한 선수
    - [Programmers - 42576] 이재원.py
    - [Programmers - 42576] 김민수.cpp
  - [Programmers - 42577] 전화번호 목록
    - [Programmers - 42577] 이재원.py
    - [Programmers - 42577] 김민수.cpp
- 3주차
  - ...
- ...



## 목차

### 1주차

LeetCode - [Challenges for New Users](https://leetcode.com/problem-list/challenges-for-new-users/)

- [13. Roman to Integer](https://leetcode.com/problems/roman-to-integer)
- [234. Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list)
- [383. Ransom Note](https://leetcode.com/problems/ransom-note)
- [412. Fizz Buzz](https://leetcode.com/problems/fizz-buzz)
- [876. Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list)
- [1337. The K Weakest Rows in a Matrix](https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix)
- [1342. Number of Steps to Reduce a Number to Zero](https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero)
- [1672. Richest Customer Wealth](https://leetcode.com/problems/richest-customer-wealth)


---

### 2주차

프로그래머스 - [코딩테스트 고득점 Kit](https://programmers.co.kr/learn/challenges?tab=algorithm_practice_kit)

**해시**

- [완주하지 못한 선수](https://programmers.co.kr/learn/courses/30/lessons/42576)
- [전화번호 목록](https://programmers.co.kr/learn/courses/30/lessons/42577)
- [위장](https://programmers.co.kr/learn/courses/30/lessons/42578)
- [베스트앨범](https://programmers.co.kr/learn/courses/30/lessons/42579)

**스택/큐**

- [기능개발](https://programmers.co.kr/learn/courses/30/lessons/42586)
- [프린터](https://programmers.co.kr/learn/courses/30/lessons/42587)
- [다리를 지나는 트럭](https://programmers.co.kr/learn/courses/30/lessons/42583)
- [주식가격](https://programmers.co.kr/learn/courses/30/lessons/42584)

---

### 3주차

프로그래머스 - [코딩테스트 고득점 Kit](https://programmers.co.kr/learn/challenges?tab=algorithm_practice_kit)

동적계획법(DP) 2문제, DFS/BFS 3문제.

#### Dynamic Programming

- [N으로 표현](https://school.programmers.co.kr/learn/courses/30/lessons/42895)
- [정수 삼각형](https://school.programmers.co.kr/learn/courses/30/lessons/43105)
  - [LeetCode - 97. Interleaving String](https://leetcode.com/problems/interleaving-string/) 

#### DFS/BFS

- [타겟 넘버](https://school.programmers.co.kr/learn/courses/30/lessons/43165)
- [네트워크](https://school.programmers.co.kr/learn/courses/30/lessons/43162)
- [단어 변환](https://school.programmers.co.kr/learn/courses/30/lessons/43163)

---

### 4주차

프로그래머스 - [코딩테스트 고득점 Kit](https://programmers.co.kr/learn/challenges?tab=algorithm_practice_kit) / LeetCode

동적계획법(DP) 2문제, DFS/BFS 2문제.

#### Dynamic Programming

- 프로그래머스 - [등굣길](https://school.programmers.co.kr/learn/courses/30/lessons/42898)
- LeetCode - [1696. Jump Game VI](https://leetcode.com/problems/jump-game-vi/)

#### DFS/BFS

- [여행경로](https://school.programmers.co.kr/learn/courses/30/lessons/43164)
- [퍼즐 조각 채우기](https://school.programmers.co.kr/learn/courses/30/lessons/84021)

---

### 5주차

프로그래머스 - [코딩테스트 고득점 Kit](https://programmers.co.kr/learn/challenges?tab=algorithm_practice_kit) / LeetCode

Hash, Greedy 1문제, 완전탐색 2문제

#### Hash

- [LeetCode] [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) (박지원)

#### Greedy

- [LeetCode] [135. Candy](https://leetcode.com/problems/candy/) (이재원)

#### 완전탐색

- [프로그래머스] [42839. 소수 찾기](https://school.programmers.co.kr/learn/courses/30/lessons/42839) (김민석)

- [프로그래머스] [42842. 카펫](https://school.programmers.co.kr/learn/courses/30/lessons/42842) (김민수)

---

### 6주차

프로그래머스 - [코딩테스트 고득점 Kit](https://programmers.co.kr/learn/challenges?tab=algorithm_practice_kit) / 백준 https://www.acmicpc.net/

Greedy 5문제

- [백준] [11000. 강의실 배정](https://www.acmicpc.net/problem/11000)
- [백준] [2437. 저울](https://www.acmicpc.net/problem/2437)
- [백준] [1700. 멀티탭 스케줄링](https://www.acmicpc.net/problem/1700)
- [프로그래머스] [42884. 단속카메라](https://school.programmers.co.kr/learn/courses/30/lessons/42884)
- [프로그래머스] [42861. 섬 연결하기](https://school.programmers.co.kr/learn/courses/30/lessons/42861)
