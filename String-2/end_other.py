def end_other(a, b):
  if len(a) < len(b):
    a,b = b,a
  b=b.lower();a=a.lower()
  
  return a.endswith(b)

