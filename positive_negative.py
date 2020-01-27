def count_positives_sum_negatives(arr):
    if arr == None:
        return []
    if len(arr) == 0:
        return []
    new_arr=[0,0]
    for i in arr:
        if i >0:
            new_arr[0]+=1
        elif i <0:
            new_arr[1]+=i
    print (new_arr)
    return new_arr

count_positives_sum_negatives (None)