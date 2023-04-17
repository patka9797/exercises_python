def fibonacci():
    numbers = 0
    while True:
        yield numbers
        numbers +=1
        n1, n2 = 0, 1
        count = 0
    
    
        if numbers == 1:
            print(n1)
<<<<<<< HEAD
        else:
            print("Fibonacci sequence: ")
        while count < numbers:
            print(n1)
            next = n1 + n2
            n1 = n2
            n2 = next
            count += 1


print(fibonacci())
=======
            next=n1+n2
            n1=n2
            n2=next
            count +=1
print(fibonacci())
>>>>>>> 50378364e93c7f3256b22ea999c3792dedc70ed5
