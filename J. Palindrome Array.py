n=int(input())
arr=list(map(int,input().split()))
list1=list(reversed(arr))
if(arr==list1):
    print("YES")
else:
    print("NO")