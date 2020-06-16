# AtCoder_my_hints

## DFS


## BFS

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