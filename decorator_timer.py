from time import time

start=time.time()



def sum_time(n):
    sum=0
    for i in range(n):
       sum += i

time.sleep(2)

print(sum_time(10000))

stop=time.time()

elapsed_time = stop - start 

print('Execution time:', elapsed_time)
           

