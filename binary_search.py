from random import random
# Creating array
N = 40
array = [int(random()*100) for i in range(N)]
# Sort our array
array.sort()
print(array)


def binary_search(list, x):
    # lowest limit (array start)
    low = 0
    # highest limit (array end)
    high = N - 1

    # main cycle
    while low <= high:
        # caclulate middle index
        mid = (low + high) // 2
        # if searching number lesser then middle indexed number
        # we move highest limit to middle
        if x < list[mid]:
            high = mid - 1
        # if searching number bigger then middle indexed number
        # we move lowest limit to middle
        elif x > list[mid]:
            low = mid + 1
        # else, if searching number == middle indexed number
        # middle index is an answer
        else:
            print('ID = ', mid)
            break
    else:
        print('No number')

number = int(input('Enter number you are looking for: '))
binary_search(array, number)
