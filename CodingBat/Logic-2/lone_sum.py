def lone_sum(a, b, c):
  x = [a,b,c]
  x = [i for i in x if x.count(i) == 1]
  return 0 if len(x) == 0 else reduce(lambda x,y:x+y, x)

