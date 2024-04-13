# [보물상자 비밀번호](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRUN9KfZ8DFAUo)

## 문제
각 변에 다음과 같이 16진수 숫자가 적혀 있는 보물상자가 있다. 보물 상자의 뚜껑은 시계방향으로 돌릴 수 있고, 한 번 돌릴 때마다 숫자가 시계방향으로 한 칸씩 회전한다.

각 변에는 동일한 개수의 숫자가 있고, 시계방향 순으로 높은 자리 숫자에 해당하며 하나의 수를 나타낸다. 보물상자에는 자물쇠가 걸려있는데, 이 자물쇠의 비밀번호는 보물 상자에 적힌 숫자로 만들 수 있는 모든 수 중, K번째로 큰 수를 10진수로 만든 수이다. N개의 숫자가 입력으로 주어졌을 때, 보물상자의 비밀번호를 출력하는 프로그램을 만들어보자. (서로 다른 회전 횟수에서 동일한 수가 중복으로 생성될 수 있다. 크기 순서를 셀 때 같은 수를 중복으로 세지 않도록 주의하자.)

## 풀이 방법
비밀번호를 만드는 과정 - **3중 for-loop**
1. 회전 횟수 `q = N//4`
    - 한 칸씩 회전시키면서, 각 변의 element 구성이 처음과 동일하기 전까지의 경우의 수
    - 변의 element 수와 동일하다 
2. 4개의 변에서의 시작 index `range(0, N, q)`
    - 변에 있는 element 수 `q` 만큼 interval을 두어 시작 index를 정한다
    - 해당 index에서 `q`개의 element로 숫자를 만든다.
3. 각 변의 element
    - hexa-symbol을 변환하는 table을 미리 만들어서 숫자로 변환한다
    - 16진법을 10진법으로 변환한다.

비밀번호를 만들었으면,
1. 발생할 수 있는 모든 수를 담는다. 
    - 중복 수를 없애기 위해 `set()`을 사용했다.
2. `set`을 `list`로 변환한다
3. `list`를 sorting한다
4. `K`번째 원소를 고른다