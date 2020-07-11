# AtCoder_my_hints

## DFS

* numpy.whereとか使いたくなるが、激重なのでNG
* collection.queとlistのスライスで攻めるのが◎

```python

import collections
H, W = [int(item) for item in input().split()]
grid = [[item for item in input()] for _ in range(H)]

stack = collections.deque()
fp = [[0 for _ in range(W)] for _ in range(H)]



stack.append(start) #任意の開始ポイント
is_found = False

fp[start[0]][start[1]] = 1
goto = [[1, 0], [0, 1], [-1, 0], [0, -1]]


while stack:
    temp = stack.pop()
    y, x = temp

    if grid[y][x] == 'g':
        is_found = True
        stack = False
        # 探索終了条件
    elif grid[y][x] == '#':
        pass
        #障害物
    else:
        for i in range(4):
            nx = x + goto[i][0]
            ny = y + goto[i][1]

            if 0 <= nx <= W-1 and 0 <= ny <= H-1:
                if fp[ny][nx] == 0:
                    stack.append([ny, nx])
                    fp[ny][nx] = fp[y][x] + 1

print('Yes') if is_found else print('No')

```


## BFS

```python

import collections
H, W = [int(item) for item in input().split()]
grid = [[item for item in input()] for _ in range(H)]

fp = [[-1 for _ in range(W)] for _ in range(H)]

# position[y, x]
# start [0,0]
# goal [H-1, W-1]

que = collections.deque([[0, 0, 1]])
fp[0][0] = 1
next_y_x = [[0, 1], [1, 0], [-1, 0], [0, -1]]
is_found = False

while que:
    temp = que.popleft()

    if temp[0] == H-1 and temp[1] == W-1:
        pass_num = temp[2]
        que = False
        is_found = True
    else:
        for dy, dx in next_y_x:
            ny = temp[0] + dy
            nx = temp[1] + dx

            if 0 <= ny <= H-1 and 0 <= nx <= W-1:
                if grid[ny][nx] == '.' and fp[ny][nx] == -1:
                    que.append([ny, nx, temp[2]+1])
                    fp[ny][nx] = temp[2] + 1

print(pass_num) if is_found else print(-1)
```

## エラストテネスの篩

### Xまでの素数のリストを求める

```python:sieve.py

def get_sieved_list(x):
    dp = [1 if item % 2 == 0 else 0 for item in range(x+1)]
    dp[:3] = [2,1,1]

    for prim_candi in range(3, x+1):
        temp_num = prim_candi
        while temp_num <= x:
            dp[temp_num] += 1
            temp_num += prim_candi
        if prim_candi >= x:
            return [i  for i in range(x+1) if dp[i] == 1]
```

### 使用したテクニック

* dpリストで値を調べた数を数える
* dpリストははじめから0,1と偶数は検査済み
* forで0,1,2を除いた素数の候補を調べる
* while文の中でdpをindex参照で操作するので、`O(1)`の時間
* 倍数は`temp_num += primt_candi`で作って、dpに記録する

## 存在の有無や数をlistのindexで高速に調べる

`A_list`の中に`B_list`があるか判別

```python
# O(n^2)のためNG
def chk_ng(A_list, B_list):
    res = []
    for i in A_list:
        for j in B_list:
            if i == j:
                res.append(i)
    return res

# 高速化O(N)
def chk(A_list, B_list):
    A_max = max(A_list)
    dp = [0 for _ in range(A_max+1)]
    for i in A_list:
        dp[i] += 1

    res = []
    for j in B_list:
        if j <= A_max:
            if dp[j]:
                res.append(j)
    return res
```

### 使用したテクニック

* for文の中に'O(N)'の処理が入らないように、A_listの有無はdpリストのスライス'O(1)'で判別した
* DPのリストのindexが範囲を超えないようにA_listの最大値以下で検索した
* A_listの最大値を求める計算がfor文の中に入ると'O(N)'の処理を毎回してしまうので、for文の外で値を得て使用した


## 浮動小数点の扱い

## 大文字小文字


## ループ中にリストを削除したり挿入したり

## 素因数分解

```python
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a
```

## bit全探索

```python
for i in range(2**(N)):
    for j in range(N):
        if ((i >> j) & 1):
            pass
```