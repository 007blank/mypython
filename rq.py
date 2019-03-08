def solve():
    a=int(input())
    b=int(input())
    q=int(a/b)
    r=a%b
    return q,r
q,r=solve()
print(q)
print(r)
