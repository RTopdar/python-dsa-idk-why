def hcf(n1,n2):
    if(min(n1,n2)) == 0: return max(n1,n2)
    return hcf(min(n1,n2),max(n1,n2)%min(n1,n2))


print(hcf(50,15))
        

