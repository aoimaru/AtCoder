import math
 
n = int(input())

i = 0
 
if n == 1:
  print(0)
else:
  while True:
    p = pow(2, i)
    if p > n:
        print(i-1)
        break
    i+=1

 
