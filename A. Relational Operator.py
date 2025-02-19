t=int(input())
def relationalOperator(n1,n2):
    if n1>n2:
        return '>'
    elif n1<n2:
        return '<'
    else:
        return '='
for _ in range(t):
    n1,n2=map(int,input().split())
    result=relationalOperator(n1,n2)
    print(result)
    
# link => https://codeforces.com/group/hzMGsVHkMR/contest/354318/problem/A