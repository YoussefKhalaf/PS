n,m=map(int,input().split())
arr=list(map(int,input().split()))
dic={}
for i in arr:
    dic[i]=dic.get(i,0)+1
for i in range(1,m+1):
    print(dic.get(i,0))
    
# link => https://codeforces.com/group/5pUldkahAU/contest/510058/problem/O