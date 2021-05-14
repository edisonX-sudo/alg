def arrPlus(arr):
    if len(arr) == 1:
        return arr[0]
    return arrPlus([arr[0]]) + arrPlus(arr[1:])


if __name__ == '__main__':
    print(arrPlus([1, 2, 3]))
