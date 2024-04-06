def comb(arr,n):
    result=[]
    if n==0:
        return result
    if n==1:
        for i in arr:
            result.append([i])
        return  result
    else:
        for i in range(len(arr)-n+1):
            for j in comb(arr[i+1:],n-1):
                result.append([arr[i]]+j)
    return result


arr1=[1,2,3,4,5]
print(comb(arr1,2))






