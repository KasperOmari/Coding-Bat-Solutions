def combo_string(a, b):
  if(len(a) < len(b)):
    a,b = b,a #swap the two strings (a=long, b=short)
  return b+a+b

