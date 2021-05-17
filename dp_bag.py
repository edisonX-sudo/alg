goods_info = [
    ("null", 0, 0),
    ("guitar", 1, 1500),
    ("audio", 4, 3000),
    ("pc", 3, 2000)
]
figure_pounds = 4


def best_value_in_bag(pounds):
    dp = [[0 for _ in range(pounds + 1)] for _ in goods_info]
    for good_inx, good_info in enumerate(goods_info):
        g_name, g_weight, g_value = good_info
        for design_pounds in range(pounds + 1):
            if design_pounds == 0 or g_name is 'null':
                dp[good_inx][design_pounds] = 0
            elif design_pounds >= g_weight:
                dp[good_inx][design_pounds] \
                    = max(dp[good_inx - 1][design_pounds], g_value + dp[good_inx - 1][design_pounds - g_weight])
            else:
                dp[good_inx][design_pounds] = dp[good_inx - 1][design_pounds]
    return dp[-1][-1]


if __name__ == '__main__':
    res = best_value_in_bag(figure_pounds)
    print(res)
