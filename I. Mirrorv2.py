n=int(input())
arr=list(map(int,input().split()))
arr.sort()
smaller_part=arr[:n//2]
bigger_part=arr[n//2:]
print(*smaller_part,*smaller_part[::-1])
print(*bigger_part[::-1],*bigger_part)
# link => https://codeforces.com/group/5pUldkahAU/contest/510058/problem/I