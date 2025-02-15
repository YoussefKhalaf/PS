n=int(input())
arr=list(map(int,input().split()))
min_idx=arr.index(min(arr))
max_idx=arr.index(max(arr))
temp=arr[min_idx]
arr[min_idx]=arr[max_idx]
arr[max_idx]=temp
print(*arr)

# link => https://codeforces.com/group/5pUldkahAU/contest/510058/problem/K