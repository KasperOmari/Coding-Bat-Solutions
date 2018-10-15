def string_match(a, b):
  if len(a) > len(b):
    a,b = b,a #a always has the shorter length
  D = {} 
  for i in range(len(a)-1):
      if(a[i:i+2] == b[i:i+2]):
        D[a[i:i+2]]=1
  return len(D)

