# coding=utf-8
# This is a sample Python script.

# Press ⇧⌘F11 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def GCD(v1, v2):
    min_num = min(v1, v2)
    max_num = max(v1, v2)
    if min_num == 0:
        return max_num
    return GCD(max_num % min_num, min_num)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(GCD(1680, 64))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
