def prime(num):
    flag=False
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                flag = True
                break
        if flag:
            print("not prime")
        else:
            print("prime")
 
num=int(input())
prime(num)
