def sumOfAP( a, d,n) :
    sum = 0
    i = 0
    while i < n :
        sum = sum + a
        a = a + d
        i = i + 1
    return sum
n =5
a =10
d =9
print (sumOfAP(a, d, n))
