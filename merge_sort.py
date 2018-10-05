def merge_sort(list):
    # if array length is less then 1 we return array cause it's already sorted
    if len(list) <=1:
        return list

    # middle of array
    mid = int(len(list)/2)

    # left part recursion splitting
    left = merge_sort(list[:mid])

    # right part recursion splitting
    right = merge_sort(list[mid:])

    # merge
    return merger(left, right)

def merger(left, right):
    res = []

    # while both of arrays are not empty
    while len(left) > 0 and len(right) > 0:

        # adding the least element of left part to the result array
        # if it's smaller then least element of right part
        if left[0] <= right[0]:
            res.append(left[0])
            left = left[1:]
        # else
        else:
            res.append(right[0])
            right = right[1:]

    # adding remaining elements from left array
    if len(left) > 0:
        res += left

    # adding remaining elements from left array
    if len(right) > 0:
        res += right

    return res

your_example = [2,1,43,3,6,4,89,7,9]
print(merge_sort(your_example))
