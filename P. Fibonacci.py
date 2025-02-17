from functools import lru_cache
@lru_cache(None)  #Least Recently Used Cache
def fib(n):
    if n==1:
        return 0 
    elif n==2:
        return 1
    return fib(n-1)+fib(n-2)
n=int(input())
print(fib(n))
# link => https://codeforces.com/group/5pUldkahAU/contest/510058/problem/P