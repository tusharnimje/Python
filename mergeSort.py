def merge(arr, start, mid, end):

    temp = [None] * (end-start+1)

    i = start
    j = mid + 1
    k = 0

    while i <= mid and j <= end:
        if arr[i] < arr[j]:
            temp[k] = arr[i]
            i += 1
            k += 1
        else: 
            temp[k] = arr[j]
            j += 1
            k += 1
    
    
    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    while j <= end:
        temp[k] = arr[j]
        j += 1
        k += 1

    k = 0

    for i in range(start, end+1):
        arr[i] = temp[k]
        k += 1

    
def mergeSort(arr, start, end):
    if start < end:
        mid = (start + end) // 2
        mergeSort(arr,start,mid)
        mergeSort(arr,mid+1,end)
        merge(arr,start,mid,end)

if __name__ == "__main__":
    n = 8
    arr = [5, 20, 30, 45, 10, 25, 28, 40]
    mergeSort(arr,0,n-1)
    for i in range(len(arr)):
        print(arr[i], end = " ")

