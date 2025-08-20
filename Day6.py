def zero_sum_subarrays(arr):
    n = len(arr)
    result = []
    sum = 0
    seen = {0: [-1]} 

    for i in range(n):
        sum += arr[i]

        if sum in seen:
            for j in seen[sum]:
                result.append([j+1 , i])  

        seen.setdefault(sum, []).append(i)

    return result
arr = list(map(int,input().split()))
print(zero_sum_subarrays(arr))
