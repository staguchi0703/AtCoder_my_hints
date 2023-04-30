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

### 典型

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

### 01BFS

* 優先高いものは前から追加DFS的に使う
* 優先低いものは後ろに追加BFS的に使う
* 例　ABC176D
  ```python
  def resolve():
      '''
      code here
      '''
      from collections import deque

      H, W = [int(item) for item in input().split()]
      Ch, Cw = [int(item)-1 for item in input().split()]
      Dh, Dw = [int(item)-1 for item in input().split()]
      grid = [input() for _ in range(H)]
      max_num = 10**6
      fp = [[max_num] * W for _ in range(H)]

      que = deque([[Ch, Cw, 0]])
      fp[Ch][Cw] = 0

      walk = [(0, 1), (0, -1), (-1, 0), (1, 0)]
      warp = [(i, j) for i in range(-2, 3) for j in range(-2, 3) if (i, j) not in [(0, 0)] + walk]

      while que:
          y, x, w_num = que.popleft()

          for dy, dx in walk:
              ny = y + dy
              nx = x + dx

              if 0 <= ny <= H-1 and 0 <= nx <= W-1 and grid[ny][nx] == '.' and fp[ny][nx] > w_num:
                  que.appendleft([ny, nx, w_num])
                  fp[ny][nx] = w_num

          for dy, dx in warp:
              ny = y + dy
              nx = x + dx
              nw = w_num +1

              if 0 <= ny <= H-1 and 0 <= nx <= W-1 and grid[ny][nx] == '.' and fp[ny][nx] > nw:
                  que.append([ny, nx, nw])
                  fp[ny][nx] = nw

      if fp[Dh][Dw] != max_num:
          print(fp[Dh][Dw])
      else:
          print(-1)

  if __name__ == "__main__":
      resolve()

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

* 繰り上げ
* 繰り下げ
* 四捨五入

## 大文字小文字

* str.lower()
* str.upper()
* `import string; sting.ascii_lowercase`


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

## 株価チャートの理想的な売買

* もしすべての価格が分かっていて、手数料がなかった場合の最良
  * 価格が+になった日に全部売る
  * その前日に全部買う
* [m_solutions2020_d](https://atcoder.jp/contests/m-solutions2020/tasks/m_solutions2020_d)

## 二分探索

### 見つけてくる系ポイント

* `from bisect import bisect_left as bis`で呼びだす
* `temp_index = bis(List, val)`でList中のvalに一番近いindexを見つけてくる
* Listの範囲外だと、0かNが帰ってくるので、Nが帰ったらList[N]がindex errorするので注意

```python
from bisect import bisect_left as bis
NA, NB = [int(item) for item in input().split()]

As = [int(item) for item in input().split()]
Bs = [int(item) for item in input().split()]
Bs.sort()

cnt_A_and_B = 0
for item in As:
    b_index = bis(Bs, item)
    if b_index < NB: 
        if item == Bs[b_index]:
            cnt_A_and_B +=1

```

### めぐる式二分探索

* OKを探してくる探索
* 小さいとNGで大きいとOKなので、最小の解を探す方法
* 最大ならOKとNG逆に描けばいい

```python
ng = 0
ok = max(As)
def f(mid):
    # 判定式
    return mid
K #狙いの値

while ok - ng > 1:
    mid = int((ng + ok)/2)

    if f(mid) > K:
        ng = mid
    else:
        ok = mid
            
print(ok)
```


## `collections.Counter()`

* 返り値はCounterオブジェクト
* ほぼdictだと思って良いが、ないkeyを指定してもerrorにならず0を返す
* メソッド
  * `most_common(3)`頻出top3
  * `elements()`keyを連結して出力

```python
import collections

As = [1,1,2,2,2,4,4]
counter = collections.Counter(As)

for k, v in conter.items():
    pass
```

## Aを使うとBが使えなくなるルール

* 実は分かり訳す使っておいて、後から過去にさかのぼってルールを満たすように変更しても答えはあっている。
  * 結果を知ってから時間を巻き戻して制約に合わせればよい。
* 例えば、Aをを使うと10点えるが、Bを使うと50点得る。ただし、Bを使うとAが使えない。

## 要素が多いときSetを使う

* 配列で要素を作ると要素数が$10^8$超える場合、setで要素の座標を持っておく
* setのin演算子はオーダ1の演算で済む
* 例　ABC176E

```python
def resolve():
    '''
    code here
    '''
    H, W, M = [int(item) for item in input().split()]
    targets = [[int(item) -1 for item in input().split()] for _ in range(M)]

    col = [0 for _ in range(H)]
    row = [0 for _ in range(W)]

    bomb_set = set()
    # 配列で要素を作ると要素数が$10^8$超える場合、setで要素の座標を持っておく


    for i,j in targets:
        col[i] += 1
        row[j] += 1
        bomb_set.add((i,j))

    max_col = max(col)
    max_row = max(row)
    max_col_index = []
    max_row_index = []

    for i in range(H):
        if col[i] == max_col:
            max_col_index.append(i)

    for i in range(W):
        if row[i] == max_row:
            max_row_index.append(i)

    res = 0
    for item in max_col_index:
        for jtem in max_row_index:
            if (item,jtem) not in bomb_set:
                # setのin演算子はオーダ1
                res =max_col + max_row
                break
        else:
            res = max(res, max_col + max_row -1 )
    print(res)

if __name__ == "__main__":
    resolve()

```

## 配列の差分で作れる数

* 作れる差の最小値は配列の最大公約数
  * 同じ倍数の配列だと倍数分の差しか作れない
  * 素数が入っていれば、差をとり続ければ1になる
    * ユークリッドの互除法と同じ

## Union-Find

* グループ化されているか判別したり、大きさを調べたりできるデータ構造

```python
    class UnionFind():
    # 作りたい要素数nで初期化
    # 使用するインスタンス変数の初期化
        def __init__(self, n):
            self.n = n
            # root[x]<0ならそのノードが根かつその値が木の要素数
            # rootノードでその木の要素数を記録する
            self.root = [-1]*(n+1)
            # 木をくっつける時にアンバランスにならないように調整する
            self.rnk = [0]*(n+1)

        # ノードxのrootノードを見つける
        def Find_Root(self, x):
            if(self.root[x] < 0):
                return x
            else:
                # ここで代入しておくことで、後の繰り返しを避ける
                self.root[x] = self.Find_Root(self.root[x])
                return self.root[x]
        # 木の併合、入力は併合したい各ノード
        def Unite(self, x, y):
            # 入力ノードのrootノードを見つける
            x = self.Find_Root(x)
            y = self.Find_Root(y)
            # すでに同じ木に属していた場合
            if(x == y):
                return 
            # 違う木に属していた場合rnkを見てくっつける方を決める
            elif(self.rnk[x] > self.rnk[y]):
                self.root[x] += self.root[y]
                self.root[y] = x

            else:
                self.root[y] += self.root[x]
                self.root[x] = y
                # rnkが同じ（深さに差がない場合）は1増やす
                if(self.rnk[x] == self.rnk[y]):
                    self.rnk[y] += 1
        # xとyが同じグループに属するか判断
        def isSameGroup(self, x, y):
            return self.Find_Root(x) == self.Find_Root(y)

        # ノードxが属する木のサイズを返す
        def Count(self, x):
            return -self.root[self.Find_Root(x)]
```