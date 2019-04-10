def testcase(c):
  if ord( c ) >= ord( 'a' ) and ord( c ) <= ord( 'z' ):
    return 1
  elif ord( c ) >= ord( 'A' ) and ord( c ) <= ord( 'Z' ):
    return 2
  else:
    return 0
    
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

def afencode(text,a ,b):
    mstr=""
    for ch in text:
        if testcase(ch)==0:
            mstr=mstr+ch
            continue
        elif testcase(ch)==1:
            x=97
        else:
            x=65
        m=((ord(ch)-x)*a+b)%26
        char=chr(m+x)
        mstr=mstr+ char
        
    return mstr  
    
def afdecode(cipher,a,b):
    mst=""
    inv=mInverse(a,26)
    for ch in cipher:
        if testcase(ch)==0:
            mst=mst+ch
            continue
        elif testcase(ch)==1:
            x=97
        else:
            x=65
        m=((ord(ch)-x-b)*inv)%26
        char=chr(m+x)
        mst=mst+ char
    return mst    
    

            
            
        