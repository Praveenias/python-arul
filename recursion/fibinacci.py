def fibonacchi(n):
  if n==0:
    return 0
  if n==1:
    return 1
  return fibonacchi(n-1)+fibonacchi(n-2)

print(fibonacchi(2))
