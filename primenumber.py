def primenumber(num):
    prime=True
    for i in range(2,num):
        if num%i==0:
            prime=False
            break
    return prime
res=primenumber(6)
print(res)

