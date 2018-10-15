def sum67(nums):
  c=0;f=1
  for i in range(len(nums)):
    if(nums[i]==6 ):
      f=0
    if f:
      c+=nums[i]
    if(nums[i]==7 and not f):
      f=1
  return c

