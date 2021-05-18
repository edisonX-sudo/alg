def arr_plus(arr):
    if len(arr) == 1:
        return arr[0]
    return arr_plus([arr[0]]) + arr_plus(arr[1:])


if __name__ == '__main__':
    print(arr_plus([1, 2, 3]))
