def in1to10(n, outside_mode):
  x=((n in range(1,11)) and not outside_mode)
  return  x or ((n <= 1 or n >= 10) and outside_mode)

