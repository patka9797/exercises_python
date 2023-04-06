def smallest_sum(N):
    sum=0
    while (N != 0):
        sum += N%10
        N = N//10
    return sum

def smallest_number(N1):
    i=1
    while (1):
        if (smallest_sum(i)==N1):
            print(i)
        break
    i += 1

        
N1=10
print(smallest_number(N1))
