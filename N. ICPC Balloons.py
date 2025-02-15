t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    listed=[]
    balloons=0
    for i in range(n):
        if s[i] in listed:
            balloons+=1
        else:
            balloons+=2
            listed.append(s[i])
    print(balloons)
    
# link => https://codeforces.com/group/5pUldkahAU/contest/510058/problem/N