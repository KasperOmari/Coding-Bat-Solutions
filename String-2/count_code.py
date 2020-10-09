def count_code(str):
  return [str[i:i+2]+str[i+3] for i in range(len(str)-3)].count('coe')

