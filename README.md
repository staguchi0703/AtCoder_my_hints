# AtCoder_my_hints

## DFS


## BFS

## エラストテネスの篩

### Xまでの素数のリストを求める

```python:sieve.py

def get_sieved_list(x):
    dp = [1 if item % 2 == 0 else 0 for item in range(x+1)]
    dp[:3] = [2,1,1]

    prim_candi = 2
    for prim_candi in range(3, x+1)
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



## 浮動小数点の扱い

## 大文字小文字


## ループ中にリストを削除したり挿入したり