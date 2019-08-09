def mergeSort(a):

    if len(a)<2:
        return a

    mid = int(len(a)/2)
    # left = mid
    # right = n - mid
    left, right = mergeSort(a[:mid]), mergeSort(a[mid:])
    return merge(left, right)

def merge(left, right):

    result = []
    left_pointer = right_pointer = 0

    while left_pointer < len(left) and right_pointer < len(right):

        if left[left_pointer] < right[right_pointer]:

            result.append(left[left_pointer])
            left_pointer += 1
        else:
            result.append(right[right_pointer])
            right_pointer += 1

    result.extend(left[left_pointer:])
    result.extend(right[right_pointer:])

    return result


a = [2,4,1,6,8,5,3,7]
# a = [5,4,3,2,1]
b = mergeSort(a)

print(b)