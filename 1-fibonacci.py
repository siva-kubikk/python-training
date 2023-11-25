print ("Fibonacci Series")

def fibonacci(n):
  a,b=0,1
  f=[]
  while a <= n:
    f.append(a)
    a,b = b, a+b # simultaneous assignment
  print(f)

fibonacci(1000)
