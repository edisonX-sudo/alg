def half_divide_search(arr_in_order, target):
    if len(arr_in_order) == 0:
        return False
    less_arr, mid_num, greater_arr = half_divide(arr_in_order)
    if mid_num < target:
        return half_divide_search(greater_arr, target)
    elif mid_num > target:
        return half_divide_search(less_arr, target)
    else:
        return True


def half_divide(arr):
    mid_inx = int(len(arr) / 2)
    return arr[:mid_inx], arr[mid_inx], arr[mid_inx + 1:]


if __name__ == '__main__':
    print(half_divide_search([1, 3, 4, 5, 7, 88], 5))
