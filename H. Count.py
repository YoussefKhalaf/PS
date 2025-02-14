no_numbers,no_queries=map(int,input().split())
list1=list(map(int,input().split()))
for i in range(no_queries):
    no_times=0
    l,r,x=map(int,input().split())
    for j in range(l-1,r):
        if(list1[j]==x):
            no_times+=1
    print(no_times)