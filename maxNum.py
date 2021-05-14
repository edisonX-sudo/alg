def maxNum(arr):
    if len(arr) == 1:
        return arr[0]
    if maxNum(arr[1:]) > arr[0]:
        return maxNum(arr[1:])
    else:
        return arr[0]


if __name__ == '__main__':
    arr = [2, 1, 30, 6, 5, 4, 9]
    print(maxNum(arr))
