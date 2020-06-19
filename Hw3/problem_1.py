def sqrt(num):
    """
    Input: num
    Output: floor of its square root
    """
    if num < 0:
        raise ValueError( "Input must be non-negative!")

    if num in [0,1]:
        return num
    start = 1
    end = num
    while start <= end:
        mid = (start+end)//2
        if mid*mid == num:
            return mid
        elif mid*mid<num:
            start = mid+1
            ans = mid
        else:
            end = mid - 1
    return ans
    



# a linear function
def sqrt_linear(num):
    if num ==0:
        return 0
    i=0
    while i*i <= num:
        i+=1
    return i-1

# test, 100 cases
for i in range(100):
    if sqrt_linear(i)!= sqrt(i):
        print("Fail")
    else:
        print('Pass')

# Negative input generates ValueError
print(sqrt(-1))