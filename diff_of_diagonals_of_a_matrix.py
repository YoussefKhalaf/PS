rows=int(input())
columns=rows
matrix=[]
for _ in range(rows):
    nums=list(map(int,input().split()))
    matrix.append(nums)
diagonal1=0
for i in range(rows):
    diagonal1+=matrix[i][i]
diagonal2=0
for i in range(rows):
    diagonal2+=matrix[i][rows-i-1]
print(abs(diagonal1-diagonal2))