from bisect import bisect_left,bisect_right
no_numbers,no_queries=map(int,input().split())
list1=list(map(int,input().split()))

positions={}
for i in range(no_numbers):
    num=list1[i]
    if num not in positions:
        positions[num]=[]
    positions[num].append(i+1)
for _ in range(no_queries):
    l,r,x=map(int,input().split())
    if x not in positions:
        print(0)
        continue
    indices = positions[x]
    left=bisect_left(indices,l)
    right=bisect_right(indices,r)
    print(right-left)
    
# link => https://codeforces.com/group/5pUldkahAU/contest/510058/problem/H