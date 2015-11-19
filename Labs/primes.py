def check(n):
    for k in range(2, n//2+1):
        if n % k == 0:
            return k
    return False

def funct(n):
    fac = 1
    fac2 = n
    num = []
    while(fac):
        fac = check(fac2)
        if (fac > 0):
            num.append(fac)
            fac2 = fac2//fac
            fac = check(fac2)
        else:
            num.append(fac2)
            break;
    num.append(fac2)
    return num
