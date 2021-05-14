def halfDevideSearch(arr_in_order, target):
    if len(arr_in_order) == 0:
        return False
    less_arr, mid_num, greater_arr = halfDevide(arr_in_order)
    if mid_num < target:
        return halfDevideSearch(greater_arr, target)
    elif mid_num > target:
        return halfDevideSearch(less_arr, target)
    else:
        return True


def halfDevide(arr):
    mid_inx = int(len(arr) / 2)
    return arr[:mid_inx], arr[mid_inx], arr[mid_inx + 1:]


if __name__ == '__main__':
    print(halfDevideSearch([1, 3, 4, 5, 7, 88], 5))
