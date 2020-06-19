def mergesort(items):
    # base case
    if len(items)<=1:
        return items
    mid = len(items)//2
    left = items[:mid]
    right = items[mid:]
    # recursive call
    left = mergesort(left)
    right = mergesort(right)
    
    return merge(left,right)

def merge(left,right):
    merged = []
    left_ind = 0
    right_ind = 0
    while left_ind<len(left) and right_ind<len(right):
        if left[left_ind]>=right[right_ind]:
            merged.append(right[right_ind])
            right_ind += 1
        else:
            merged.append(left[left_ind])
            left_ind += 1
    merged += left[left_ind:]
    merged += right[right_ind:]
    return merged

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    sorted_arr = mergesort(input_list)
    a1,a2 = '',''
    for index,ele in enumerate(sorted_arr):
        if index%2==0:
            a1 = str(ele) + a1
        else:
            a2 = str(ele) + a2
    return int(a1),int(a2) 

# test
def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")
def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

# Default
test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])

# Repeating Numbers
test_function([[1, 1, 1, 1, 1], [111, 11]])
test_function([[1, 1, 2, 2, 3, 3, 4, 4], [4321, 4321]])

# Out of order with repeating
test_function([[9, 1, 8, 2, 7, 3, 9], [9831, 972]])