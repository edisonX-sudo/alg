def count_str_seq(s1, s2):
    dp = [[0 for _ in range(len(s2))] for _ in range(len(s1))]
    max_num = 0
    for i1 in range(len(s1)):
        for i2 in range(len(s2)):
            c1, c2 = s1[i1], s2[i2]
            if c1 == c2:
                if i1 - 1 < 0 or i2 - 1 < 0:
                    dp[i1][i2] = 0
                dp[i1][i2] = dp[i1 - 1][i2 - 1] + 1
                max_num = max(max_num, dp[i1][i2])
            else:
                dp[i1][i2] = 0

    return max_num


if __name__ == "__main__":
    print(count_str_seq("fish", "fosh"))
