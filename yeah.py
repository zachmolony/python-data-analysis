# Selection sort
def bubble(arr):
    flag=True
    n = len(arr)
    while(flag == True and n > 1):
        flag = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                flag = True
        n -= 1
    return arr