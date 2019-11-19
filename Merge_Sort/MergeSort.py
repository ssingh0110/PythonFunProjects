def merge(unsorted_list):
    print(unsorted_list)
    if len(unsorted_list) > 1:
        m = len(unsorted_list)//2
        L = unsorted_list[:m]
        R = unsorted_list[m:]
        merge(L)
        merge(R)
        print("Here")
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                unsorted_list[k] = L[i]
                i += 1
            else:
                unsorted_list[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            unsorted_list[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            unsorted_list[k] = R[j]
            j += 1
            k += 1

arr = [int(x) for x in input().split()]
merge(arr) 
print("Sorted array is:", arr) 
