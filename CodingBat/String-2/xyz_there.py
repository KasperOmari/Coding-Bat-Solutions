def xyz_there(st):
  return [st[i:i+3] for i in range(len(st)-2) if i==0 or st[i-1]!='.'].count('xyz') > 0

