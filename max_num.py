def max_num(arr):
    if len(arr) == 1:
        return arr[0]
    if max_num(arr[1:]) > arr[0]:
        return max_num(arr[1:])
    else:
        return arr[0]


if __name__ == '__main__':
    arr = [2, 1, 30, 6, 5, 4, 9]
    print(max_num(arr))
