def count_str_subseq(s1, s2):
    dp = [[0 for _ in range(len(s2))] for _ in range(len(s1))]
    for i1 in range(len(s1)):
        for i2 in range(len(s2)):
            c1, c2 = s1[i1], s2[i2]
            if c1 == c2:
                dp[i1][i2] = dp[i1 - 1][i2 - 1] + 1 if i1 - 1 >= 0 and i2 - 1 >= 0 else 1
            else:
                t1 = dp[i1 - 1][i2] if i1 - 1 >= 0 else 0
                t2 = dp[i1][i2 - 1] if i2 - 1 >= 0 else 0
                dp[i1][i2] = max(t1, t2)
    return dp[-1][-1]


if __name__ == "__main__":
    print(count_str_subseq("fish", "fosh"))
