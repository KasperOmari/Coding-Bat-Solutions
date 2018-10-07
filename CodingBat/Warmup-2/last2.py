def last2(str):
  c = 0 
  for i in range(len(str)-2):
    c += str[i:i+2] == str[-2:]
  return c

