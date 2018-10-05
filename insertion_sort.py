# list [l1, l2, l3, ... ,ln]
#
# for i = 2, 3, ... , n:
#     value := list[i]
#     j := i - 1
#     while j>0 and list[j] > value:
#         list[j+1] := list[j]
#         j := j - 1
#     list[j+1] := value

def insert_sort(list):
    # main cycle
    for i in range(1, len(list)):
        # second element
        value = list[i]
        # index of first element
        j = i - 1
        # inner cycle
        # work if j > 0 and first element > second element
        while j > 0 and list[j] > value:
            # list['i'] = list['i-1']
            list[j+1] = list[j]
            j -= j
        list[j+1] = value
    print(list)

insert_sort([2,1,5,6,3,10])
