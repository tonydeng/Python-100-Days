
for i in range(1000,10000):
    # a = i // 1000
    # b = (i%1000) // 100
    # c = (i%100) // 10
    # d = i%10

    a = int(str(i)[0])
    b = int(str(i)[1])
    c = int(str(i)[2])
    d = int(str(i)[3])
    
    m = pow(a,4)+pow(b,4)+pow(c,4)+pow(d,4)
    
    if m == i:
        print(i)
