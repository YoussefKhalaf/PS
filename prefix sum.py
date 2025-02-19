def prefix_sum(arr):
    n=len(arr)
    prefix = [0]*(n+1)
    for i in range(n):
        prefix[i+1]=prefix[i]+arr[i]
    return prefix

def sum(prefix,l,r):
    return prefix[r]-prefix[l-1]

arr=list(map(int,input().split()))
l,r=map(int,input().split())
prefix=prefix_sum(arr)
print(sum(prefix,l,r))

