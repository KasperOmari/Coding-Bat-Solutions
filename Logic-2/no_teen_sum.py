def fix(n):
  return 0 if n in range(13,20) and n not in [15,16] else n
def no_teen_sum(a, b, c):
  return fix(a)+fix(b)+fix(c)

