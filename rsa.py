def mInverse(a, n):
    r0, r1, t0, t1 = n, a, 0, 1
    while r1 > 1:
        q = r0 // r1
        r2 = r0 - r1 * q
        t2 = t0 - t1 * q
        r0, r1 = r1, r2
        t0, t1 = t1, t2
 
    if r1 == 1:
        return t1 % n
    return 0


def rsaencrypt(value,n,e):
    y=pow(value,e,n)
    return y
    
def rsadecrypt(value,n,d):
    x= pow(value,d,n)
    return x
    
def rsahack(n,e):
    for i in range(2,n//2):
        if n%i==0:
            break
        
    pr=n//i
    phi=(pr-1)*(i-1)
    d=mInverse(e,phi)
    return d
    