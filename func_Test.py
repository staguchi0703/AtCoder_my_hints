def get_sieved_list(x):
    dp = [1 if item % 2 == 0 else 0 for item in range(x+1)]
    dp[:3] = [2,1,1]

    prim_candi = 2
    while True:
        prim_candi += 1
        temp_num = prim_candi
        while temp_num <= x:
            dp[temp_num] += 1
            temp_num += prim_candi
        

        if prim_candi >= x:
            return [i  for i in range(x+1) if dp[i] == 1]


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

if __name__ == "__main__":
    print(chk(list(range(10**4)), list(range(10**4-13, 2*10**4))))