def find_pivot(arr,start,end):
    """
    Input:
    arr: the rotated, sorted array
    start: the starting index
    end: the ending index
    Output: 
    -1 if there is NO rotation
    otherwise the index of pivot number
    eg [3,4,5,1,2] pviot number is 5 and index is 2
    """
    
    # base condition
    if end < start:
        return -1
    if end == start:
        return end
    
    mid = (start+end)//2
    
    if mid < end and arr[mid]>arr[mid+1]:
        return mid
    if mid > start and arr[mid-1]>arr[mid]:
        return mid-1
    # trigger the recursive call
    if arr[mid]>=arr[start]:
        return find_pivot(arr,mid+1,end)
    else:
        return find_pivot(arr,start,mid-1)


def standard_bs(arr,start,end,target):
    # base condition
    if end < start:
        return -1
    # trigger the recursive call
    mid = (start+end)//2
    if arr[mid]==target:
        return mid
    elif arr[mid]< target:
        return standard_bs(arr,mid+1,end,target)
    else:
        return standard_bs(arr,start,mid-1,target)

def rotated_sorted_search(arr,start,end,target):
    len_arr = len(arr)
    if len_arr==0:
        return -1
    elif len_arr==1:
        if arr[0]==target:
            return 0
        else:
            return -1
        
    # Find the pivot
    pivot_ix = find_pivot(arr,start,end)
    if pivot_ix==len_arr:
        return standard_bs(arr,start,end,target)
    head = arr[0]
    if arr[0]<=target:
        return standard_bs(arr,start,pivot_ix,target)
    else:
        return standard_bs(arr,pivot_ix+1,len_arr,target)
    

######
#test#
######
def linear_search(arr, target):

    """
    Simple straightforward linear search
    """
    for ix, ele in enumerate(arr):
        if ele == target:
            return ix
    return -1
def test_function(test_case):
    input_list = test_case[0]
    s=0
    e=len(input_list)-1
    target = test_case[1]
    if linear_search(input_list, target) == rotated_sorted_search(input_list,s,e,target): 
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[], 10])
test_function([[1], 1])
test_function([[1], 0])
test_function([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 3])

