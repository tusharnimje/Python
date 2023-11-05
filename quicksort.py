def partition(arr, start, end):
    pIndex = start
    pivot = arr[end]

    for i in range(start, end):
        if arr[i] < pivot:
            arr[i], arr[pIndex] = arr[pIndex], arr[i]
            pIndex += 1

    arr[end], arr[pIndex] = arr[pIndex], arr[end]
    return pIndex

def quickSort(arr, start, end):
    if start < end: 
        pi = partition(arr,start,end);
        quickSort(arr,start,pi-1);
        quickSort(arr,pi+1,end);

if __name__ == "__main__":
    n = 5
    arr = [10, 25, 3, 50, 20]
    quickSort(arr,0,n-1)
    print("Array in sorted order :")
    for i in range(len(arr)):
        print(arr[i], end = " ");

