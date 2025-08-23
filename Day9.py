def longestCommonPrefixer(arr):
        if not arr:
            return ""
        for i in range(len(arr[0])):
            ch = arr[0][i]
            for s in arr[1:]:
                if i >= len(s) or s[i] != ch:
                    return arr[0][:i]
        return arr[0]
arr=list(map(str,input().split()))
print(longestCommonPrefixer(arr))
