n=int(input())
arr=list(map(int,input().split()))
arr.sort()
list1,list2=[],[]
halflen= int(len(arr)/2)
for i in range(halflen):
    list1.append(arr[i])
for i in range(halflen,n):
    list2.append(arr[i])
print(*list1,end=" ")
list1.reverse()
print(*list1)
list2.reverse()
print(*list2,end=" ")
list2.reverse()
print(*list2)

# link => https://codeforces.com/group/5pUldkahAU/contest/510058/problem/I